class User:
    def __init__(self , name = None ,  balance = 0):
        self.name = name
        self.balance= balance 
    
        
        
    def make_withdrawal(self, amount):
        self.balance= self.balance - amount
        return self#########
        

    def display_user_balance(self):
        print(f"User Name: {self.name}, balance: {self.balance}")
        return self  #########
    
        
    def transfer_money(self, amount, reciver_user):
        
        self.make_withdrawal(amount)
        reciver_user.make_deposite(amount)
        self.display_user_balance()
        reciver_user.display_user_balance()
        return self  #####
        
        
    def make_deposite(self, amount):
        self.balance= self.balance + amount
        return self######################
        
        
turk = User("Turk",50000)
sami = User("mo",0)

turk.display_user_balance()
turk.transfer_money(2000, sami)

turk.make_deposite(100).make_withdrawal(50).display_user_balance()