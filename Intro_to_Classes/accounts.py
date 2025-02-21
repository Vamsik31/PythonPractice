from members import Member
import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
#member count is global variable,
member_count = 20

class BaseAccount:
    def __init__(self, id, crtd_dt, mem_id, bal,Acct_type):
        self.id = id
        self.created_date = crtd_dt
        self.member_id = mem_id
        self.member = None
        self.balance = bal
        self.account_type=Acct_type
        self.connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
        def add_money_to_account(self, amount):
            cursor =self.connection.cursor()
            query = "INSERT INTO accounts (Acct_type,crtd_dt, mem_id,bal) VALUES (%s ,%s ,%s ,%s)"
            cursor.execute(query, (self.Acct_type, self.crtd_dt, self.mem_id, self.bal))
        self.connection.commit()
    
        return True
    