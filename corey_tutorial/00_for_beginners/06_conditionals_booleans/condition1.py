user = 'Admin'
logged_in = True
# logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
print()


if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
print()


if not logged_in:
    print('Please log in')
else:
    print('Welcome')



# and
# or
# not
