import re
import logging
import ast
from mdtest.structures import CommandCode


class SourceScaner:
    def __init__(self, source):
        self.lines = source.splitlines(True)
        self.lineno = 1

    def get_next_lineno_matching(self, regex):
        for lineno, line in enumerate(self.lines):
            m = re.search(regex, line)
            if m:
                self.lines = [line[m.end():]]+self.lines[lineno+1:]
                self.lineno += lineno
                return self.lineno


def _get_mdtesturl_regex(text, command):
    return r'\[{}\]\(\s*-\s*"{}"\)'.format(
        re.escape(text),
        re.escape(command))


def _get_mdtesturl_besttry_regex(text, command):
    return r'\[.*{}.*\]\(\s*-\s*"{}"\)'.format(
        re.escape(text),
        re.escape(command))


def annotate_source_lineno(mdtests, source):
    scanner = SourceScaner(source)
    for test in mdtests:
        _annotate_test(test, scanner)
        for cmd in test.get_commands():
            if isinstance(cmd, CommandCode):
                _annotate_cmd(cmd, scanner)


def _annotate_test(test, scanner):
    _annotate_link(test, test.get_name_in_source(),
                   test.get_fixture_in_source(), scanner)


def _annotate_cmd(cmd, scanner):
    _annotate_link(cmd, cmd.get_text(), cmd.get_code(), scanner)


def _annotate_link(what, text, code, scanner):
    regex = _get_mdtesturl_regex(text, code)
    lineno = scanner.get_next_lineno_matching(regex)
    if not lineno:
        regex = _get_mdtesturl_besttry_regex(text, code)
        lineno = scanner.get_next_lineno_matching(regex)
    if not lineno:
        lineno = 0
    what.set_lineno(lineno)


def fix_lineno(node, compiled_mdtest):
    generated_to_source = compiled_mdtest.get_code2source_map()
    logging.debug("linefixer: fix_lineno using map: %s",
                  str(generated_to_source))

    for child in ast.walk(node):
        if 'lineno' in child._attributes:
            lineno_in_genereted = getattr(child, 'lineno', 0)

            child.lineno = generated_to_source[lineno_in_genereted]
    return node
