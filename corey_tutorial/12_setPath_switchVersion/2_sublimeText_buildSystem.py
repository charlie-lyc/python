import sys
print(sys.version)
print(sys.executable)

# [ command + b ]
# 3.7.4 (default, Aug 13 2019, 15:17:50)
# [Clang 4.0.1 (tags/RELEASE_401/final)]
# /Users/charlie/opt/anaconda3/bin/python

#######################################################################################

# Sublime text -> Tools -> Build System -> New Build System
# {
#   "cmd": ["/usr/bin/python", "-u", "$file"],
#   "file_regex": "^[ ]*file \"(...*?)\", line ([0-9]*)",
#   "quiet": true
# }
# save "Python 2.7"

# Sublime text -> Tools -> Build System -> sellect "Python 2.7"
# [ command + b ]
# 2.7.16 (default, Apr 17 2020, 18:29:03)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc-
# /System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python


# Sublime text -> Tools -> Build System -> New Build System
# {
# 	"cmd": ["/Library/Frameworks/Python.framework/Versions/3.8/bin/python3",  "-u", "$file"],
# 	"file_regex": "^[ ]*file \"(...*?)\", line ([0-9]*)",
# 	"quiet": true
# }
# save "Python 3.8"

# Sublime text -> Tools -> Build System -> sellect "Python 3.8"
# [ command + b ]
# 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
# [Clang 6.0 (clang-600.0.57)]
# /Library/Frameworks/Python.framework/Versions/3.8/bin/python3

#######################################################################################

### *** finding "User" folder where to save Build System file : Sublime text -> Preferences -> Browse Packages


