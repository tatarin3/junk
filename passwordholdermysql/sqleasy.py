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
	return bases

def get_id(base):
	print(base)
	name = str(base)
	print(name)
	vid = _execute("SELECT id FROM base WHERE name=?",(name,))
	print(vid)
	return vid

def get_that_accs(base):
	vid = get_id(base)
	accs = _execute("SELECT login FROM accounst WHERE base_id=?",(vid[0],))
	return accs

def get_that_password(base,login):
	vid = get_id(base)
	password = _execute("SELECT password FROM accounst WHERE base_id=? AND login=?",(vid,login))
	return password
