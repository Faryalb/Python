class BankAccount: 
    
    def __init__(self, first_name, last_name, balance, account_number, yield_int_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.account_number = account_number
        self.yield_int_rate = yield_int_rate

    def deposit(self, amount):
        self.balance += amount
        return self 

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("Insufficient funds: Charging a $5 fee") 
            self.balance = self.balance - 5
        else:
            return self

    def display_account_info(self):
        print(f" Hello {self.first_name} {self.last_name} your balance is ${self.balance}")
    
    def yield_int_rate(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            return self

      

faryal_acct = BankAccount("Faryal", "Bhatti", 2000, 123456,.2)
noor_acct = BankAccount("Noor", "Ausim", 4000, 34567,.5)

faryal_acct.deposit(25).deposit(100).deposit(40).withdraw(90).display_account_info()
noor_acct.deposit(400).deposit(40).withdraw(50).withdraw(100).withdraw(25).withdraw(10).display_account_info()
 
 #I was unable to get yield_int to work, will reach out to TA for help on this 