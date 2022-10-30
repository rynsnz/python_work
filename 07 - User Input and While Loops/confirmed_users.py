# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more confirmed users.
#  Move each verified user into the list of confirmed users.

# This while loop will run as long as the unconfirmed_users list is not empty
while unconfirmed_users:
    # use pop method to remove users one at a time from the end of the list
    # candace, then brian, and ending with alice
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())