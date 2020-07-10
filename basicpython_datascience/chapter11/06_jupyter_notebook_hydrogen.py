import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

#######################################################################

# "Jupyter" 설치하고 "Notebook" 실행하여 웹상에서 결과 보기
# - Jupyter : Python Shell을 웹환경에서 구현하여 만든 일종의 IDE
# - 즉, 나의 가상환경 조건을 그대로 가지고 웹상에서 파일, 모듈, 패키지등을 실행해 볼 수 있다.
# (venv) % pip install jupyter
# (venv) % sudo python -m jupyter ipykernel install
# (venv) % jupyter notebook
# 가상환경에서 쥬피터 노트북을 실행하여 실제 파일을 실행하면 확장자 '.ipynb'의 임시파일 생성.

# 이러한 쥬피터 노트북의 기능을 적용한 것이 Atom의 "Hydrogen" 패키지이다.

# Atom에서 "Hydrogen" 설치하고 실행하여 결과 보기
# - Shift + Enter : 한줄 실행하고 다음줄로 커서 이동
# - Shift + Option + Enter : 모두 실행하고 다음으로 커서 이동
# - Command + Enter : 한줄 실행
# - Command + Control + Enter : 모두 실행
