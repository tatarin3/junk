import sqlite3

database = sqlite3.connect("accounts.db", check_same_thread=False)


def _execute(command,params=(),commit=True):
	'''Smart cursor'''
	cur = database.cursor()
	cur.execute(command,params)
	data = [e1 for e1 in cur]
	if commit:
		database.commit()
	return data

def check_name_exists(username):
	'''check if name exists in database'''
	check_exists = _execute('SELECT * FROM accs WHERE (name=?)',(username,))
	if len(check_exists) == 0:
		return False
	else:
		return True


def create_user(username):
	'''creating user'''
	_execute('INSERT INTO accs(name) VALUES(?)',(username,))
	return

def get_user_password(username):
	'''get user password by address'''
	user_password = _execute('SELECT pass FROM accs WHERE (name = ?)',(username,))
	return user_password[0][0]


def set_user_password(username,password):
	'''set new user password'''
	_execute('UPDATE accs SET (pass = ?) WHERE (name = ?)',(password,username))
	return
