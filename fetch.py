import sqlite3

conn = sqlite3.connect("user.db")
cursor = conn.cursor()

username_input = raw_input("Please enter username")
password_input = raw_input("Please enter password")

print "Entered username ",username_input
print "Entered password ",password_input

def print_gretings():
	print "User Found"

def print_invalid():
	pass
query = """SELECT * FROM USERS"""

cursor.execute(query)
for username,password in cursor.fetchall():
	print "Database Username ",username
	print "Database password ",password
	if username_input == username and password_input == password:
		print_gretings()
		break
	else:
		print_invalid()

