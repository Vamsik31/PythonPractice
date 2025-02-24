import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


def create_branch(branch_name, bran_address, bran_phone):

    connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
    print('Connected to DB Succesfully')
    #get a cursor
    cursor = connection.cursor()
    #run the insert query
    query = "INSERT INTO accounts (branch_name, bran_address, bran_phone) VALUES (%s ,%s ,%s)"
    cursor.execute(query, ())
    connection.commit()
    connection.close()
   

def update_branch(branch_name, bran_address):
            #get a connection
        connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
        print('Connected to DB Succesfully')
    #get a cursor
        cursor = connection.cursor()
    #run the insert query
        query = "UPDATE branches SET bran_phone = %s WHERE branch_name = %s"
        cursor.execute(query, (bran_address,branch_name))
        connection.commit()
        print("Branch updated successfully")
        cursor.execute(query)
        cursor.commit()

        #create_branch('Ashburn', '44322 Russel Branch pkwy,20148', '9912813826')
        #update_branch('Ashburn', '44322 Russel Branch pkwy,20148', '9705448183')