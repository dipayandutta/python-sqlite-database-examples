import sqlite3

conn = sqlite3.connect("user.db")
cursor = conn.cursor()

username = "employee"
password = "abcd"

query = """INSERT INTO USERS (name,password) VALUES ('employee','abcd') """

output = cursor.execute(query)

conn.commit()
print output
