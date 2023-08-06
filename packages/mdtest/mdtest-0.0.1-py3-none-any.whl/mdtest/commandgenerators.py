import re
import logging


def get_generators_commands():
    return _generators_commands


def generator_for_explicit_commands(cmd):
    code = cmd.get_code()
    command = str(re.search(_REGEX_EXPLICIT_COMMAND, code).group(1))
    cmd.set_code(re.sub(_REGEX_EXPLICIT_COMMAND, '', code))

    if command in _generators_explicit_commands:
        return _generators_explicit_commands[command](cmd)

    logging.error('codegenerator: Unsupported  command: "%s"' % (code,))
    return 'Unsupported  command: "%s"' % (code,)


def generate_set(cmd):
    return '%s = """%s"""' % (
        generate_code_python_symantics(cmd.get_code()), cmd.get_text())


def generate_assert(cmd):
    return 'self.assertEqual( """%s""", %s)' % (
        cmd.get_text(),
        generate_code_python_symantics(remove_assert_prefix(cmd.get_code())),)


def generate_assert_true(cmd):
    return 'self.assertTrue( %s )' % (
        generate_code_python_symantics(cmd.get_code()),)


def generate_assert_false(cmd):
    return 'self.assertFalse( %s )' % (
        generate_code_python_symantics(cmd.get_code()),)


def generate_assertExtended(cmd):
    return 'self.assertEqual( %s )' % (
        generate_code_python_symantics(re.sub("==", ",", cmd.get_code())))


def generate_assert_contain(cmd):
    return 'self.assertIn( """%s""", %s)' % (
        cmd.get_text(), generate_code_python_symantics(cmd.get_code()), )


def generate_code_python_symantics(cmd_code):
    return '%s' % (extract_variable_name(cmd_code),)


def extract_variable_name(var):
    return re.sub(r'#(\w+)', r'\g<1>', var)


def remove_assert_prefix(var):
    return re.sub(r'^\?=', '', var)


_REGEX_EXPLICIT_COMMAND = r'^c:(\S+?)[= ]'

_generators_commands = [
    {'re': _REGEX_EXPLICIT_COMMAND, 'generator': generator_for_explicit_commands},
    {'re': r'^#\w+$', 'generator': generate_set},
    {'re': r'^\?=', 'generator': generate_assert},
    {'re': r'==', 'generator': generate_assertExtended},
]

_generators_explicit_commands = {
    'assert-equals': generate_assert,
    'assert-true': generate_assert_true,
    'assert-false': generate_assert_false,
    'set': generate_set,
    'execute': lambda cmd: generate_code_python_symantics(cmd.get_code()),
    'assert-contain': generate_assert_contain,
}
