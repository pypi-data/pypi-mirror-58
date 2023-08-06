"""Markdown Test (mdtest)

Runs tests embedded in markdown similar to way as pytest does.

Usage:
  mdtest [--skip=TEST_NAME]...
  mdtest TEST_SUITE... [--skip=TEST_NAME]...
  mdtest (-h | --help)

Options:
  -h --help                   Show this screen.
  --skip=TEST_NAME            Skips test with given name.
"""

import os
import sys
import logging
from docopt import docopt
from mdtest.discover import discover_mdfiles
from mdtest import testrunner
from mdtest import mdcompiler


def get_cli_arguments():
    arguments = docopt(__doc__)
    logging.info('Started with arguments: %s' % (str(arguments)))
    return arguments


def add_std_fixture_to_path():
    this_path = os.path.dirname(os.path.abspath(__file__))
    fixture_path = os.path.join(this_path, "fixture")
    sys.path.append(fixture_path)


def readfile(filename):
    logging.info("Reading %s", filename)
    with open(filename, 'r') as file:
        data = file.read()
    return data


def read_and_compile_mdfiles(test_runner, mdfiles):
    complier = mdcompiler.MdComplier(test_runner)
    for mdfile in mdfiles:
        data = readfile(mdfile)
        complier.compile(data, mdfile)


def main(glob):
    logging.basicConfig(filename='mdtest.log', level=logging.DEBUG)

    arguments = get_cli_arguments()

    mdfiles = arguments['TEST_SUITE']
    if not mdfiles:
        mdfiles = discover_mdfiles()

    test_runner = testrunner.TestRunner()
    test_runner.add_markdown_paths_to_pythonpath(mdfiles)
    add_std_fixture_to_path()

    read_and_compile_mdfiles(test_runner, mdfiles)

    test_runner.skip_tests(arguments['--skip'])

    test_runner.run_all_test(glob)

    logging.info('Testing finished')
