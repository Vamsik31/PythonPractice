import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
#member count is global variable,
member_count = 20

class BaseAccount:
    def __init__(self, id,bal,acct_type , mem_id,crtd_dt):
        self.id = id
        self.created_date = crtd_dt
        self.member_id = mem_id
        self.balance = bal
        self.account_type=acct_type
        self.connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
    def add_money_to_account(self):
            print(self.id,float(self.balance),self.account_type,int(self.member_id),datetime.now().date())
            cursor =self.connection.cursor()
            query = "INSERT INTO accounts (id,balance,account_type,member_id,created_date) VALUES (%s ,%s ,%s ,%s,%s)"
            cursor.execute(query, (self.id,self.balance,self.account_type,self.member_id,datetime.now().date()))
            self.connection.commit()
            self.connection.close()
    
       
id= input("Enter id:")
Acct_type =input("Enter Acct_type:")
crtd_dt =input("Enter Crtd_Dt:")
mem_id =input("Enter Mem_Id:")
bal =input("Enter balance:")

accounts =BaseAccount(id,bal,Acct_type,mem_id,crtd_dt)
accounts.add_money_to_account()