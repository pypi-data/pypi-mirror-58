from setuptools import setup, find_packages

setup(name='fracture-contracts',
      version='0.2',
      description='The functionality of dpcontracts with improved error messages',
      url='https://github.com/Fracture17/contracts',
      author='Fracture',
      packages=find_packages(),
      install_requires=[
          'hypothesis',
          'pytest',
          'pytest-pycharm'
      ])