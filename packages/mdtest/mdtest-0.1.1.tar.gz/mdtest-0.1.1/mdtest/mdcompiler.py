from mdtest import markdownparser
import logging
from mdtest import linefixer, codegenerator


class MdComplier:

    def __init__(self, test_runner):
        self.test_runner = test_runner

    def compile(self, data, file_name):
        tests = markdownparser.parseMarkdownForConcordionTests(data)
        linefixer.annotate_source_lineno(tests, data)
        logging.debug("Parsed md into: %s", str(tests))

        for test in tests:
            logging.info("Compiling test: %s", test.get_name())
            compiled_mdtest = codegenerator.parseTest2code(test)
            compiled_mdtest.set_source_file_name(file_name)

            logging.debug("Compiled test to:<code>\n%s</code>",
                          compiled_mdtest.get_code())
            self.test_runner.add_test(compiled_mdtest)
