import sqlite3

database = sqlite3.connect("chatserver.db", check_same_thread=False)


def _execute(command,params=(),commit=True):
	'''Smart cursor'''
	cur = database.cursor()
	cur.execute(command,params)
	data = [e1 for e1 in cur]
	if commit:
		database.commit()
	return data


def server_get(data,address):
	'''base work chat'''
    if check_address_exists(address):
    	if get_user_status(address) == 0:
    		if get_user_password(address) == '0':
    			set_user_password(address,data)
    			set_user_status(address,1)
    			answer = 'Welcome ' + get_user_name(address) +  '\n'
				print('user {} login as {}'.format(address,get_user_name(address)))
    			return answer
    		else:
    			if get_user_password(address) == data:
    				set_user_status(address,1)
    				answer = 'Welcome ' + get_user_name(address) +  '\n'
					print('user {} login as {}'.format(address,get_user_name(address)))
    				return answer
    			else:
    				delete_address_from_user(address)
					print('user {} enter wrong password'.format(address))
    				return 'Wrong password\n'
    	else:
    		message = str(get_user_name(address) + ': ' + data)
			print('user {} wich login as {} send message {}'.format(address,get_user_name(address),message))
    		return message
    else:
    	if ((data == 'log') or (data == 'reg')):
    		return 'Enter your nickname\n'
    	else:
    		if check_name_exists(data):
    			if check_name_address(data):
    				set_user_address(address,data)
					print('user {} try login as {}'.format(address,get_user_name(address)))
    				return 'Enter your password\n'
    			else:
					print('user {} try login as {}'.format(address,get_user_name(address)))
    				return 'Somebody already use this profile\n'
    		else:
    			create_user(address,data)
				print('user {} create account {}'.format(address,get_user_name(address)))
    			return 'Enter your new password\n'



def check_login_status(address):
	'''checking login status (does not using)'''
	if check_address_exists(address) and get_user_status(address) == 1:
		return True
	else:
		return False


def check_address_exists(address):
	'''check if address exists in database'''
	check_exists = _execute('SELECT name FROM users WHERE useraddr=?',(address,))
	if len(check_exists) == 0:
		return False
	else:
		return True


def check_name_exists(username):
	'''check if name exists in database'''
	check_exists = _execute('SELECT pass FROM users WHERE name=?',(username,))
	if len(check_exists) == 0:
		return False
	else:
		return True


def check_name_address(username):
	'''check if name have already address in database'''
	user_address = _execute('SELECT useraddr FROM users WHERE name = ?',(username,))
	if user_address[0][0] == ' ':
		return True
	else:
		return False


def create_user(address,username):
	'''creating user'''
	_execute('INSERT INTO users(name,useraddr) VALUES(?,?)',(username,address))
	return


def get_user_name(address):
	'''get user name by address'''
	user_name = _execute('SELECT name FROM users WHERE useraddr = ?',(address,))
	return user_name[0][0]


def get_user_status(address):
	'''get user status by address'''
	user_status = _execute('SELECT status FROM users WHERE useraddr = ?',(address,))
	return user_status[0][0]


def get_user_password(address):
	'''get user password by address'''
	user_password = _execute('SELECT pass FROM users WHERE useraddr = ?',(address,))
	return user_password[0][0]


def set_user_password(address,password):
	'''set new user password'''
	_execute('UPDATE users SET pass = ? WHERE useraddr = ?',(password,address))
	return


def set_user_status(address,status):
	'''set user status'''
	_execute('UPDATE users SET status = ? WHERE useraddr = ?',(status,address))
	return


def set_user_address(address,username):
	'''set user address'''
	_execute('UPDATE users SET useraddr = ? WHERE name = ?',(address,username))
	return


def delete_address_from_user(address):
	'''deleting user address'''
	_execute("UPDATE users SET useraddr = ' ' WHERE useraddr = ?",(address,))
	return
