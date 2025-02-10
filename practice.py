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
