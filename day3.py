# ##############tuples################# tuples are immutable and it is a collection used to store multiple variables,lists are mutable
# student = ("ram","sam","bheem")
# print(student [0])  ##  or print(student [-1]) or print(student) 

# numbers = (10,20,30,40)
# print(numbers [-3]) ## or print(numbers [3])



# data = [1,2,3]   ###using list
# data[0] = 100
# print(data)
   
# data = (1,2,3)   ###using tuple,tuples cannot be updated
# data[0] = 100
# print(data)



# x = (1,2,3,2,1,1,1)
# print(x.count(3))
# print(x.count(2))


# x = ("ram","ham","sam","jam","ram","ram")
# print(x.count("ram"))


# x = ("ram","ham","sam","jam","ram","ram")
# print(x.index("sam"))


# ##############tuple slicing################    Tuple slicing in  allows you to extract a subset of elements from a tuple using start, stop, and step indices.
# num = (10,20,30,40,50)
# print(num[1:4])
#########################



##################sets######################### set is a  collection of:remove duplicate values : stores unique values :no indexing :
# x ={1,2,3,2,1,1,1}
# print(x)
# data = {1,2,3}
# data.add(4)
# print(data)


##############union,intersection#################
# a = {1,2,3}
# b = {3,4,5}
# print(a|b)


# a = {1,2,3}
# b = {3,4,5}
# print(a & b)


###############fuction#######################
# def greeting():
#     print("hello students")
# greeting()

# def add():
#      return 10 + 20 
# result = add()
# print(result)


# def sub() :
#      return 10 -20
# result = sub()
# print(result)

# def mul() :
#      return 10 * 2
# result = mul()
# print(result)


# c

###############*args########################3
# def add(a,b):
#     print(a,b)
# add(10,20)

# def add(a,b):
#     print(a+b)
# add(10,2)
# def multiply(a,b):
#     print(a*b)
# multiply(10,2)
# def div(a,b):
#     print(a/b)
# div(10,2)
# def sub(a,b):
#     print(a-b)
# sub(10,2)

# def usha(*numders):
#    print(numders)
# usha(10,20,30,40,50)

# def add(*num):
#     total=0
#     for i in num:
#         total += i
#     print(total)
# add(10,20,30,40,50)

#############kwargs################

# def student(**details):
#     print("name :",details["name"])
#     print("age :",details["age"])
#     print("job :",details["job"])
# student(
#     name="penga",
#     age=22,
#     job="sales",
# )


# def square(x):         square fuction
#     return x * x
# print(square(16))

# square = lambda x:x*x   #lambda function
# print(square(25))

# add = lambda a,b:a+b
# print(add(10,20))

# add = lambda a,b:a*b
# print(add(10,20))

# dd = lambda a,b:a-b
# print(add(10,20))

# dd = lambda a,b:a/b
# print(add(10,20))

# even = lambda n: "Even" if n % 2 == 0 else "Odd"

# print(even(1))
# print(even(4))

# lower_case=lambda n :n.lower()
# upper_case=lambda n :n.upper()
# print(lower_case("RAM"))
# print(upper_case("raj"))


# sham = lambda name:name.upper()
# print(sham("ram charan"))

# sham = lambda text:len(text)
# print(sham("ram charan"))
 

##############file handling#####################    txt:transfer textfile


file = open("student.txt","w" )
file.write("Hello")
file.close()

print("data written successfully")

file = open("student.txt","r" )
data = file.read()
print(data)
file.close()

file = open("student.txt","a")
file.write("\n uta thindha dinga")
file.close()

print("data append successfully")

file = open("student.txt","r")
print(file.read())
file.close()
