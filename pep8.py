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

import os

try:
    from pep8 import StandardReport
except ImportError:
    StandardReport = None

from SublimeLinter.lint import PythonLinter


if StandardReport is not None:

    class Report(StandardReport):

        """Provides a report in the form of a single multiline string, without printing."""

        def get_file_results(self):
            """Collect and return the results for this file."""
            self._deferred_print.sort()
            results = ''

            for line_number, offset, code, text, doc in self._deferred_print:
                results += '{path}:{row}:{col}: {code} {text}\n'.format_map({
                    'path': self.filename,
                    'row': self.line_offset + line_number,
                    'col': offset + 1,
                    'code': code,
                    'text': text
                })

            return results


class PEP8(PythonLinter):

    """Provides an interface to the pep8 python module/script."""

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
    module = 'pep8'

    def check(self, code, filename):
        """Run pep8.Checker on code and return the output."""

        view_settings = self.get_view_settings()

        kwargs = {
            'select': view_settings.get('select', '').split(','),
            'ignore': view_settings.get('ignore', '').split(','),
            'max_line_length': view_settings.get('max-line-length'),
            'reporter': Report
        }

        checker = self.module.StyleGuide(**kwargs)

        return checker.input_file(
            filename=os.path.basename(filename),
            lines=code.splitlines(keepends=True)
        )
