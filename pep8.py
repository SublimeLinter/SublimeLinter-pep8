#
# pep8.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
#
# Project: https://github.com/SublimeLinter/SublimeLinter-contrib-pep8
# License: MIT
#

from SublimeLinter.lint import Linter


class Pep8(Linter):
    language = 'python'
    cmd = ('pep8', '*', '-')
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?P<type>[EW])\d+ (?P<error>.+)'
    multiline = True
    defaults = {
        '--select=': [],
        '--ignore=': [],
        '--max-line-length=': None
    }
    comment_re = r'\s*#'
    inline_settings = 'max-line-length'
    inline_overrides = ('select', 'ignore')
