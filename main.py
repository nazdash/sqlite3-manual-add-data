# simple script to add a new custom row w/ hashed password to user database
# table user(email, name, password)
# https://docs.python.org/3/library/sqlite3.html
# https://www.sqlitetutorial.net/sqlite-python/insert/

import sqlite3
from werkzeug.security import generate_password_hash # func generating hash from string

database = r"application/database.db"
psw = r"admin"
pswh = generate_password_hash(psw, method="sha256")

con = sqlite3.connect(database) # establishing connection
cur = con.cursor() # creating Cursor object
sql = """ INSERT INTO user (email,first_name,password VALUES(?,?,?) """ # '?' passing a value
new_user = ("test@test.com", "test_name", pswh)

cur.execute(sql, new_user)
con.commit()

### as a function ###

def insert_user(email, name, password, database):
  pswh = generate_password_hash(password, method="sha256")
  con = sqlite3.connect(database)
  cur = con.cursor()
  sql = """ INSERT INTO user (email,first_name,password VALUES(?,?,?) """
  new_user = (email, name, pswh)
  cur.execute(sql, new_user)
  con.commit()
  return cur.lastrowid