#######apis.py##############
import requests
response = requests.get('https://api.github.com/users/python')
data=response.json()
print(data) 


##########calculator.py#############
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(add(30,20))
print(sub(200,10))  


###########decorator.py###########
# def login(func):
#    def wrapper():
#         print("checking login")
#         func()
#         return wrapper
#         @login
#         def dashboard():
#              print("Dashboard login")
#              dashboard()

def message(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper
@message
def hello():
    print("hello python")
    print("hello django")
    print("hello friend")
hello()


###########inheritence.py#############
# ############single inheritance
# class father:
#     def house(self):
#         print("father has a house")
# class son(father): #inheritance
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.bike()

# ###########multi level inheritance
# class grandfather:
#     def house(self):
#         print("grandfather has a house")
# class father(grandfather):
#     def car(self):
#         print("father has a car")
# class son(father):
#     def bike(self):
#         print("son has a bike")
# s=son()
# s.house()
# s.car()
# s.bike()

# # class thatta:
#     def land(self):
#         print("thatta's land")
# class appa(thatta):
#     def house(self):
#         print("appa's house")
# class maga(appa):
#     def bike(self):
#         print("maga's bike")
# obj=maga()
# obj.house()
# obj.land()
# obj.bike()

# # ####multiple inheritance
# class father:
#     def house(self):
#         print("father has a house")
# class mother:
#     def car(self):
#         print("mother has a car")
# class child(father,mother):
#     def bike(self):
#         print("child has a bike")
# obj=child()
# obj.house()
# obj.car()
# obj.bike()

#################hierarchical inheritance
class father:
    def house(self):
        print("father has a house")
class son(father):
    def bike(self):
        print("son has a bike")
class daughter(father):
    def doll(self):
        print("daughter has a doll")
obj1=son()
obj1.house()
obj1.bike()
obj2=daughter()
obj2.house()
obj2.doll()



##################json format.py#########################
# import json
# student={
#     "name":"varsha",
#     "age":18,
# }
# data=json.dumps(student) #converts python object into json object
# print(data)

import json
data='{"name":"varsha","age":18}'
result=json.loads(data) #converts json object into python object
print(result["name"])

#########main.py#########
# from calculator import sub
# print(sub(10,20))

# from calculator import add
# print(add(10,20)) 

# import calculator
# result=calculator.add(10,20)
# print(result)

# import calculator as cal
# result=cal.add(10,20)

# import math
# print(math.sqrt(16))


import random
number=(random.randint(1, 10))
print(number)

##########oops.py############
# ############class object########
# class student:#class name
#     name="bindhu" #attributes
#     def study(self):#represent current object
#         print("bindhu is studying")
# s1=student() #s1 is object
# print(s1.name) #accessing attributes
# s1.study()#study 


# class student:
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()
    
# student.details(s1)

##########constructor is a special method which is automatically called when an object of class is created

# class student:
#     def __init__(self,name,age): #initial is a constructor,self represents the current object
#         self.name=name
#         self.age=age
# s1=student("bindhu",22)
# s2=student("varsha",18)
# s3=student("vaishu",20)
# print(s1.name,s2.name,s3.name)
# print(s1.age,s2.age,s3.age)

# class bank: ### ther eare 2 methods balance and check_balance
# def __init__(self,balance):
#        self.balance=balance
# def check_balance(self):
#     print(self.balance)
#     account1=bank(1000)



class user:
    def __init__(self,name):
        self.name=name
    def login(self):
        print(self.name,"is logged in")
u1=user("varsha")
u2=user("vaishu")
u1.login()
u2.login()   