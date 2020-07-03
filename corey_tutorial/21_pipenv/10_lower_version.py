
# Correct 'Pipfile' by lower version(3.7) of python and...

### my_project % pipenv --python 3.7 

# Virtualenv already exists!
# Removing existing virtualenv…
# Warning: the environment variable LANG is not set!
# We recommend setting this in ~/.profile (or equivalent) for proper expected behavior.
# Creating a virtualenv for this project…
# Pipfile: /Users/charlie/Documents/CoreySchafer_PythonTutorial/21_pipenv/my_project/Pipfile
# Using /usr/bin/python3 (3.7.3) to create virtualenv…
# ⠹ Creating virtual environment...created virtual environment CPython3.7.3.final.0-64 in 846ms
#   creator CPython3macOsFramework(dest=/Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm, clear=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/charlie/Library/Application Support/virtualenv)
#     added seed packages: pip==20.1.1, setuptools==47.3.1, wheel==0.34.2
#   activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
# ✔ Successfully created virtual environment! 
# Virtualenv location: /Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm


### my_project % pipenv run python

# Python 3.7.3 (default, Apr 24 2020, 18:51:23) 
# [Clang 11.0.3 (clang-1103.0.32.62)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import sys
# >>> sys.executable
# '/Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm/bin/python'
# >>> exit()


# Correct again 'Pipfile' by lower version(3.8) of python and...

### my_project % pipenv --python 3.8

# Virtualenv already exists!
# Removing existing virtualenv…
# Warning: the environment variable LANG is not set!
# We recommend setting this in ~/.profile (or equivalent) for proper expected behavior.
# Creating a virtualenv for this project…

### my_project % pipenv run python

# Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>>




