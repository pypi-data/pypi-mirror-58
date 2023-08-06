from setuptools import setup

setup(name='mdtest',
      version='0.1.0',
      description='Framework for running tests embedded in markdown files.',
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
