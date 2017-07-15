import sqlite3

database = sqlite3.connect('accounts.db')


def _execute(command, params=(), commit=True):
    '''Smart cursor'''
    cur = database.cursor()
    cur.execute(command, params)
    data = [e1 for e1 in cur]
    if commit:
        database.commit()
    return data


def create_msgandfl(username):
    _execute('CREATE TABLE {} (id integer NOT NULL,status integer NOT NULL DEFAULT 1)'.format(
        username + 'fl'))
    _execute('CREATE TABLE {} (id_user integer NOT NULL, name varchar(255) NOT NULL, mes_text varchar(255) NOT NULL)'.format(
        username + "msg"))


def wipe_balances():
    '''Set all balances in database 0'''
    _execute('UPDATE balance SET balance=?', (0,))
    print('You made balances wipe')


def mine_ss(username):
    '''This function will add 1 to users balance'''
    balance = get_user_balance(username) + 1
    _execute('UPDATE balance SET balance=? WHERE user_id=?',
             ((balance), (get_user_id(username))))
    print('Your balance {}'.format(balance))


def show_all_accounts():
    '''Print all information about accounts and their balances'''
    sha = _execute\
        ('SELECT id,name,pass,balance FROM users ' +
         'LEFT JOIN balance ON (users.id=balance.user_id)')

    for i in range(0, len(sha)):
        for j in range(0, len(sha[i])):
            print(sha[i][j], end=' ')
        print('\n')
    return


def send_msg(username):
    userg = input('Enter the recipient : ')
    if check_user_exist(userg) == 0:
        print('This user not exists')
        return
    msg_txt = input('Enter your message : ')
    _execute('INSERT INTO {} (id_user,name,mes_text) VALUES(?,?,?)'.format(userg + 'msg'),
             (get_user_id(username), username, msg_txt))
    print('Message sent successfully')


def send_fr_req(username):
    userg = input('Enter login : ')
    if check_user_exist(userg) == 0:
        print('This user not exists')
        return
    check_status = _execute('SELECT status FROM {} WHERE id=?'.format(
        username + 'fl'), (get_user_id(userg),))
    if len(check_status) == 0:
        g_check_status = _execute(
            'SELECT status FROM {} WHERE id=?'.format(userg + 'fl'), (get_user_id(username),))
        if len(g_check_status) == 0:
            _execute('INSERT INTO {} (id) VALUES(?)'.format(userg + 'fl'), (get_user_id(username),))
            print('Friend add request added')
            return
        elif g_check_status[0][0] == 1:
            print('You have already applied for friendship')
            return
    elif check_status[0][0] == 1:
        _execute("UPDATE {} SET id=(?),status=(?)".format(userg + "fl"), (get_user_id(username), 2))
        print('You are friends now')
        return
    elif check_status[0][0] == 2:
        print('You are already friends')
        return


def show_fr_req(username):
    frreq = _execute('SELECT * FROM ?', (username + 'fl',))
    if frreq == 0:
        print('You dont have any friendship requests')
        return
    for i in range(0, len(frreq)):
        for j in range(0, len(frreq[i])):
            print(frreq[i][j])
        print('\n')
    return


def show_msg(username):
    messages = _execute('SELECT * FROM ?', (username + 'msg',))
    if messages == 0:
        print('You dont have messages')
        return
    for i in range(0, len(messages)):
        for j in range(0, len(messages[i])):
            print(messages[i][j])
        print('\n')
    return


def create_new_account(supera=0):
    '''Insert in database information about new account'''
    username = input('Enter desired login : ')
    if check_user_exist(username) == 1:
        print('This user already exists')
    else:
        need_su = _execute('SELECT count(id) FROM users')
        password = input('Enter desired password: ')
        _execute('INSERT INTO users(name,pass) VALUES(?,?)',
                 (username, password))
        create_msgandfl(username)
        if need_su[0][0] == 0:
            _execute('UPDATE users SET super=1')
            print('Superuser access get')
        if supera == 0:
            print('Your account was successfully created')
            return username
        else:
            print('You was successfully created additional account')
            return


def get_password(username):
    '''Get users password'''
    password = _execute('SELECT pass FROM users WHERE name=?', (username,))
    if len(password) == 0:
        return 0
    else:
        return password[0][0]


def check_access(username):
    '''Check users admin access'''
    supera = _execute('SELECT super FROM users WHERE name=?', (username,))
    if len(supera) == 0:
        return 0
    else:
        return supera[0][0]


def get_user_id(username):
    '''Get users id '''
    user_id = _execute('SELECT id FROM users WHERE name=?', (username,))
    if len(user_id) == 0:
        return 0
    else:
        return user_id[0][0]


def get_user_balance(username):
    '''Get users balance'''
    balance = _execute(
        'SELECT balance FROM balance WHERE user_id=?', (get_user_id(username),))
    if len(balance) == 0:
        return 0
    else:
        print(balance[0][0])
        return balance[0][0]


def show_user_info(username):
    '''Show users information'''
    balance = get_user_balance(username)
    user_id = get_user_id(username)
    about = get_user_about(username)
    print('Name {}, ID {}, Balance {}, Additional information {}'
          .format(username, user_id, balance, about))


def show_other_info():
    '''Show other users information'''
    username = input('Enter login wich profile you want to see : ')
    if check_user_exist(username) == 1:
        show_user_info(username)
    else:
        print('This user not exists')


def check_user_exist(username):
    '''Check if user exists in database'''
    password = _execute('SELECT pass FROM users WHERE name=?', (username,))
    if len(password) == 0:
        return 0
    else:
        return 1


def set_new_password(username):
    '''Set new password for user'''
    password = input('Enter new password : ')
    _execute('UPDATE users SET pass=? WHERE name=?', ((password), (username)))
    print('You successfully changed password.')


def set_new_login(username):
    '''Set new login for user'''
    login = input('Enter new login : ')
    if check_user_exist(login) == 0:
        _execute('UPDATE users SET name=? WHERE name=?', ((login), (username)))
        print('You successfully changed login')
        return login
    else:
        print('This user already exists')
        return username


def set_user_about(username, supera=0):
    '''Set field about for user'''
    if supera == 0:
        set_about = input('Enter information about yourself : ')
        _execute('UPDATE users SET about=? WHERE name=?',
                 (set_about, username))
        print('Information was successfully added')
    else:
        username = input('Enter name wich additional information' +
                         'you want to change : ')
        if check_user_exist(username) == 1:
            set_about = input('Enter information : ')
            _execute('UPDATE users SET about=? WHERE name=?',
                     (set_about, username))
            print('Information was successfully added')
        else:
            print('This user not exists')


def set_access():
    '''Add admin access for user'''
    username = input('Enter users login wich you want to add access : ')
    if check_user_exist(username) == 1:
        _execute('UPDATE users SET super=? WHERE name=?', (1, username))
        print('Access successfully added')
    else:
        print('This user not exists')


def get_user_about(username):
    '''Get users about'''
    about = _execute('SELECT about FROM users WHERE name=?', (username,))
    return about[0][0]


def send_ss(username):
    '''Send ss to other user'''
    userg = input("Enter recipient's login : ")
    if check_user_exist(userg) == 0:
        print('This user not exists')
    else:
        howm = int(input('How much do you want to transfer : '))
        balance = get_user_balance(username)
        if howm <= balance:
            balance = balance - howm
            balplus = get_user_balance(userg) + howm
            _execute('UPDATE balance SET balance=? WHERE user_id=?',
                     ((balance), (get_user_id(username))))
            _execute('UPDATE balance SET balance=? WHERE user_id=?',
                     ((balplus), (get_user_id(userg))))
            print('You successfully transferred SS')
        else:
            print('You do not have enough SS')


def delete_account(username, supera=0):
    '''Delete account from database'''
    if supera == 0:
        uver = input('Are you sure you want to delete account?(Y)')
        if uver == 'Y':
            _execute('DELETE FROM users WHERE name=?', (username,))
            print('Your account has been deleted')
            raise SystemExit(1)

    else:
        username = input('Enter users login wich you want to delete : ')
        if check_user_exist(username) == 1:
            uver = input('Are you sure you want to delete this account?(Y)')
            if uver == 'Y':
                _execute('DELETE FROM users WHERE name=?', (username,))
                print('{} accaunt has been deleted'.format(username))
                return
        else:
            print('This user not exists')


def set_new_balance():
    '''Set balance for a user'''
    username = input('Enter the name of the user you want' +
                     ' to set up a balance : ')
    if check_user_exist(username) == 1:
        balance = int(input('Enter a balance for this user'))
        _execute('UPDATE balance SET balance=? WHERE user_id=?',
                 ((balance), (get_user_id(username))))
        print('User {} have {} on his balance'
              .format(username, balance))
    else:
        print('This user not exists')
