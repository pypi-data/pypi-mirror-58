import re
import logging
import markdown
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension
from mdtest.structures import MdTest, CommandCode, CommandBlock


class TestParser:
    def __init__(self):
        self.tests = []
        self.current_test_level = None

    def getTests(self):
        return self.tests

    def walk(self, parent_element):
        logging.debug("markdownparser: walk(%s)", str(parent_element))
        for e in parent_element:
            _log_element(e)

            self._check_for_test_end(e)
            self._check_for_new_test(e, parent_element)

            if self.current_test_level:
                self._parse_in_test_element(e, parent_element)

            self.walk(e)

    def _check_for_test_end(self, e):
        if _is_header(e) and self.current_test_level:
            if _get_header_level(e) < self.current_test_level:
                logging.debug(
                    "markdownparser: higher or same level header - ending test")
                self.current_test_level = None

    def _check_for_new_test(self, e, parent_element):
        if _is_concordion_link(e) and _is_header(parent_element):
            self._optionally_create_new_test(e, parent_element)

    def _optionally_create_new_test(self, e, parent_element):
        if "c:status=" in _get_concordion_command(e):
            self.current_test_level = None
        else:
            self.tests.append(_create_test(e.text, _get_concordion_command(e)))
            self.current_test_level = _get_header_level(parent_element)

    def _parse_in_test_element(self, e, parent_element):
        if _is_concordion_link(e) and not _is_header(parent_element):
            code = _get_concordion_command(e)
            self._add_command_to_test(CommandCode(''.join(e.itertext()), code))
        if e.tag == 'code':
            self._add_command_to_test(CommandBlock(e.text))

    def _add_command_to_test(self, cmd):
        logging.debug("markdownparser: add command %s", cmd)
        self._get_cur_test().add_command(cmd)

    def _get_cur_test(self):
        return self.tests[-1]


def _log_element(e):
    logging.debug("markdownparser: visited element: tag=%s text=%s href=%s title=%s", str(
        e.tag), str(e.text),  str(e.get('href')), str(e.get('title')))


def _create_test(name, fixture):
    logging.debug(
        "markdownparser: create test %s with fixture %s", name, fixture)
    return MdTest(name, fixture)


def _is_concordion_link(element):
    return element.tag == 'a' and element.get('href') == '-'


def _is_header(element):
    return element.tag.startswith('h')


def _get_header_level(element):
    return int(element.tag[1:])


def _get_concordion_command(element):
    return element.get('title')


class ConcordionLinkExtractor(Treeprocessor):
    def run(self, doc):
        "Find all Concordion links and append to markdown.concordionTests."
        testparser = TestParser()
        testparser.walk(doc)
        self.md.concordionTests = testparser.getTests()


class ConcordionExtension(Extension):
    def extendMarkdown(self, md):
        concordionTests_ext = ConcordionLinkExtractor(md)
        md.treeprocessors.register(concordionTests_ext, 'concordionTests', 10)


def parseMarkdownForConcordionTests(string):
    md = markdown.Markdown(extensions=[ConcordionExtension()])
    html_from_md = md.convert(string)
    logging.debug("markdownparser: generated html: %s", str(html_from_md))
    return md.concordionTests
