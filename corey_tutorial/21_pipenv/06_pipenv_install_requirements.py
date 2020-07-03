
### my_project % pipenv install -r ../snippets/requirements.txt

# Requirements file provided! Importing into Pipfile…
# Installing dependencies from Pipfile.lock (b6dc94)…
#   🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
# To activate this project's virtualenv, run pipenv shell.
# Alternatively, run a command inside the virtualenv with pipenv run.


# 계속 "ERROR: Couldn't install package: pillow" 메시지가 발생되어
# 구글링해 보니 파이썬 3.8버전에 필로우 5.2버전이 지원되지 않는다고 하여
# "requirements.txt" 파일의  "Pillow==5.2.0"를 "Pillow==7.2.0"으로 수정하여 해결

# Check 'Pipfile' file
# We can see 4 packages added from 'requirements.txt' file in [packages]


