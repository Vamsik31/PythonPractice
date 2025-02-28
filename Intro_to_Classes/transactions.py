import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


class Transaction:

    def __init__(self, transac_type, transac_date, acct_id, balance):
        self.type = transac_type
        self.transac_date = transac_date if transac_date else datetime.now().date()
        self.account_id = acct_id
        self.balance = balance  # Use lowercase for consistency


        self.connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
    def add_transactions(self):
        cursor =self.connection.cursor()
        query = "INSERT INTO transactions (type,transac_date,account_id ,balance) VALUES (%s ,%s ,%s ,%s)"
        cursor.execute(query, (self.type, self.transac_date, self.account_id,self.balance))
        self.connection.commit()
        cursor.close()
    
        return True
    
   

#id= input("Enter id:")
Acct_type =input("Enter Acct_type:")
transac_date =input("Enter transac_date:")
account_id =input("Enter account_id:")
balance =input("Enter balance:")

accounts =Transaction(Acct_type,transac_date,account_id,balance)
accounts.add_transactions()


#Transaction( 3, 1000, "savings").add_transactions(100)s