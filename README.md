SublimeLinter-pep8
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-pep8.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-pep8)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [pep8](https://github.com/jcrocholl/pep8). It will be used with files that have the “Python” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before installing this plugin, you must ensure that `pep8` is installed on your system. To install `pep8`, do the following:

1. For best performance, install [Python 3](http://python.org) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `pep8` by typing the following in a terminal, replacing '3.x' with the available version of pip:
   ```
   [sudo] pip-3.x install pep8
   ```

**Note:** This plugin requires `pep8` 1.4.6 or later.

### Linter configuration
In order for `pep8` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `pep8` is installed and configured, you can proceed to install the SublimeLinter-pep8 plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `pep8`. Among the entries you should see `SublimeLinter-pep8`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-pep8 provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline](http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings).

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|ignore|A comma-separated list of error codes to ignore| |&#10003;|
|select|A comma-separated list of error codes to select, overrides ignore| |&#10003;|
|max-line-length|The maximum allowed line length. `null` uses the PEP8 default of 79.|&#10003;| |

### Implementing per-project settings
Typically you will want to configure pep8 on a per-project basis to conform to the coding style for all files in that project. Usually you want to ignore certain pep8 warnings. First you need to find the pep8 error codes from the [pep8 documentation](http://pep8.readthedocs.org/en/latest/intro.html#error-codes). Then you need to configure the pep8 linter to ignore those warnings.

For example, let’s say your project requires python 2.7+, you want the maximum line length to be 512, and you want to ignore warnings about visual indents (pep8 errors E127 and E128):

* If you have not already created a project in Sublime Text, select `Project -> Save Project As...`.

* Select `Project -> Edit Project`.

* At the **top** level of the project’s JSON data, add the following:

        "SublimeLinter":
        {
            "@python": 2.7,
            "linters":
            {
                "pep8":
                {
                    "@disable": false,
                    "ignore": "E127,E128",
                    "max-line-length": 512
                }
            }
        }

* Save the file.

Any time you edit the project and change a linter’s settings, all open files that use that linter will be re-linted to reflect the new settings.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
