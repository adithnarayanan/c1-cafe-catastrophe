class ATM: 
    def __init__(self, balance=1000): 
        # Map accounts to balances
        self.accounts = {}
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount

    def deposit(self, amount):
        assert amount > 0
        self.balance += amount
        
    

