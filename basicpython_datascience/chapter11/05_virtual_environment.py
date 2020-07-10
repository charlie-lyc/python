# 두개의 프로젝트 예를 들어 "웹"과 ""데이터 분석"을 동시에 진행하게 된다면
# 각각에 해당되는 패키지 구성을 어떻게 것인가가 관건이다.
# 왜냐하면 나중에 프로젝트를 배포하게 될 경우 필요한 패키지 구성을
# 정확하게 작성해 두는 것이 반드시 필요하기 때문이다.

# Virtual Environment : 위와 같은 상황에 대응하기 위해 "가상환경"이 필요하다.
# - 프로젝트 진행 시 필요한 패키지만 설치하는 환경
# - 기본 인터프리터 + 프로젝트 종류별 패키지 설치
# - 다양한 패키지 관리도구를 사용

# 가상환경 도구
# - virtualenv : 가장 대표적인 가상환경 관리도구, 다수의 레퍼런스 + 패키지(pip) 제공
# - conda : 상용 가상환경 도구, miniconda 기본도구, 설치의 용이성, Windows에서 장점

# Windows : 원하는 디렉토리로 이동해서 "가상환경 폴더 설치"
# conda create -n my_project python=3.4 (설치)
# activate my_project                   (활성화)
# deactivate                            (비활성)

#####################################################################

# Mac OS : 원하는 디렉토리로 이동해서 "가상환경 폴더 설치"
# python -m venv project_env
# which python                    (원래 작동되는 파이썬 시스템 경로 확인)
# source project_env/bin/activate (활성화)
# (project_env) % which python    (활성화 이후 파이썬 시스템 경로 확인)
# (project_env) % deactivate      (비활성화)

# 개발하고 있는 "프로젝트 내에 가상환경 폴더 설치"
# mkdir my_project                      (프로젝트 폴더 만들기)
# python -m venv my_project/venv        (프로젝트 내에 가싱환경 설치)
# source my_project/venv/bin/activate   (활성화)
# (venv) % deactivate                   (비활성화)

# 가상환경 내 설치된 모든 팩키지 보기
# (venv) % pip list
# 목록파일 생성시 포함되는 패키지 보기
# (venv) % pip freeze
# 가상환경 내에서 이것 저것 팩키지를 설치하여 작업을 실시한 후 배포하기 위한 목록파일 만들기
# (venv) % pip freeze > pip freeze > requirements.txt
# 만들어진 목록파일 내용 보기
# cat requirements.txt
# 만들어진 목록파일 그대로 다른 가상환경에서 다시 설치하기
# pip install -r requirements.txt

#######################################################################
# 외부 패키지 설치하기

# Python 패키지 : 수많은 패키지 제공, MacOS, Linux
# pip install [패키지]
# pip install matplotlib

# Miniconda 패키지 : 높은 Windows 호환
# conda install [패키지]
# conda install matplotlib


# Example of Virtulal Environment
# Matplotlib : 대표적인 파이썬 그래프 관리 패키지
# - 엑셀과 같은 그래프들을 화면에 표시
# - 다양한 데이터 분석 도구들과 함께 사용

# (venv) % pip list
# Package    Version
# ---------- -------
# pip        19.2.3
# setuptools 41.2.0
# (venv) % pip install --upgrade pip
# (venv) % pip list
# Package    Version
# ---------- -------
# pip        20.1.1
# setuptools 41.2.0
# (venv) % pip install matplotlib
# (venv) % pip list
# Package         Version
# --------------- -------
# cycler          0.10.0
# kiwisolver      1.2.0
# matplotlib      3.2.2
# numpy           1.19.0
# pip             20.1.1
# pyparsing       2.4.7
# python-dateutil 2.8.1
# setuptools      41.2.0
# six             1.15.0
