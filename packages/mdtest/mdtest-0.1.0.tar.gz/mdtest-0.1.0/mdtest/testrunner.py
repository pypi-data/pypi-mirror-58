import os
import sys
import ast
import logging
import traceback
import unittest
from mdtest import linefixer, problemreporter


class DynamicClassBase(unittest.TestCase):
    longMessage = True
    maxDiff = None


class TestRunner():

    def __init__(self):
        self.env_test_runner = {}
        self.problem_reporter = problemreporter.ProblemReporter()

    def add_markdown_paths_to_pythonpath(self, mdfiles):
        paths = {os.path.dirname(file) for file in mdfiles}
        for path in paths:
            logging.info("Adding python fixture path: %s", str(path))
            sys.path.append(path)

    def add_test(self, compiled_mdtest):
        test_fixture_name = compiled_mdtest.get_testfixture_name()
        test_func_name = compiled_mdtest.get_test_func_name()
        logging.info("testrunner: Adding %s" % (test_fixture_name))

        env_test_globals = {}
        env_test_locals = env_test_globals

        try:
            astree = ast.parse(compiled_mdtest.get_code())
            astree = linefixer.fix_lineno(astree, compiled_mdtest)
            test_codeobj = compile(astree,
                                   compiled_mdtest.get_source_file_name(),
                                   'exec')

            exec(test_codeobj, env_test_globals, env_test_locals)
        except Exception as e:
            self.problem_reporter.exception_during_compilation(
                e, compiled_mdtest)
            exit(-1)

        self.env_test_runner[test_fixture_name] = type(
            test_fixture_name,
            (DynamicClassBase,),
            {test_func_name: env_test_globals[test_func_name]}
        )

    def skip_tests(self, tests_to_skip):
        for test_name_to_skip in tests_to_skip:
            for test in self.env_test_runner:
                if test_name_to_skip in str(test):
                    self.env_test_runner[test] = unittest.skip(
                        self.env_test_runner[test])

    def get_env(self):
        return self.env_test_runner

    def run_all_test(self, globals):
        logging.info("testrunner: Running all tests")
        logging.debug("testrunner env: %s", str(self.env_test_runner))
        globals.update(self.env_test_runner)
        unittest.main(argv=[sys.argv[0]], verbosity=1)
