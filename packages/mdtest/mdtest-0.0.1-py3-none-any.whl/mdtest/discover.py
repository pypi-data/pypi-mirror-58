import os
import logging


def discover_mdfiles():
    mdfiles = _get_markdown_files_in_dir("doc")
    _add_readme_if_exists(mdfiles)
    logging.info("Found markdown files:" + str(mdfiles))
    return mdfiles


def _get_markdown_files_in_dir(dir):
    mdfiles = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                mdfiles.append(os.path.join(root, file))
    return mdfiles


def _add_readme_if_exists(mdfiles):
    if os.path.isfile('README.md'):
        mdfiles.append('README.md')
