from pymongo import MongoClient
import json
import psycopg2
import os
import logging
from dotenv import load_dotenv

load_dotenv()
mongo_uri = os.getenv("MONGO_DB_CONNECTION")
uri = os.getenv("MONGO_DB_CONNECTION")
client = MongoClient(mongo_uri)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client.finbloom
members_collection = db["members_vamsik"]
transactions_collection = db["transactions_vamsik"]
   # Fetch all documents
x={'a':20,'b':30}
members = list(members_collection.find({}))
print(members)
for member in members:
     print(member)



  # Connect to PostgreSQL
conn = psycopg2.connect(
                dbname=os.getenv("dbname"), 
                user=os.getenv("user"),
                password=os.getenv("password"),
                host=os.getenv("host"),
                port=os.getenv("port"))
cur = conn.cursor()
print("Pinged your deployment. You successfully connected to PostgresDB!")
for membere in members:
  #  print(membere.get("fname"))
        member_id = membere["_id"]
        firstname = membere.get("first_name","nag")
        lastname = membere.get("last_name","talluri")
        gender= membere.get("gender","Male")
    #print(member_id,firstname,lastname,gender) 
        cur.execute(
        """INSERT INTO member ( first_name,last_name,gender)
        VALUES ( %s, %s, %s);""",
        ( firstname, lastname,gender))
conn.commit()
cur.close()
conn.close()
print("Data successfully inserted into PostgreSQL")
  # Commit and close connections
 
 