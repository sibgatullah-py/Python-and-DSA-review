class Account:
    def __init__(self,name,accountNo,balance):
        self.name = name
        self.accountNo = accountNo
        self.balance = balance
        
    def credit(self,amount):
        self.balance += amount
        print(f"Amount {amount} has been credited . Balance {self.balance}tk")
        
    def debit(self,amount):
        self.balance -= amount
        print(f"Amount {amount} has been debited . Balance {self.balance}tk")
        
    def get_balance(self):
        print(f'Account balance is {self.balance}tk')
 
 
 
acc1 = Account('Helal', 10001, 500)     
acc2 = Account('Sibgatullah', 10002, 100)     
acc3 = Account('Tahmeed', 10003, 1000)     

acc2.credit(50)
acc3.debit(70)
acc1.get_balance()

