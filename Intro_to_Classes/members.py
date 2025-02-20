import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Member:
    member_serial_number = 0

    def __init__(self, email, fname=None, lname=None, age=None, address=None, salary=None):
        self.id = None
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.phone_number = None
        self.age = age
        self.address = address
        self.salary = salary
        self.__ssn = None
        self.__created_at = datetime.now()

        

        try:
            self.connection = psycopg2.connect(
                dbname=os.getenv("dbname"),
                user=os.getenv("user"),
                password=os.getenv("password"),
                host=os.getenv("host"),
                port=os.getenv("port")
            )
        except psycopg2.Error as e:
            print(f"Database connection failed: {e}")
            self.connection = None

    def __del__(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

"""# Example usage
try:
    new_member = Member(email="test@example.com", age=20)
    print("Member created successfully!")
except ValueError as e:
    print(f"Error: {e}")"""

