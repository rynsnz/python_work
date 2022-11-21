"""
loop new users to see if each username has already been used
"""

current_users = ['jandoe', 'jondoe', 'ryadoe', 'poedoe', 'admin']
new_users = ['JanDoe', 'JONDOE', 'ryan', 'erwin', 'poe']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'Sorry, {new_user} is unavilable.')
    else: print(f'{new_user} is available!')