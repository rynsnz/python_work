"""
make a list of five or more usernames to include 'admin'
print a generic message for all users except admin
print unique message for admin
catch if username list is empty
"""
usernames = ['jandoe', 'jondoe', 'ryadoe', 'poedoe', 'admin']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello admin, would you like to see a status report?')
        else: print(f'Hello {username}, thank you for logging in again.')
else: print('We need to find some users!')