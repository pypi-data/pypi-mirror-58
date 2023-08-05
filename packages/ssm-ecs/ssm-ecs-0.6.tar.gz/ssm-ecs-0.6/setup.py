from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='ssm-ecs',
      version='0.6',
      description=readme.partition('\n')[0],
      long_description=readme,
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console'
      ],
      keywords='amazon aws ssm ecs',
      url='https://github.com/umzegher/ssm-ecs',
      author='Ben Zeghers',
      license='MIT',
      packages=['ssmecs'],
      install_requires=[
          'boto3',
      ],
      entry_points={
          'console_scripts': ['ssm-ecs=ssmecs.ssm_ecs:start'],
      },
      include_package_data=True,
      zip_safe=False)
