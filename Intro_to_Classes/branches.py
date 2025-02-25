import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
class branch:
    #class variable
    number_of_branches = 0
    
    
    def __init__(self, bid, bname, baddr, bphone):
        #instance variable
        self.branch_id = bid
        self.branch_name = bname
        self.address = baddr
        self.phone = bphone

        self.connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )
     #cursor =  connection.cursor()


    def create_branch(self):

        #get a connection
        #connection = pyscopg2.connect()
        #get a cursor
        #cursor = connection.cursor()
        
        cursor = self.connection.cursor()
        #run the insert query
        query = "INSERT INTO branches (branch_name, bran_address, bran_phone) VALUES (%s, %s, %s)"
        #query = f"insert into branches values (?, ?, ?)".format(self.branch_name, self.address, self.phone)
        try:
            cursor.execute(query, (self.branch_name, self.address, self.phone))
            self.connection.commit()
            return "New Branch is created  successfully!"
        except Exception as e:
            self.connection.rollback()
            print("Error:", e)
            return "Can't create a new Branch As it is already created successfully!"
        finally:
           cursor.close()

bid= input("Enter id:")
bname =input("Enter branchname:")
baddr =input("Enter address:")
bphone =input("Enter phoneno:")

branches =branch(id,bname,baddr,bphone)
branches.create_branch()