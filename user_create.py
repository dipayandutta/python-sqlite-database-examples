import sqlite3

def newUser():
	found = 0
	while found == 0:
		username = raw_input("Please Enter a username")
		password = raw_input("Please enter a password")

		with sqlite3.connect("user.db") as db:
			cursor = db.cursor()

		findUser = ("SELECT * FROM USERS WHERE name = ?")
		cursor.execute(findUser,[(username)])

		if cursor.fetchall():
			print "User name already Exists"

		else:
			found = 1
	
	insertData = '''INSERT INTO USERS(name,password) values (?,?) '''
	cursor.execute(insertData,[(username),(password)])
	db.commit()

if __name__ == '__main__':
	newUser()
