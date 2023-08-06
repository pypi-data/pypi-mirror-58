import re
import logging
from mdtest.structures import CommandCode, CommandBlock, CompiledMdTest
from mdtest.commandgenerators import (
    get_generators_commands, generate_set, generate_code_python_symantics
)


def parseTest2code(test):
    code_writer = CodeWriter()
    cmd_parser = CommandParser()
    compiled_test = CompiledMdTest(test)

    code_writer.add_import(
        compiled_test.get_fixture_python_name(), test.get_lineno())
    code_writer.add_function(
        compiled_test.get_test_func_name(), test.get_lineno())

    command_array = _make_block_assigns_first(test.get_commands())
    for cmd in command_array:
        _substitute_TEST_NAME_variable(cmd, test.get_name())
        code_writer.add_statement(
            cmd_parser.parse_command(cmd),
            cmd.get_lineno())
    code_writer.store_result_in(compiled_test)
    return compiled_test


class CodeWriter():

    def __init__(self):
        self._code = ""
        self._code2source_map = [0]
        self._number_of_statements = -1

    def add_import(self, module, source_lineno=0):
        self._add_to_code("from %s import *\n\n" % (module), source_lineno)

    def add_function(self, func_name, source_lineno=0):
        self._add_to_code("def %s(self):\n" % (func_name), source_lineno)
        self._number_of_statements = 0

    def add_statement(self, statement, source_lineno=0):
        self._add_to_code("    "+statement + "\n", source_lineno)
        self._number_of_statements += 1

    def store_result_in(self, compiled_test):
        if self._number_of_statements == 0:
            self.add_statement("pass")

        compiled_test.set_code(self._code)
        compiled_test.set_code2source_map(self._code2source_map)

    def _add_to_code(self, string, source_lineno=0):
        self._code += string
        self._code2source_map += [source_lineno]*string.count('\n')


def _make_block_assigns_first(command_array):
    blocks_commands = []
    other_commands = []
    for cmd in command_array:
        if isinstance(cmd, CommandBlock):
            blocks_commands.append(cmd)
        else:
            other_commands.append(cmd)
    return blocks_commands + other_commands


def _substitute_TEST_NAME_variable(cmd, test_name):
    if isinstance(cmd, CommandCode):
        cmd.set_code(re.sub('#TEST_NAME',
                            '"""' + test_name+'"""',
                            cmd.get_code()))


def _substitute_TEXT_variable(cmd):
    cmd.set_code(re.sub('#TEXT', '"""'+cmd.get_text()+'"""', cmd.get_code()))


class CommandParser:

    def __init__(self):
        self.code_block_count = 0

    def parse_command(self, cmd):
        if isinstance(cmd, CommandBlock):
            self.code_block_count += 1
            return generate_set(CommandCode(
                cmd.get_block(),
                'code'+str(self.code_block_count))
            )

        _substitute_TEXT_variable(cmd)

        for gen in get_generators_commands():
            if bool(re.search(gen['re'], cmd.get_code())):
                return (gen['generator'])(cmd)

        return generate_code_python_symantics(cmd.get_code())
