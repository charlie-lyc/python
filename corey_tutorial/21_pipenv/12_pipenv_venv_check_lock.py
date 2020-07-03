### my_project % pipenv --venv

# /Users/charlie/.local/share/virtualenvs/my_project-D_84u7rm


### my_project % pipenv check

# Checking PEP 508 requirements…
# Passed!
# Checking installed package safety…
# All good!

# 만약 위와 같이 메시지가 나오지 않는다면 다시 한번더 재설치하고 체크 권장

### my_project % pipenv install
### my_project % pipenv check


### my_project % pipenv graph

# Django==2.1
#   - pytz [required: Any, installed: 2018.5]
# django-crispy-forms==1.7.2
# Pillow==7.2.0


### my_project % pipenv lock

# Locking [dev-packages] dependencies…
# Building requirements...
# Resolving dependencies...
# ✔ Success! 
# Locking [packages] dependencies…
# Building requirements...
# Resolving dependencies...
# ✔ Success! 
# Updated Pipfile.lock (7eee3f)!