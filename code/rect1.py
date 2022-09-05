class Rectangle:
    def __init__(self,l,w):
        print("In constructor")
        if l>0:
            self.__length=l
        else:
            self.__length=10
        if w>0:
            self.__width=w
        else:
            self.__width=5
    def get_area(self):
        area=self.__length*self.__width
        print("Area:",area)
        return area
    def set_length(self,l):
        if l>0:
            self.__length=l


class Account:
    def __init__(self):
        self.balance=0
    def get_balance(self):
        retrurn self.balance
    def withdraw(self,money):
        self.balance-=money

class SavingsAccount(Account):
    def __init__(self):
        self.interest=0.1


class PremiumSavingsAccount(SavingsAccount):
    
 
        
    

        
        
