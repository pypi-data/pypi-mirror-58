from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='mdtest',
      version='0.1.1',
      description='Framework for running tests embedded in markdown files.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/kgrzywocz/mdtest',
      author='Krzysztof Grzywocz',
      author_email='kgrzywocz@wp.pl',
      license='LGPLv3',
      packages=['mdtest', 'mdtest/fixture'],
      install_requires=[
          'python_version>="3.5"',
          'Markdown>=3',
          'docopt>=0.5'
      ],
      scripts=['bin/mdtest'],
      zip_safe=True,
)
