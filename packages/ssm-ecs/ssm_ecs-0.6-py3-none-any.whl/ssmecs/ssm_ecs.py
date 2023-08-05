import argparse
import contextlib
import json
import errno
import signal
import sys
import random
import boto3
from subprocess import check_call

# This enhances the input prompt but is not available on Windows
try:
    import readline
except ImportError:
    pass

ERROR_MESSAGE = (
    'SessionManagerPlugin is not found. ',
    'Please refer to SessionManager Documentation here: ',
    'http://docs.aws.amazon.com/console/systems-manager/',
    'session-manager-plugin-not-found'
)

session = boto3.session.Session()


def start():
    parser = argparse.ArgumentParser(
        description='Start a shell session inside an ECS container using SSM Session Manager.')
    parser.add_argument('--cluster', '-cl', default='',
                        help='The short name or full Amazon Resource Name (ARN) of the cluster.')
    parser.add_argument('--service', '-s', default='', help='The name of the service.')
    parser.add_argument('--command', '-co', default='/bin/bash', help='Command to run inside the container. Defaults to'
                                                                      ' starting a bash shell.')
    args = parser.parse_args()

    ecs_client = boto3.client('ecs')

    cluster = args.cluster
    if not cluster:
        cluster_arns = ecs_client.list_clusters(maxResults=100)['clusterArns']
        for index, cluster_arn in enumerate(cluster_arns):
            name = cluster_arn.split('/', 1)[1]
            print(f'[{ index }] { name }')

        choice = input('Please choose a cluster: ')
        try:
            # Try to convert to int and use as index in list
            cluster = cluster_arns[int(choice)].split('/', 1)[1]
        except ValueError:
            # Otherwise use input as cluster name
            cluster = choice

    service = args.service
    if not service:
        service_arns = ecs_client.list_services(cluster=cluster, maxResults=100)['serviceArns']
        for index, service_arn in enumerate(service_arns):
            name = service_arn.split('/', 1)[1]
            print(f'[{ index }] { name }')

        choice = input('Please choose a service: ')
        try:
            # Try to convert to int and use as index in list
            service = service_arns[int(choice)].split('/', 1)[1]
        except ValueError:
            # Otherwise use input as service name
            service = choice

    # Pick a random task ARN for this service
    task_arn = random.choice(ecs_client.list_tasks(cluster=cluster, serviceName=service)['taskArns'])
    # There should be exactly one task with this ARN
    task = ecs_client.describe_tasks(cluster=cluster, tasks=[task_arn])['tasks'][0]
    container_instance_arn = task['containerInstanceArn']
    task_definition_arn = task['taskDefinitionArn']

    # There should be exactly one container instance with this ARN
    container_instance = ecs_client.describe_container_instances(
        cluster=cluster,
        containerInstances=[container_instance_arn]
    )['containerInstances'][0]
    ec2_instance_id = container_instance['ec2InstanceId']

    task_definition = ecs_client.describe_task_definition(taskDefinition=task_definition_arn)['taskDefinition']
    task_definition_family = task_definition['family']
    task_definition_revision = task_definition['revision']
    container_name = task_definition['containerDefinitions'][0]['name']

    parameters = {
        'Target': ec2_instance_id,
        'DocumentName': 'RunCommand',
        'Parameters': {
            'command': [
                f'docker exec -it $(docker ps --filter "name=ecs-{task_definition_family}-{task_definition_revision}-'
                f'{container_name}-" --format {{{{.ID}}}} --latest) {args.command}'
            ]
        }
    }

    ssm_client = boto3.client('ssm')

    response = ssm_client.start_session(**parameters)
    session_id = response['SessionId']

    region_name = session.region_name
    # profile_name is used to passed on to session manager plugin
    # to fetch same profile credentials to make an api call in the plugin.
    # If no profile is passed then pass on empty string
    profile_name = session.profile_name
    endpoint_url = ssm_client.meta.endpoint_url

    try:
        # ignore_user_entered_signals ignores these signals
        # because if signals which kills the process are not
        # captured would kill the foreground process but not the
        # background one. Capturing these would prevents process
        # from getting killed and these signals are input to plugin
        # and handling in there
        with ignore_user_entered_signals():
            # call executable with necessary input
            check_call(["session-manager-plugin",
                        json.dumps(response),
                        region_name,
                        "StartSession",
                        profile_name,
                        json.dumps(parameters),
                        endpoint_url])
        sys.exit(0)
    except OSError as ex:
        if ex.errno == errno.ENOENT:
            # start-session api call returns response and starts the
            # session on ssm-agent and response is forwarded to
            # session-manager-plugin. If plugin is not present, terminate
            # is called so that service and ssm-agent terminates the
            # session to avoid zombie session active on ssm-agent for
            # default self terminate time
            ssm_client.terminate_session(SessionId=session_id)
            raise ValueError(''.join(ERROR_MESSAGE))


@contextlib.contextmanager
def ignore_user_entered_signals():
    """
    Ignores user entered signals to avoid process getting killed.
    """
    if sys.platform == 'win32':
        signal_list = [signal.SIGINT]
    else:
        signal_list = [signal.SIGINT, signal.SIGQUIT, signal.SIGTSTP]
    actual_signals = []
    for user_signal in signal_list:
        actual_signals.append(signal.signal(user_signal, signal.SIG_IGN))
    try:
        yield
    finally:
        for sig, user_signal in enumerate(signal_list):
            signal.signal(user_signal, actual_signals[sig])