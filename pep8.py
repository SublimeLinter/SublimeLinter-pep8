#
# pep8.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-pep8
# License: MIT
#

"""This module exports the PEP8 plugin linter class."""

from SublimeLinter.lint import PythonLinter


class PEP8(PythonLinter):

    """Provides an interface to the pep8 python script."""

    language = 'python'
    cmd = ('pep8@python', '*', '-')
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>E)|(?P<warning>W))\d+ (?P<message>.+)'
    multiline = True
    defaults = {
        '--select=,': "",
        '--ignore=,': "",
        '--max-line-length=': None
    }
    inline_settings = 'max-line-length'
    inline_overrides = ('select', 'ignore')
