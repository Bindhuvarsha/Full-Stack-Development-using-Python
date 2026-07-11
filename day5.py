# encapsulation means wrapping variables and methods together inside a class and controlling access of data 
# class bank :
#      def __init__(self):
#          self.balance = 10000
# account = bank()
# account.balancde = 10000000
# print(account.balance)    ##without data encapsulation


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