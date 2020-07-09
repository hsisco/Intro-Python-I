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
        output = f"{self.name}\n"
        for i, c in enumerate(self.catagories):
            output += " " + str(i+1) + ". " + c.name + "\n"

    output += " " + str(len(self.catagories) + 1) + ". Exit"
    return output

my_store = Store("The Dugout", [Category("Running"), Category()])

"""
Products
"""
class Product:
    def __init__(self, name, price, description, brand, sku, on_sale=False):
        self.name = name
        self.price = price
        self.description = description
        self.brand = brand
        self.sku = sku
        self.on_sale = on_sale

    def __str__(self):
        return self.name + "\t$" + str(self.price)

class Clothing(Product):
    def __init__(self, color, size, name, price, description, brand, sku):
        super().__init__(name, price, description, brand, sku, on_sale=True): # putting on_sale here makes it impossible for a user to make on_sale be False
        self.color = color
        self.size = size
    
    def __str__(self):
        super().__str__() + " comes in " + self.color + ", " + self.size
        # makes Product str available and adds the new Clothing str

class Food(Product):
    pass

# Product reader function
products = []

def product_reader(products=[])