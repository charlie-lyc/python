import os


print(os.getcwd())
os.chdir('/Users/charlie/Documents/CoreySchafer_PythonTutorial')
print(os.getcwd())
print()

print(">>>>>>>>>>>>>>>>>>>>>>>> About 'os.path' <<<<<<<<<<<<<<<<<<<<<<<<")
print()
print(os.path)
# <module 'posixpath' from '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/posixpath.py'>
print()
print(dir(os.path))
print()
print(help(os.path))
print()

print(">>>>>>>>>>>>>>>>>>>>>>>> About 'os.environ' <<<<<<<<<<<<<<<<<<<<<<<<")
print()
print(os.environ)
# environ({
#	'OLDPWD': '/Applications/Sublime Text.app/Contents/MacOS', 
#	'HOME': '/Users/charlie', 
#   'LOGNAME': 'charlie', 
#   'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.HyVSF4XUAl/Listeners', 
#	'SHELL': '/bin/zsh', 
#	'__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 
#	'XPC_SERVICE_NAME': '0', 
#	'PATH': '/Library/Frameworks/Python.framework/Versions/3.8/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/share/dotnet:~/.dotnet/tools:/Library/Apple/usr/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands',
#   'TMPDIR': '/var/folders/rg/65f998kx2jdg7l7p6cg8d2540000gn/T/', 
#	'XPC_FLAGS': '0x0', 
#	'USER': 'charlie', 
#	'LC_CTYPE': 'UTF-8'
# })
print()
print(dir(os.environ))
print()
print(help(os.environ))
print()
print(os.environ.get('HOME'))
print()


# Real example
file_path = os.path.join(os.environ.get('HOME'),
			'Documents/CoreySchafer_PythonTutorial/test.txt')
string = '\nHello world\n'
with open(file_path, 'a') as f:
    f.write(string)
f.close()


# Right path join
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)


# Wrong path join
file_path = os.environ.get('HOME') + 'test.txt'
print(file_path)



