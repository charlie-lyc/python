
### my_project % pipenv --rm

# Removing virtualenv (/Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm)…


### my_project % pipenv install

# Warning: the environment variable LANG is not set!
# We recommend setting this in ~/.profile (or equivalent) for proper expected behavior.
# Creating a virtualenv for this project…
# Pipfile: /Users/charlie/Documents/CoreySchafer_PythonTutorial/21_pipenv/my_project/Pipfile
# Using /Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 (3.8.3) to create virtualenv…
# ⠼ Creating virtual environment...created virtual environment CPython3.8.3.final.0-64 in 261ms
#   creator CPython3Posix(dest=/Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm, clear=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/charlie/Library/Application Support/virtualenv)
#     added seed packages: pip==20.1.1, setuptools==47.3.1, wheel==0.34.2
#   activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
# ✔ Successfully created virtual environment! 
# Virtualenv location: /Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm
# Installing dependencies from Pipfile.lock (7eee3f)…
#   🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:00
# To activate this project's virtualenv, run pipenv shell.
# Alternatively, run a command inside the virtualenv with pipenv run.


# 제일 처음에는 'pip install pipenv'를 실행하여 패키지를 설치 하였고,
# 일단 한번 설치된 'pipenv'는 지워져도 'Pipfile.lock'에 정보가 그대로 남아
# 다시 설치하기위해 'pipenv install'을 실행하게 되면
# "Installing dependencies from Pipfile.lock (7eee3f)… "
# 이런식으로 설치 된다.




