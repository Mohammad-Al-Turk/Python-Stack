from BankAccount import BankAccount
class User:
    def __init__(self , name = None ,  balance = 0):
        self.name = name
        self.balance= balance
        self.account = BankAccount(rate=0.02,balance=0)
    
    def make_withdrawal(self, amount):
        self.balance= self.balance - amount
        return self.balance
        
    def display_user_balance(self):
        return print(f"User Name: {self.name}, balance: {self.balance}")
        
    def make_deposite(self, amount):
        self.balance= self.balance + amount
        return self.balance
    
    
zak=User("zak!",3000)
zak.make_deposite(999999999999999)


