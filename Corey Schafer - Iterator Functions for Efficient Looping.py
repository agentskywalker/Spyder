# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:54:38 2021

Corey Schafer - Iterator Functions for Efficient Looping
https://www.youtube.com/watch?v=Qu3dThVy6KQ

1 Video - 45 mins

@author: Skywalker
"""


#%% Itertools Module - Iterator Functions for Efficient Looping

import itertools

counter = itertools.count()

data = [100, 200, 300, 400, 500]

daily_data = list(zip(itertools.count(), data))

print(daily_data)


print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# Infinite loop
# for num in counter:
#     print(num)



#%% 

import itertools

counter = itertools.count(start=5, step=5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.count(start=5, step=-2.5)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#%% 
import itertools

counter = itertools.count()

data = [100, 200, 300, 400, 500]

# Print ONLY needed range of values
daily_data = list(zip(range(10), data))
print(daily_data)

# Print all the range of values
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)


#%% cycle function - cycle through the given values
# use case, Switch turning On and OFF

import itertools

counter = itertools.cycle([1, 2, 3])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.cycle(['ON', 'OFF'])

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))



#%% repeat function

import itertools

counter = itertools.repeat(2, times=3)

print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))
# print(next(counter))

#%% map and starmap function

import itertools
 
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))


squares = itertools.starmap(pow, [(5,2), (1,2), (2,2)])
print(list(squares))


#%% combinations and permutations - No duplicates

import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

print('# Combitions')
result = itertools.combinations(letters, 2)
for item in result:
    print(item)

print('# Permutations')
result = itertools.permutations(letters, 2)

for item in result:
    print(item)


#%% Create all 4 digit values

import itertools

numbers = [0, 1, 2, 3]

print('# Cartesian Product')
result = itertools.product(numbers, repeat = 4)

for item in result:
    print(item)


print('# Combinations with repeat')
result = itertools.combinations_with_replacement(numbers, 4)

for item in result:
    print(item)


#%% chain function - loop through all the lists 1 by 1

import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

print('# Chain function')
combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)


#%% islice function - loop through list until upper index is reached

import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

print('# islice function')
result= itertools.islice(range(10), 5)
for item in result:
    print(item)

print('# islice function - with start and stop index')
result= itertools.islice(range(10), 1, 5)
for item in result:
    print(item)    

print('# islice function - with start and stop index - step through')
result= itertools.islice(range(10), 1, 5, 2)
for item in result:
    print(item)      

#%% Read a file

import itertools

#os.listdir()

#with open('C:\Users\Skywalker\Spyder\test.log', 'r') as f: # This didn't work
#with open(r'test.log') as f:                               # this didn't works
with open(r'C:\Users\Skywalker\Spyder\test.log') as f:      # this works
    header = itertools.islice(f, 3) # read first 3 lines
    
    for line in header:
        print(line, end = '')
    

#%% compress function - select  values form list based on True or False
import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

result = itertools.compress(letters, selectors)
    
for item in result:
    print(item)


#%% compress function and filter
import itertools

def lt_2(n):
    if n<2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

selectors = [True, True, False, True]

print('# filter function - using custom method')    
result = filter(lt_2, numbers)
    
for item in result:
    print(item)
    
print('# itertools.filterfalse')    
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)    

print('# itertools.dropwhile')    
result = itertools.dropwhile(lt_2, numbers)
for item in result:
    print(item)    

print('# itertools.takewhile')    
result = itertools.takewhile(lt_2, numbers)
for item in result:
    print(item)    

#%% accumulate funciton

import itertools
import operator

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

print('# accumulate function')    
result = itertools.accumulate(numbers)
    
for item in result:
    print(item)

print('# accumulate function using multiply operator')    
result = itertools.accumulate(numbers, operator.mul)
    
for item in result:
    print(item)
    

#%% group by function - It needs the values to be sorted :(
#   tee function to yopy an iterator

import itertools

def get_state(person):
    return person['state']

# list of dictionaries
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

print('# groupby function 1') 
# Once grouped, can be traversed only once :(
person_group = itertools.groupby(people, get_state)

# Make copies
# Do NOT use the original iterator after you copy using tee function
copy1, copy2 = itertools.tee(person_group)

#for key, group in person_group:
for key, group in copy1:    
    print(key, group)
    for person in group:
        print(person)
    print()

print('# groupby function 2')    
# Group again, if you want to traverse again :(
# person_group = itertools.groupby(people, get_state)

#for key, group in person_group:
for key, group in copy2:    
    print(key, len(list(group)))


#%% 

#%% 

#%% 



#%% 

#%% 

#%% 

#%% 


#%% 

#%% 

#%% 

#%% 


#%% 

#%% 

#%% 

#%% 




