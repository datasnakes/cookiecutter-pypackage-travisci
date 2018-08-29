# -*- coding: utf-8 -*-
import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{cookiecutter.python_package_name}}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python project/module name. Please do not use a - and use _ instead.' % module_name)

    # Exit to cancel project creation
    sys.exit(1)
