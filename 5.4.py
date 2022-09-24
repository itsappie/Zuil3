def new_password():
    x = input('Old Password: ')
    y = input('New Password: ')

    if x == y:
        print('Invalid new Password!')
    elif len(y) >= 6:
        print('Valid new Password!')
    elif len(y) < 6:
        print('Invalid new Password!')


new_password()
