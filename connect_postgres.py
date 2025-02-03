import psycopg2

# Database connection details
dbname = "mloans"
user = "postgres"
password = "Account@3107"
host = "localhost"
port = "5432"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(dbname='mloans', user='postgres', password='Account@3107', host='localhost', port='5432')
    print("Connected to PostgreSQL successfully!")
    
    # Close connection
    conn.close()
except Exception as e:
    print("Error connecting to PostgreSQL:", e)
