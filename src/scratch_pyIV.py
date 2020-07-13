""" Inheritance """
class Bicycle:
    def exclaim(self):
        print("I am a bicycle!")

class Specialized(Bicycle):
    def jump(self):
        print("I can jump!")

a_bike = Bicycle()
a_special_bike = Specialized()

a_special_bike.exclaim()    # I am a bicycle!
a_special_bike.jump()       # I can jump!


class Student:
    def __init__(self, name):
        self.name = name

class Graduate(Student):
    def __init__(self, name, grad_date):
        super().__init__(name)
        self.grad_date = grad_date

dan = Graduate('Dan', 'June 13')
dan

""" Aggregates """
class Duck:
    def __init__(self, name, bill_desc, tail_len, collar):
        self.name = name
        self.bill = Bill(bill_desc)
        self.tail = Tail(tail_len)
        self.collar = collar
    def about(self):
        # print(f'{self.name} has a {self.bill.description} bill and a {self.tail.length} tail.')
        print(f'{self.name} has a {self.bill.description} bill, a {self.tail.length} tail, and a {self.collar.color} collar.')

# Bill + Tail cannot exist without the Duck
class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

# duck = Duck("Quacker", "wide and orange", "long")

# duck.about()    # Quacker has a wide and orange bill and a long tail.

class Collar:
    def __init__(self, color):
        self.color = color

red_collar = Collar("red")

duckette = Duck("Quackette", "yellow", "short", red_collar)

duckette.about()    # Quackette has a yellow bill, a short tail, and a red collar.

"""
List Comprehensions
"""
people = ["Abe", "Billy", "Charles", "David", "Dolly", "Evelyn", "Frank", "Gunther"]

# comp for names that start with D
a = [i for i in people if i.startswith("D")]
print(a)
# same:
#   a = []
#   for i in people:
#       if person.startswith("D"):
#           b.append(person)

# comp for names that end in Y
b = [i for i in people if i.endswith("y")]
print(b)

# comp for names that start with B through D
letter = ["B", "C", "D"]
c = [i for i in people if i.startswith(tuple(letter))]
print(c)

# comp for names but in uppercase
d = [i.upper() for i in people]
print(d)