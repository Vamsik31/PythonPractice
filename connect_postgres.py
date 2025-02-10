import math
import os
import sys
import psycopg2
from manage_tables import create_table
dbname = "postgres"
user = "postgres"
password = "Account@3107"
host = "localhost"
port = "5432"

connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
print("Connected to PostgreSQL successfully!")
create_table(connection=connection,table_name="members")
create_table(connection,"accounts")
print("Tables created successfully!")

first_name = input("Enter first name of the member")
last_name = input("Enter last name of the member")
gender = input("ENter gender of the member")


