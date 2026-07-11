# encapsulation means wrapping variables and methods together inside a class and controlling access of data 
class bank :
     def __init__(self):
          self.balance = 10000
account = bank()
account.balancde = 10000000
print(account.balance)    ##without data encapsulation


class bank :
    def __init__(self) :
        self.__balance = 10000
    def deposit(self,amount) :
        self.__balance +=amount
    def show_balance(self) :
        print(self.__balance)
account = bank()
account.deposit(5000)
account.show_balance()    ##with data encapsulation



########getter#########
class employee :
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self) :
        return self.__salary
emp = employee(52836)
print(emp.get_salary())



#########setter#######
class employee:
    def __init__(self):
        self.__salary = 0
    def set_salary(self,amount):
        if amount > 0 :
            self.__salary = amount
        else:
            print("invalid salary")

    def get_salary(self) :
        return self.__salary
emp = employee()
emp.set_salary(52836)
print(emp.get_salary())


#########################polymorphism#################################
#polymorphism means the same method name can perform a different action depending on the object

class dog :
    def sound(self) :
        print("dog barks")
class cat :
    def sound(self) :
        print("cat meows")
Dog = dog()
Cat = cat()

Dog.sound()
Cat.sound()

class Bank:
    def credited(self):
        print("Credited")


class Amount:
    def debited(self):
        print("Debited")


bank = Bank()
amount = Amount()

bank.credited()
amount.debited()


class PhonePe:
    def pay(self):
        print("Payment successful")


class GooglePay:
    def pay(self):
        print("Payment successful ")


phonepe = PhonePe()
googlepay = GooglePay()

phonepe.pay()
googlepay.pay()


#################abstraction-means hiding internal implementation and showing only the neccessary features to the user
