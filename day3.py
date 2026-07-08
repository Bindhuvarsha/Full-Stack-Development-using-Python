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

def add():
     return 10 + 20 
result = add()
print(result)


def sub() :
     return 10 -20
result = sub()
print(result)

def mul() :
     return 10 * 2
result = mul()
print(result)


def div() :
     return 10 / 5
result = div()
print(result)


