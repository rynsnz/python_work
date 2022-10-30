requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f'{"mushrooms" in requested_toppings}')

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')
