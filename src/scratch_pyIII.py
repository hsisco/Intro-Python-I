"""
Classes
"""
class Account:
    interest = 0.02
    def _init_(self, account_holder):
        self.balance = 10000
        self.holder = account_holder

    def deposit(self, amount):
        self.balance =+ amount  # self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds 😢"
        self.balance -= amount
        return self.balance

my_account = Account("Hysen")
his_account = Account("Dan")

my_account.interest = 0.05
print(my_account.interest)  # 0.05
print(his_account.interest) # 0.02

"""
Scope
"""
x = 1
y = 2

def my_function(x):
    y = 3
    print(x,y)

my_function(10)     # 10, 3

print(x,y)

x = 100

def my_outer_function(x):
    y = 50

def my_inner_function():
    print(x,y)

# my_inner_function()   # ERROR
my_outer_function(75)   # 10, 3
my_inner_function()     # ERROR

print(x,y)

"""
Store
"""
class Store:
    def __init__(self, name, catagories):
        #attributes
        self.name = name
        self.catagories =  catagories
    
    def __str__(self):
        output = f"{self.name}/n"
        for i, c in enumerate(self.catagories):
            output += " " + str(i+1)