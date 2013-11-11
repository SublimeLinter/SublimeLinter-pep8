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
    executable = 'pep8'
    regex = r'^.+?:(?P<line>\d+):(?P<col>\d+): (?P<type>[EW])\d+ (?P<error>.+)'
    multiline = True
    comment_re = r'\s*#'
    defaults = {
        'select': [],
        'ignore': [],
        'max-line-length': None
    }

    def cmd(self):
        cmd = [self.executable]
        settings = self.get_view_settings()

        if 'max-line-length' not in settings:
            settings['max-line-length'] = self.settings.get('max-line-length')

        for option in self.defaults:
            value = settings.get(option)

            if isinstance(value, (list, tuple)):
                value = ','.join(value)

            if value:
                cmd.append('--{}={}'.format(option, value))

        cmd.append('-')
        return cmd

    def merge_inline_settings(self, view_settings, inline_settings):
        '''
        Merge inline settings with view settings.
        Allow 'select' and 'ignore' settings to use +/- to add or remove
        an error/warning from the list passed to pep8. If neither
        +/- is present, assume +.
        '''
        options = {}

        for name in ('select', 'ignore'):
            view_setting = view_settings.pop(name, [])
            inline_setting = inline_settings.pop(name, '')
            options[name] = self.override_options(view_setting, inline_setting)

        view_settings.update(options)

        # Update the view settings with any other inline settings
        view_settings.update(inline_settings)
        return view_settings
