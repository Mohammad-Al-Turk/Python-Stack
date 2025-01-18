class BankAccount:
    def __init__(self, rate =0.01, balance = 10000999):

        self.rate = rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return print("you have now ",self.balance,"$")

    def withdraw(self, amount):

        if amount > self.balance:
            self.balance -= 5
            return print("Insufficient funds", self.balance)
        else:
            self.balance = self.balance - amount 
            return print("you have now ",self.balance,"$")
  
    def display_account_info(self):

        return print("you have now ",self.balance,"$")

    def yield_interest(self):

        if self.balance > 0:
            self.balance = self.balance * self.rate
            return print("you have now ",self.balance,"$")