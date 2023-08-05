from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='gplpy',
      version='1.1.0',
      author='aturing',
      author_email="itic@aturing.com",
      description='Grammar-Guided Genetic Programming Library',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/aturing/GPLpy.git',
      license='Apache License 2.0',
      packages=find_packages(),
      install_requires=['numpy','scipy','pandas','matplotlib','pymongo[srv]'],
      python_requires='>=3.6',
) 
