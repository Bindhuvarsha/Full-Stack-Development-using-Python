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