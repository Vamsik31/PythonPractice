import psycopg2
import os
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

class Member:

    member_serial_number = 0
    

    def __init__(self, email, fname=None, lname=None,  age=None, address=None, salary=None,phone_number=None,ssn=None):
        self.id = 0
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone_number = phone_number
        self.join_date = datetime.now().date()
        self.age = age
        self.address = address
        self.salary = salary
        self.__ssn = ssn
        if self.age<18:
            raise ValueError("age must be 18 or older")
        else:
            self.age = age
            
        self.connection = psycopg2.connect(
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )


    
    def create_new_member(self):
        cursor= self.connection.cursor()
        query = "INSERT INTO members (first_name ,age ,address ,salary ,join_date ,last_name ,email,phone_number ,ssn  ) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s) RETURNING id"
        cursor.execute(query, (self.first_name, self.age, self.address, self.salary, self.join_date, self.last_name, self.email, self.phone_number, self.__ssn))
        self.connection.commit()
  
        result = cursor.fetchone()
      
        if result:
            self.id= result[0]
            return f"id of inserted row {self.id}"
        else:
            raise Exception("Failed to retrieve the inserted row ID")

        #save member to database

        #raise exception if email already exists

        return f"id of inserted row{self.id}"
    
email =input("Enter email:")
first_name =input("Enter first_name:")
last_name =input("Enter last_name:")
while True:
    try:
        age = int(input("Enter age: "))
        if age < 18:
            print("age must be 18 or older. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid age.")

address =input("Enter address:")
salary =int(input("Enter salary:"))
phone =input("Enter phone:")
ssn =input("Enter ssn:")


memuber =Member(email,first_name,last_name,age,address,salary,phone,ssn)
memuber.create_new_member()