import sqlite3

def login():


	username = raw_input("Please enter your username")
	password = raw_input("Please enter you password")

	with sqlite3.connect("user.db") as db:
		cursor = db.cursor()
	
	check_user_pass = ("SELECT * FROM USERS WHERE name = ? AND password = ?")
	cursor.execute(check_user_pass,[(username),(password)])

	results = cursor.fetchall()

	if results:
		for i in results:
			print "Welcome "+str(i[0])
			break

	else:
		print "Username or password incorrect"

if __name__ == '__main__':
	login()
