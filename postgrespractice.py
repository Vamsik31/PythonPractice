#2.3 Creating a Cursor Object and Executing Queries
#Once connected, a cursor object is used to execute SQL queries:

cursor = connection.cursor()
cursor.execute("SELECT version();")
print("PostgreSQL version:", cursor.fetchone())