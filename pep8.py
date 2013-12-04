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

from SublimeLinter.lint import persist, PythonLinter


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
        """Run pep8 on code and return the output."""

        options = {
            'reporter': Report
        }

        type_map = {
            'select': [],
            'ignore': [],
            'max-line-length': 0,
            'max-complexity': 0
        }

        self.build_options(options, type_map, transform=lambda s: s.replace('-', '_'))

        if persist.settings.get('debug'):
            persist.printf('{} options: {}'.format(self.name, options))

        checker = self.module.StyleGuide(**options)

        return checker.input_file(
            filename=os.path.basename(filename),
            lines=code.splitlines(keepends=True)
        )
