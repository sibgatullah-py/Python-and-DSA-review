class BankAccount:
    def __init__(self,account,password,balance):
        self.account = account
        self.__password = password
        self.__balance_val = balance
        
    def credit(self,amount):
        self.__balance_val += amount
        print(f"Account {self.account} has been credited {amount}tk")
        
    def __debit(self,amount):
        self.__balance_val -= amount
        print(f"Account {self.account} has been debited {amount}tk.\n New balance {self.__balance_val}")
    
    def __balance(self):
        print(f"Account {self.account} balance is {self.__balance_val}tk")
        
    def checker(self,pas,token,amount=0):
        if pas == self.__password and token == 1:
            self.__debit(amount)
        elif pas == self.__password and token == 2:
            self.__balance()
        else:
            print("wrong password")
            
user1 = BankAccount(1001,12345,1000)
user1.checker(12345,1,300)
user1.credit(600)
user1.checker(1234,2)