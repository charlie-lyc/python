
# brilliant.org/cms

###########################################################################################

# python >>> python2.7
# python3 >>> python3.8

# which python
# /usr/bin/python
# which python3
# /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# type python
# python is /usr/bin/python
# type python3
# python3 is /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# echo $PATH
# /Library/Frameworks/Python.framework/Versions/3.8/bin:
# /usr/local/bin:
# /usr/bin:
# /bin:
# /usr/sbin:
# /sbin:
# /usr/local/share/dotnet:
# ~/.dotnet/tools:
# /Library/Apple/usr/bin:
# /Library/Frameworks/Mono.framework/Versions/Current/Commands

# /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# ls /Users/charlie/opt/anaconda3/bin/

# /Users/charlie/opt/anaconda3/bin/python3

###########################################################################################

# cd /Users/charlie
# (sudo) nano .bash_profile
# # Setting PATH for Python 3.8
# PATH="/Library/Frameworks/Python.framework/Versions/3.8/bin:${PATH}"
# export PATH

# (sudo) nano .bash_profile
# alias python=python3
# alias pip=pip3

# which python
# python: aliased to python3
# which python3
# /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# which pip
# pip: aliased to pip3
# which pip3
# /Library/Frameworks/Python.framework/Versions/3.8/bin/pip3

# type python
# python is an alias for python3
# type python3
# python3 is /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# type pip
# pip is an alias for pip3
# type pip3
# pip3 is /Library/Frameworks/Python.framework/Versions/3.8/bin/pip3

##########################################################################################

### ".bash_profile"에도 기록도 하고 "sudo"를 이용해 아래를 실행해봐도 영구히 설정되는 것은 아닌 것 같다.
### 터미널을 시작할 때마다 실행해야 한다. 영구히 설정 하는 방법이 따로 있는 건지 아니면 일시적으로 설정하는 게 맞는 건지...
# alias python=python3
# alias pip=pip3

# pip list

# python
# >>> import sys
# >>> sys.executable
# '/Library/Frameworks/Python.framework/Versions/3.8/bin/python3'

# pip install django

# pip show django

# python
# >>> import django
# >>> import sys
# >>> sys.executable
# '/Library/Frameworks/Python.framework/Versions/3.8/bin/python3'


