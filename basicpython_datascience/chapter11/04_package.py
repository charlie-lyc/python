# Package : 하나의 대형 프로젝트를 만드는 코드의 묶음
# 다양한 모듈들의 합, 폴더로 연결됨
# __init__, __main__ 등 키워드 파일명이 사용됨
# 다양한 오픈 소스들이 모두 패키지로 관리됨

# 패키지 만들기
#
# 1) 기능들을 세부적으로 나눠 폴더로 만듦
# - game/
# - game/graphic/
# - game/play/
# - game/sound/
#
# 2) 각폴더별로 필요한 모듈을 구현함 : 패키지가 구성되어 실제로 구동이 되는지 알아보는 과정
# - 'touch [file]'명령을 통해 아래의 각 파일들을 간단하게 만든다.
# - game/
#        __init__.py
#         graphic/
#               __init__.py
#               render.py
#               screen.py
#         play/
#               __init__.py
#               run.py
#               test.py
#         sound/
#               __init__.py
#               echo.py
#               wav.py
#
# graphic/render.py
# def render_test():
#     print('render')
#
# sound/echo.py
# def echo_test():
#     print('echo')
#
# 3) 1차 Test - python shell : game/의 바로 상위 디렉토리에서 "python shell 실행""
# charlie@Charlie-MacBookPro chapter11 % "python"
# Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from game.sound.echo import echo_test
# >>> echo_test()
# echo
# >>> from game.graphic import render
# >>> from game.graphic import render as rd
# >>> rd.render_test()
# render
# >>>
#
# 4) 폴더별로 __init__.py 만들기
# - 현재 폴더가 패키지임을 알리는 초가화 스크립트
# - 없을 경우 패키지로 간주하지 않음(다만 3.3버전 이후로는 사용하지 않는다. 하위 호환성을 위해서는 사용)
# - 하위 폴더와 .py파일(모듈)을 모두 포함
# - import와 '__all__' 키워드 사용
#
# 5) __main__.py 만들기 : game/디렉토리에 위치 - "패키지를 실행""하기 위해 반드시 필요
# - 작성 후 실제 실행해 보면
# charlie@Charlie-MacBookPro game % "python game"
# render
# echo
#
# 6) 2차 Test - python shell : __init__.py와 __main__.py를 모두 작성 후
# charlie@Charlie-MacBookPro chapter11 % python
# Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
# [Clang 6.0 (clang-600.0.57)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from game.graphic.render import render_test
# >>> render_test()
# render
# >>> from game.sound.echo import echo_test
# >>> echo_test()
# echo
# >>>

# Package namespace : 패키지 내에서 다른 폴더의 모듈을 호출할 때 상대 참조로 호출
# 1) 절대 경로 참조
#  from game.graphic import render
#  render.render_test()
#
#  from game.graphic.render import render_test
#  render_test()
#
# 2) 상대 경로(현재 디렉토리 : 해당 파일이 있는 디렉토리) 기준
#  from . import render
#  render.render_test()
#
#  from .render import render_test
#  render_test()
#
# 3) 상대 경로(부모 디렉토리) 기준
#  from ..sound import echo
#  echo.echo_test()
#
#  from ..sound.echo import echo_test
#  echo_test()
#
