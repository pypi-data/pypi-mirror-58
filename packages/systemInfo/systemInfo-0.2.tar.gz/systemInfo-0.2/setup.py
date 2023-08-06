from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='systemInfo',
      version='0.2',
      description='Implementation of system information apis',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='',
      author='sudarshan',
      author_email='sudarshanadmuthe@gmail.com',
      keywords='system configuration information',
      license='GPLv3',
      packages=['system'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)