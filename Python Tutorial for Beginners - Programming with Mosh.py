# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:20:02 2021

@author: Skywalker

Programming with Mosh - https://www.youtube.com/watch?v=kqtD5dpn9C8
Python Tutorial for Beginners - Learn Python in 1 Hour

"""
#%% Hello World
print("Hello World")

#%% Assignment and Print
age = 20
age = 30
price = 19.95
first_name = 'Jyoti'
is_online = False
print(age, price, first_name, is_online)


#%% How to receive input from user
name = input("What is your name? ")
print("Hello " + name)


#%% 3 types of data in Python - Type conversion
birth_year = input("Enter yout birth year : ")
age = 2021 - int(birth_year)
print("Your age is " + str(age))



#%% Condition statement
x = 5
y = 10
if x == y:
	print("equal")
elif x > y:
	print("greater")
else:
   	print("smaller")


#%% Functions

def fact(n):
    if n == 1:
       return n
    else:
       return n * fact(n - 1)

print(fact(5))

#%% for loop
for i in range(0, 10):
    print(i)


#%% while loop
n = 10
while n > 0: 
    if n == 5:
        break
    else:
        print(n)
        n = n - 1

#%% Inheritance
class Parent():
    def fun1(self):
        print('This is function 1')
        
class Child(Parent):
    def fun2(self):
        print('This is function 2')        
        
ob = Child()
ob.fun1()
ob.fun2()


#%% main()

print("First module's name: {}".format(__name__))


#%% main  usage 2
def main():
    print("Inside method main")
    pass

if __name__ == '__main__':
    main()


#%% Calculator
first = float(input("First : "))
second = float(input("Second : "))
sum = first + second
print("\n\nSum is : " + str(sum))

#%% String Methods
course = 'Python for Beginners'
print(course.upper())
print(course)
print(course.find('y'))
print(course.find('for'))
print(course.replace('for', '4'))
print('Python' in course)


#%% Arithmatic operations
print(10+3)
print(10/3)
print(10//3)
print(10%3)

x = 10
x = x+3
print(x)
x+=3
print(x)

# Operator Precedence
# () parenthesis
# *,/
# +,-


#%% Comparison operators

x = 3 > 2
print(x)

x = 3 == 2
print(x)

x = 3 != 2
print(x)

# >, >=, <, <=, ==, !=

#%% Logical operators
# and, or, not

#%% Conditional Statement
# if elif
# Python uses indentation to represent a block of code
temp = 12
if temp > 30:
    print("It's a hot day")
elif temp > 20:             # temp between 20 and 30
    print("It's a nice day")
elif temp > 10:             # temp between 10 and 20
    print("It's a cool day")
else:
    print('It\'s a cold day')
print('DONE')

#%% Weight convertor program
weight = float(input("Please enter Weight : "))
unit = input("K(g) or (L)bs : ")
if unit.upper() == 'K':
    #converted = weight / 0.45
    converted = weight * 2.205
    print("Weight in Lbs : " + str(converted))
else:
    #converted = weight * 0.45
    converted = weight / 2.205
    print("Weight in Kgs : " + str(converted))

#%% While Loop 1
i = 1
while i <= 1_000: # 1_000 is same as writing 1000. 
                  # Makes it better readable
    print(i)
    i = i+1


#%% While Loop2
i = 1
while i <= 10: 
    print(i * '*') # This allows the string to be multiplied
    i = i+1


#%% For Loop
numbers = [1, 2, 3, 4, 5, 6, 7]
for item in numbers:
    print(item)

#%% Lists
names = ['Jyoti', 'Ranjan', 'Mohapatra']
print(names)
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])

names[2] = 'Skywalker'
print(names)

print(names[0:1])
print(names[0:2])
print(names[0:3])

print('Jyoti' in names)
print(len(names))
      
      
#%% List Methods
names.append('Gamer')
print(names)

names.insert(0, 'Mr.')
print(names)

names.remove('Gamer')
print(names)

names.clear()
print(names)
      
      
      
#%% range function
#default use 1
print('default use 1')
nums = range(5)
print(nums)

for num in nums:
    print(num)

#default use 2
print('default use 2')
for num in range(8):
    print(num)

# Usage mid range
print('Usage mid range')
nums2 = range(5, 20)
print(nums2)

for num2 in nums2:
    print(num2)
    
# Usage skipping range    
print('Usage skipping range')    
nums3 = range(5, 20, 2)
print(nums3)

for num3 in nums3:
    print(num3)

#%% Tuples - immutable
numbers = (1, 2, 3, 4, 5, 5)
print(numbers.count(5))

print(numbers.index(2))

















