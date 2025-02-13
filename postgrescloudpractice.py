import math
import os
import sys
import psycopg2
import members
print(members.greet("AITraining"))
from manage_tables import create_table
from members import create_member
from members import retrieve_members,update_member,delete_member
dbname = "neondb"
user = "neondb_owner"
password = "npg_hKLaOPy9vs2l"
host = "ep-blue-sky-a4haw4w1-pooler.us-east-1.aws.neon.tech"
port = "5432"

connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
print("Connected to PostgreSQL successfully!")
#version printing
cursor = connection.cursor()
cursor.execute("SELECT version();")
print("PostgreSQL version:", cursor.fetchone())

#closing connection
"""cursor.close()
connection.close()
print("Database connection closed.")"""

#Creating tables
#create_table(connection = connection, table_name="members")
#create_table( table_name="members", connection = connection)
#create_table(connection, "accounts")

#inserting data
first_name = "Vamsi"
last_name = "Karumanchi"
gender = "M"
create_member(connection, first_name, last_name, gender)

#selecting records
retrieve_members(connection)

#update
update_member(connection, 8, "Nag", "Talluri")
#Delete
delete_member(connection,14)


def fetch(connection):
   cursor= connection.cursor()
   cursor.execute("select * FROM members")
   rows=cursor.fetchall()
   cursor.close()
   return rows
data=fetch(connection)
for row in data:
      print(row)