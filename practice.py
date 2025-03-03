#print('hi')
#print(2 ** 2 ** 3)
#print(2*3)
#print(9%6%2)
#print(-4-4)
#print(-4+8)
#print('Hello, Vamsi')
#a=[1,2,3]
#b=a
#a=[4,5,6]
#a=True
#if a:
 #   print('It is True')
  #  print('Also Print This')
 #print('Always print this')   
#a= [1,2,3,4,5]
#for number in a:
#print(number)
#4 in a

#02-07-2025
#numbers=[1,2,3,4,5]
#print(numbers)

numbers=[1,"python",3.14,True]
print(numbers)

numbers=[10,20,30,40,50]
print(numbers[0])

numbers=[10,20,30,40,50]
print(numbers[-1])

numbers[1]=25
print(numbers)

numbers.append(60)
print(numbers)

numbers.insert(2,35)
print(numbers)

numbers.remove(30)
print(numbers)

del numbers[1]
print(numbers)

subset=numbers[1:4]
print(subset)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
squares=[x**2 for x in range(10)]
print(squares)
evens=[x for x in range (10) if x%2==0]
print(evens)

person={"name":"vamsi","age":"28","city":"sterling"}
print(person)

print(person["name"])
print(person.get("age"))

person["profession"]="engineer"
print(person)

del person["profession"]
print(person)

#person.clear()
print(person)

print(person.keys())
print(person.values())

print(person)
# Indentation -Indentation refers to the spaces at the beginning of a code line.
if 5>2:
    print('Five is greater than Two')

#Comments can be used to explain Python code.
#Comments can be used to make the code more readable.
#Comments can be used to prevent execution when testing code   

#This is a comment for singlr line of code
print("Hello, World!")

#Multiline comment denoted inbetween double quotes in 3 times

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting---If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.
#String variables can be declared either by using single or double quotes:
#Variable names are case-sensitive
x=5
y='John'
print(type(x))
print(type(y))

"""A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""
#Example   -----Remember that variable names are case-sensitive-------
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Mu='10'
print(Mu)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables
"""Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside."""
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#-----Create a variable inside a function, with the same name as the global variable----
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

"""Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""

#Examples:-
#x = "Hello World"--str	
#x = 20	--int	
#x = 20.5--float	
#x = 1j	--complex	
#x = ["apple", "banana", "cherry"]--	list	
#x = ("apple", "banana", "cherry")--	tuple	
#x = range(6)--	range	
#x = {"name" : "John", "age" : 36}--dict	
#x = {"apple", "banana", "cherry"}--set	
#x = frozenset({"apple", "banana", "cherry"})--	frozenset	
#x = True--	bool	
#x = b"Hello"--	bytes	
#x = bytearray(5)	--bytearray	
#x = memoryview(bytes(5))--	memoryview	
#x = None	--NoneType	

#Python Arithmetic Operators---Arithmetic operators are used with numeric values to perform common mathematical operations:


#  + --	Addition:-	x + y	
#  - --Subtraction;-	x - y	
# *	--Multiplication;-	x * y	
# /	--Division;- x / y	
# %	--Modulus;-	x % y	
# ** --Exponentiation;-	x ** y	
# // --Floor division;-	x // y


thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#--------------------------
  fruits=['apple','banana','cherry','pineapple','mango','berry']
  newlist=[]
  for x in fruits:
     if 'a' in  x:
        newlist.append(x)

        print(newlist)
#--------------------------------------------------

#Classes

