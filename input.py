import pyodide_js
import sqlite3
import re
conn = sqlite3.connect('customer.db')
cur = conn.cursor()
first_name = input("enter your first name ")
while not re.match("[A-Za-z]+", first_name):
    print("Only letters are allowed")
    first_name = input("enter your first name ")
last_name = input("enter your last name ")
while not re.match("[A-Za-z]+", last_name):
    print("Only letters are allowed")
    last_name = input("enter your last name ")
email = input ("enter your email name ")
while not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
  print("invalid email")
  email = input("enter your email ")
cur.execute(f"""
INSERT INTO customer (
  first_name,
  last_name,
  email
)

VALUES (
    '{first_name}',
    '{last_name}',
    '{email}'
)
""")
conn.commit()

conn.close()


