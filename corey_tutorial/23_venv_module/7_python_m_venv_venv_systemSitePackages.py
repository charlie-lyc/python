
# my_project % rm -rf venv

### 내 파이썬 시스템(global Python)에 있는 모든 패키지(global Packages)를 가상환경에 설치.
# my_project % python -m venv venv --system-site-packages
# my_project % source venv/bin/activate

### 그런데 만약 필요한 패키지가 있어서 더 추가해서 설치할때
### 가상환경에서 설치하면 local Packages로 인식되므로
### 반드시 deactivate해서 global Python에도 설치할 것
# (venv) my_project % pip install Flask
# (venv) my_project % pip list --local

# (venv) my_project % deactivate
# my_project % pip install Flask


