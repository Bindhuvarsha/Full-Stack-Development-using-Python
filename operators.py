# product_price = 5000
# delivery_charge = 100

# total=product_price + delivery_charge
# print(total)




# ###############
# a=10
# b=3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b) #2 floating division
# print(a % b)
# print(a ** b)


# students = 10
# groups = 2
# print(students // groups)


# ################### assignment operators
# followers =100
# followers= followers - 1
# print(followers)


# followers =100
# followers +=1
# print(followers)


# ############comparision operators (==, !=, >, <, >=, <=)

# saved_password = "1234"
# enterd_password="1234"
# print(saved_password == enterd_password)



# saved_password = "1234"
# enterd_password="12345"
# print(saved_password == enterd_password)

# saved_password = "abcd"
# enterd_password="abcd"
# print(saved_password == enterd_password)

# saved_password = "abcde"
# enterd_password="abc"
# print(saved_password == enterd_password)


# ################logical operators
# balance = 5000
# pin_correct = True
# if balance >=1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")


# balance = 500
# pin_correct = True
# if balance <=1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")



# balance = 500
# pin_correct = True
# if balance >=1000 and pin_correct:
#     print("withdraw allowed")
# else:
#     print("failed")


# #########################billing calculators
# product = input("Enter product name: ")
# price = int(input("Enter product price: "))
# quantity = int(input("Enter product quantity: "))
# discount = int(input("Enter discount amount: "))
# total = price * quantity
# final_bill = total - discount
# print("Product:",product)
# print("Total amount:",total)
# print("Final bill:",final_bill)



# ######################################

# #password = input("Enter your password: ")
# if password == "admin123":
#     print("welcome")
# else:
#     print("wrong password")

# age = 20
# if age >= 18:
#      print("You are eligible to vote")


# marks = int(input("Enter your marks: "))   #conditions
# if marks >= 90:
#     print("CGPA 9")
# elif marks >= 75:
#     print("CGPA 8")
# else:
#     print("fail")

                   
 # logical conditions
######################AND#######################
# age = 25   
# salary = 500000
# if age > 18 and salary >30000:
#     print("loan approved")
# #######################OR#######################
# day = "sunday"
# if day == "saturday"or day == "sunday":
#     print("holiday")
# ######################NOT#######################
# age = 20
# if not age < 18:
#     print("eligible to vote")
# else:
#     print("not eligible")


# login = False
# if not login:
#     print("loggedin")



def withdraw_money():
    pin = input("enter pin:")
    if pin == "1234":
           amount = int(input("enter amount:"))
           balance = 5000
           if amount <= balance:
               balance = balance - amount
               print("withdraw successful")
               print("remaining balance:",balance)
           else:
               print("insufficient balance")
withdraw_money()