#
# pep8.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-pep8
# License: MIT
#

from SublimeLinter.lint import PythonLinter


class Pep8(PythonLinter):
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
