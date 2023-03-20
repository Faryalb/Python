class BankAccount: 
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
       

    def deposit(self, amount):
        self.balance += amount
        return self 

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 5:
            print("Insufficient funds: Charging a $5 fee") 
            self.balance = self.balance - 5
        else:
            return self

    def display_account_info(self):
        print(f" Balance {self.balance}")
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            return self
        
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def deposit(self, amount):
        self.account.deposit(400)
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= BankAccount(amount)
        if self.balance < 5:
            print("Insufficient funds: Charging a $5 fee") 
            self.balance = self.balance - 5
        else:
            return self
    
    def display_user_balance(self, balance):
        print(f"Your balance is {self.balance}")
faryal_acct = BankAccount

