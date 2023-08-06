import re


def escape_name(s):
    s = re.sub(" ", "_", s)
    s = ''.join(filter(lambda c: c.isalnum() or c == '_', s))
    return s


class MdTest:

    def __init__(self, name, fixture, lineno=0):
        self.name = name
        self.fixture = fixture
        self.lineno = lineno
        self.commands = []

    def get_name(self):
        return escape_name(self.name)

    def get_name_in_source(self):
        return self.name

    def get_fixture(self):
        return escape_name(self.fixture)

    def get_fixture_in_source(self):
        return self.fixture

    def get_lineno(self):
        return self.lineno

    def set_lineno(self, lineno):
        self.lineno = lineno

    def get_commands(self):
        return self.commands

    def add_command(self, cmd):
        self.commands.append(cmd)

    def add_commands(self, cmd):
        self.commands += cmd

    def __eq__(self, other):
        if not isinstance(other, MdTest):
            return NotImplemented
        return (self.get_name() == other.get_name()
                and self.get_fixture() == other.get_fixture()
                and self.commands == other.commands)

    def __hash__(self):
        return hash((self.get_name(), self.get_fixture(), self.commands))

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        return ("MdTest: "+self.get_name()
                + " fixture: "+self.get_fixture()
                + " commands: "+self.get_commands())


class Command:

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)


class CommandCode(Command):

    def __init__(self, text, code):
        self.text = text
        self.code = code
        self.lineno = 0

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_text(self):
        return self.text

    def get_lineno(self):
        return self.lineno

    def set_lineno(self, lineno):
        self.lineno = lineno

    def __eq__(self, other):
        if not isinstance(other, CommandCode):
            return NotImplemented
        return self.text == other.text and self.code == other.code

    def __hash__(self):
        return hash((self.text, self.code))


class CommandBlock(Command):

    def __init__(self, block):
        self.block = block
        self.lineno = 0

    def get_block(self):
        return self.block

    def get_lineno(self):
        return self.lineno

    def set_lineno(self, lineno):
        self.lineno = lineno

    def __eq__(self, other):
        if not isinstance(other, CommandBlock):
            return NotImplemented
        return self.block == other.block

    def __hash__(self):
        return hash((self.block))


class CompiledMdTest:
    def __init__(self, mdtest):
        self.code = None
        self.test_name = mdtest.get_name()
        self.fixture = mdtest.get_fixture()
        self.source_file_name = None
        self.code2source_map = None

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_fixture(self):
        return self.fixture

    def get_fixture_python_name(self):
        return "fixture_%s" % self.fixture

    def get_testfixture_name(self):
        return 'Test_{0}_{1}'.format(
            escape_name(self.get_source_file_name()),
            self.get_test_func_name()
        )

    def get_test_func_name(self):
        return "test_%s" % self.test_name

    def get_source_file_name(self):
        if self.source_file_name:
            return self.source_file_name
        else:
            return "<<compiled_md_test>>"

    def set_source_file_name(self, file_name):
        self.source_file_name = file_name

    def get_code2source_map(self):
        return self.code2source_map

    def set_code2source_map(self, code2source_map):
        self.code2source_map = code2source_map
