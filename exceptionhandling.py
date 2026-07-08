# try:
#     a = 10
#     b = 0
#     print(a/b)
# except :
#     print("something went wrong")


# try :
#     num = int(input("enter number:"))
#     print(num)
# except ValueError :
#     print("only number allowed")             #############specific exception
 

# try :
#     a = int(input("enter A:"))
#     b = int(input("enter B:2"))
#     print(a/b)
# except ZeroDivisionError :
#     print("cannot divide by zero")
# except ValueError :
#     print("enter only numbers")        ############multiple exception


# try :
#     file = open("data.txt")
#     print(file.read())
# except :
#     print("file error")

# finally :
#     print("program completed")      #####final bloack:if errors exists the program will be executed using final block



########else block##############
try :
    print(10/2)
except :
    print("error")
else :
    print("success")