# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:57:52 2021

Corey Schafer - Classes and OOP - 6 Videos
https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

@author: Skywalker
"""

#%% Vid 1 - Employee Class

class Employee:
    pass            #Use class iy you want to define attrs and methods later
    
emp_1 = Employee()
emp_2 = Employee()

print(emp_1) # See the memory address
print(emp_2)

emp_1.first = 'Jyoti'
emp_1.last = 'Mohapatra'
emp_1.email = 'jyotiranjan@live.com'
emp_1.pay = 5000

emp_2.first = 'John'
emp_2.last = 'Skywalker'
emp_2.email = 'j.skywalker@gmail.com'
emp_2.pay = 9000

print(emp_1.email)
print(emp_2.email)


#%% Init method

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))


emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)

print(emp_1.email)
print(emp_2.email)

#Basic way
print('{} {}'.format(emp_1.first, emp_1.last))

#Print using a method
print(emp_1.fullname())
print(emp_2.fullname())

#Print using a method and class name
print(Employee.fullname(emp_1))



#%% Vid 2 - Class Variables
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay * Employee.raise_amount) # Same use

emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)


# An attribute is searched on the instance first
# If not found, then it will search the Class for the attribute
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(Employee.__dict__)

# Update attr at Class
print('Update attr at Class')
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Update attr at Instance
print('Update attr at Instance')
emp_1.raise_amount = 1.09
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)
print(Employee.__dict__)

# Number of instances for a class
print(Employee.num_of_emps)


#%% Vid 3 - Regular methods, Class Methods and Static Methods
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #self.pay = int(self.pay * Employee.raise_amount) # Same use
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day): # Do not need either cls or self
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        

emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Set Raise
print('# Set Raise')
Employee.set_raise_amt(1.08)    # Use class method. 
                                # It can also be run from instance
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Parse a String and use values to create an object
print('# Parse a String and use values to create an object')
emp_str_1 = 'John-Doe-11000'
emp_str_2 = 'Steve-Smith-12000'
emp_str_3 = 'Jane-Frings-13000'

# Normal Way
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.__dict__)

# Create and use a constructor to do this job
print('# Create and use a constructor to do this job')
new_emp_11 = Employee.from_string(emp_str_1)
new_emp_12 = Employee.from_string(emp_str_2)
new_emp_13 = Employee.from_string(emp_str_3)
print(new_emp_11.__dict__)
print(new_emp_12.__dict__)
print(new_emp_13.__dict__)

# Static Method - is_workday
print('## Static Method - is_workday')
import datetime
my_date = datetime.date(2020, 4, 9)

print(Employee.is_workday(my_date))



#%% Vid 4 - Inheritance

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amt = 1.10


emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)

print(emp_1.raise_amount)
print(emp_2.raise_amount)

dev_1 = Employee('Jyoti','Mohapatra', 5000 )
dev_2 = Employee('John','Skywalker', 9000)
print(dev_2.raise_amount)
print(dev_2.raise_amount)

print('print(help(Developer - and Check the details of child class')
print(help(Developer))

print('# Use subclass raise amount to give raise')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


#%% Inheritance - 2

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)           # Choice 1 - better  
        #Employee.__init__(self, first, last, pay)   # Choice 2 - works
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())                         


dev_1 = Developer('Jyoti','Mohapatra', 5000 , 'Java')
dev_2 = Developer('John','Skywalker', 9000, 'Python')

print(dev_1.email)
print(dev_1.prog_lang)


mgr_1 = Manager('Marcus', 'Wienert', 90000, [dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)

mgr_1.print_emps()




#%% Inheritance - 3

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)           # Choice 1 - better  
        #Employee.__init__(self, first, last, pay)   # Choice 2 - works
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())                         


dev_1 = Developer('Jyoti','Mohapatra', 5000 , 'Java')
dev_2 = Developer('John','Skywalker', 9000, 'Python')

mgr_1 = Manager('Marcus', 'Wienert', 90000, [dev_1])

print('# print(isinstance)')
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print('# print(issubclass)')      
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))      

# Sample study material - exception.py
# HTTPException class inherits from Exception parent class
# BadRequest class -(code 400)- inherits from HTTPException Class

#%% Vid 5 - Special (Magic/Dunder) Methods
### https://www.youtube.com/watch?v=3ohzBxoFHAY
### REFERENCE Python docs
### https://docs.python.org/3/reference/datamodel.html#special-method-names

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # This method will change the object printing from type 1 to type 2 below
    # <__main__.Employee object at 0x0000017C41CAD7C0>
    # Employee('Jyoti', 'Mohapatra', '5000')        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
 
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
    
# just an example of + operator working based on the params
print(1 + 2)
print('a' + 'b')


emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)
print(emp_1)

print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1 + emp_2) # Becasue of dunder add method, gives combined salary

print('# __Dunder test method')
print(len('test'))
print(len(emp_1))



#%% Vid 6 - Property Decorators - Getters, Setters, and Deleters

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Move email attribute to a Property Decorator method
        #self.email = first + '.' + last + '@company.com'
           
    @property
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    @property
    def email(self): #all methods in a class need an instance 'self'
        return ('{}.{}@newemail.com'.format(self.first, self.last))

emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)




#%% Property Decorators - Getters, Setters, and Deleters

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Move email attribute to a Property Decorator method
        #self.email = first + '.' + last + '@company.com'
           
    @property
    def fullname(self): #all methods in a class need an instance 'self'
        return ('{} {}'.format(self.first, self.last))
    
    @property
    def email(self): #all methods in a class need an instance 'self'
        return ('{}.{}@newemail.com'.format(self.first, self.last))

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!!')
        self.first = None
        self.last = None

emp_1 = Employee('Jyoti','Mohapatra', 5000 )
emp_2 = Employee('John','Skywalker', 9000)

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


emp_3 = Employee('Jane','Sheperd', 11000)
print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)

emp_3.fullname = 'Sarah Frings'
print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)

del emp_3.fullname
print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)


#%% 

#%% 

#%% 

