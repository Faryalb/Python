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
    
    # def yield_int_rate(self):
    #     if self.balance > 0:
    #         self.balance += self.balance * self.int_rate
    #     else:
    #         return self
        
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance = 0)
    
    def make_deposit(self, amount):
        self.account.deposit(100)
        print(self.account.balance)
    
    def make_withdraw(self, amount):
       self.account.make_withdraw()
       return self
    
    def display_user_balance(self, balance):
        self.account.display_user_balance()

faryal= User("FaryalBhatti", "faryal0605@gmail.com")
faryal.display_user_balance()



#Hello, I worked on this assignment with Sloan, in case there are any code similarities
# I was unable to get the code to work, kept reciving same error messages but unsure on how to resolve error