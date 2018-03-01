import sqlite3

conn = sqlite3.connect("user.db")
if conn:
	print "Connected!"
else:
	print "Unable to connect!"

