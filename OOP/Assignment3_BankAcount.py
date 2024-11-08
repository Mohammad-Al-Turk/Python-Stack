class BankAccount:
    def __init__(self, rate =0.01, balance = 0): # don't forget to add some default values for these parameters!
        # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
        self.rate = rate
        self.balance = balance
        
        
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        return print("you have now ",self.balance,"$")
    
    
    
    def withdraw(self, amount):
        # your code here
        if amount > self.balance:
            self.balance -= 5
            return print("Insufficient funds", self.balance)
        else:
            self.balance = self.balance - amount 
            return print("you have now ",self.balance,"$")

            
    def display_account_info(self):
        # your code here
        return print("you have now ",self.balance,"$")

        
        
        
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance = self.balance * self.rate
            return print("you have now ",self.balance,"$")

        
        
        
ahmad=BankAccount(0.01 , 5000)
ahmad.deposit(200)

turk=BankAccount(0.01 , 5000)
turk.deposit(200)