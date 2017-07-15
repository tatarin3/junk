import socialdb


def login_menu():
    '''Login menu'''
    print('You use socialBDwithSSbalance')
    username = ''
    while True:
        users_choise = input("Enter 'log' for login, or 'reg' for" +
                             " registration or 'exit' to exit the program : ")
        if users_choise.upper() == 'LOG':
            username = input('Enter login :')
            password = input('Enter password :')
            if (password != socialdb.get_password(username)):
                print('Wrong login or password')
            else:
                break
        elif users_choise.upper() == 'REG':
            username = socialdb.create_new_account()
            break
        elif users_choise.upper() == 'EXIT':
            raise SystemExit(1)
    print('Welcome, {}'.format(username))
    return username


def menu(username):
    '''Show users opportunitys and do what users want'''
    if 1 == socialdb.check_access(username):
        print('SuperUser access')
    else:
        print('Usual access')
    print('Enter 1 to see your profile')
    print('Enter 2 to change password')
    print('Enter 3 to change login')
    print('Enter 4 for sending SS')
    print('Enter 5 to exit the program')
    print('Enter 6 to delete your account')
    print('Enter 7 to change additional information')
    print('Enter 8 to see other user profile')
    print('Enter 9 to exit the profile')
    print('Enter 10 to send message')
    print('Enter 11 to send friendship request')
    print('Enter 12 to view all messages')
    print('Enter 13 to view all friends')
    print('Enter 723451 to extract one SS')
    if 1 == socialdb.check_access(username):
        print('Enter 666 to set SS to the user')
        print('Enter 333 to create a new account')
        print('Enter 111 to view all profiles')
        print('Enter 404 to delete a user account')
        print('Enter 999 to change user additional information')
        print('Enter 166617771 for the balances wipe')
        print('Enter 42 to add superuser access to the user')
    users_choise = int(input('==> '))
    if users_choise == 1:
        socialdb.show_user_info(username)
    elif users_choise == 2:
        socialdb.set_new_password(username)
    elif users_choise == 3:
        username = socialdb.set_new_login(username)
    elif users_choise == 4:
        socialdb.send_ss(username)
    elif users_choise == 5:
        raise SystemExit(1)
    elif users_choise == 6:
        socialdb.delete_account(username)
    elif users_choise == 7:
        socialdb.set_user_about(username)
    elif users_choise == 8:
        socialdb.show_other_info()
    elif users_choise == 9:
        return False
    elif users_choise == 10:
        socialdb.send_msg(username)
    elif users_choise == 11:
        socialdb.send_fr_req(username)
    elif users_choise == 12:
        socialdb.show_msg(username)
    elif users_choise == 13:
        socialdb.show_fr_req(username)
    elif users_choise == 666 and 1 == socialdb.check_access(username):
        socialdb.set_new_balance()
    elif users_choise == 333 and 1 == socialdb.check_access(username):
        socialdb.create_new_account(socialdb.check_access(username))
    elif users_choise == 111 and 1 == socialdb.check_access(username):
        socialdb.show_all_accounts()
    elif users_choise == 404 and 1 == socialdb.check_access(username):
        socialdb.delete_account(username, socialdb.check_access(username))
    elif users_choise == 999 and 1 == socialdb.check_access(username):
        socialdb.set_user_about(username, socialdb.check_access(username))
    elif users_choise == 166617771 and 1 == socialdb.check_access(username):
        socialdb.wipe_balances()
    elif users_choise == 42 and 1 == socialdb.check_access(username):
        socialdb.set_access()
    elif users_choise == 723451:
        socialdb.mine_ss(username)
    return True
