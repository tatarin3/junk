import sqlite3


database = sqlite3.connect("acc.db")


def _execute(command, params=(), commit=True):
	'''Smart cursor'''
	cur = database.cursor()
	cur.execute(command, params)
	data = [e1 for e1 in cur]
	if commit:
		database.commit()
	return data

def get_bases():
	bases = _execute("SELECT name FROM base")
	print(bases)
	return bases

def get_id(base):
	name = base[2:-3]
	vid = _execute("SELECT id FROM base WHERE name=?",(name,))
	return vid[0][0]

def get_that_accs(base):
	vid = get_id(base)
	accs = _execute("SELECT login FROM accounst WHERE base_id=?",(vid,))
	print(accs)
	return accs

def get_that_password(base,login):
	print(login)
	vid = get_id(base)
	password = _execute("SELECT password FROM accounst WHERE base_id=? AND login=?",(vid,login))
	return password
