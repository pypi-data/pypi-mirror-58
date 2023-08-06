import subprocess
import logging


def run_shell(comand_line):
    comand_line = ' '.join(comand_line.split())
    completed_process = subprocess.run(comand_line,
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT)
    if completed_process.returncode != 0:
        raise ValueError('Process "%s" unsuccessful\nDetail output:\n%s' % (
            comand_line, completed_process.stdout))
    out = completed_process.stdout.decode("utf-8")
    logging.debug('fixture_cli: run_shell("%s") returned: %s' %
                  (comand_line, out))
    return out
