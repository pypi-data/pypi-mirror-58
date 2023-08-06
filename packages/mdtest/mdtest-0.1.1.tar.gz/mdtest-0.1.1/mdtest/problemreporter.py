import re
import sys
import logging
import traceback


class ProblemReporter:

    def exception_during_compilation(self, exception, compiled_mdtest):
        logging.error(
            "testrunner: error ocurred during compilation of %s:\n %s" % (
                compiled_mdtest.get_source_file_name(),
                str(traceback.format_exc())))

        problem = self._get_problem_with_line_fixed(exception, compiled_mdtest)

        sys.stderr.write("Error in %s: %s: %s\n" % (
            compiled_mdtest.get_source_file_name(),
            compiled_mdtest.get_test_func_name(),
            problem))

    def _get_problem_with_line_fixed(self, exception, compiled_mdtest):
        problem = str(exception)
        if not re.search(r"<\S+>", problem):
            return problem
        m = re.search(r"line (\d+)", problem)
        if m:
            line = int(m.group(1))
            line = compiled_mdtest.get_code2source_map()[line]
            problem = re.sub(r"line \d+", "line %d" % (line,), problem)
            problem = re.sub(r"while parsing \(<unknown>, line \d+\)",
                             "while parsing line %d - missing bracket in command?" % (
                                 line,),
                             problem)
        return problem
