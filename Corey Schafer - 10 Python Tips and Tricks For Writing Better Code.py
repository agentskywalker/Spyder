# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:53:08 2021

Corey Schafer - 10 Python Tips and Tricks For Writing Better Code
https://www.youtube.com/watch?v=C-gEQdGVXbk

@author: Skywalker
"""


#%%  Ternary conditions

#Normal style
condition = True
if condition:
    x = 1
else:
    x = 0
print(x)    

# Alternate style
x = 5 if condition else 6
print(x)    

    
#%% Use underscore as separators for better Readability
num1 = 1_000_000_000
num2 = 100_000
total = num1 + num2
print(total)

print(f'{total:,}') #format output number with commas

#%% Use context managers to manage resources
# saves trouble of managing/closing the resource manually

with open('test.txt', 'r') as f:
    file_contents = f.read()
    
words = file_contents.split(' ')
word_count = len(words)
print(word_count)


#%% Use enumerate function to keep track of index in a List
# Traditional way - not clean
names = ['Corey', 'Chris', 'Dave', 'Travis']
index = 0
for name in names:
    print(index, name)
    index += 1
        
# Alternate way - Clean
print('Alternate way - Clean - Start with 0')    
for index, name in enumerate(names):
    print(index, name)

print('Alternate way - Clean - Start with 1')        
for index, name in enumerate(names, start=1):
    print(index, name)    

#%% Enumerate example alternate - Zip function
# Old way - Enumerate
print('Old way - Enumerate')
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')  

#New way - Zip function
print('New way - Zip function 111111111')
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')  

#New way - Zip function
print('New way - Zip function 222222222')
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')  

print('New way - Zip function 333333333')    
for value in zip(names, heroes, universes):
    print(value)      

#%% Unpacking
print('Unpacking 1')
a, _ = (1, 2)   # Use underscore when a variable is not being used
print(a)
#print(b)

print('Unpacking 2')
a, b, *c = (1, 2, 3, 4, 5) 
print(a)
print(b)
print(c)


print('Unpacking 3')
a, b, *_ = (1, 2, 3, 4, 5) 
print(a)
print(b)
#print(c)


print('Unpacking 4')
a, b, *c, d = (1, 2, 3, 4, 5) 
print(a)
print(b)
print(c)
print(d)

#%% Class - Setting attribute value dynamically 1
class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Jyoti'

setattr(person, 'first', 'Sky')     #Set attribute
print(person.first)

setattr(person, first_key, first_val)
print(person.first)    
print(getattr(person, first_key))   #Get attribute



#%% Class - Setting attribute value dynamically 2
class Person():
    pass

person = Person()

person_info = {'first': 'Jyoti', 'last': 'Ranjan'}

for key, value in person_info.items():
    setattr(person, key, value)
print(person.first)    
print(person.last)    

for key in person_info.keys():
    print(getattr(person, key))   #Get attribute

#%%


#%%


#%%



#%%


#%%