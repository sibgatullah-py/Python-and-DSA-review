class Account:
    def __init__(self,acc,bal):
        self.account = acc
        self.balance = bal
        
    def credit(self,increase):
        self.balance += increase
        print(f"account {self.account} has been credited {increase} tk")
        
    def debit(self, decrease):
        self.balance -= decrease
        print(f"account {self.account} has been debited {decrease} tk")
        
    def check(self):
        print(f"account {self.account} has balance of {self.balance} tk")
        
acc1 = Account(1001,1000)
acc1.check()

acc1.credit(1300)
acc1.check()
acc1.debit(400)
acc1.check()
        