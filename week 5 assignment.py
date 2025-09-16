from itertools import count


class bankaccount:
    def init(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount>self.balance:
            print("insufficient fund")
        else:
            self.balance -= amount
    def check_balance(self):
        print(f"{self.name}, balance :{self.balance}")
account = bankaccount( "lekan", 500)
account.deposit(100)
account.withdraw(200)
account.check_balance()

        
        

#POLYMORPHISM
class vehicle:
    def move(self):
        print("vehicle is moving")

class car(vehicle):
    def move(self):
        print("driving")

class plane(vehicle):
    def move(self):
        print("flying")

class boat(vehicle):
    def move(self):
        print("sailing")
vehicles = [car(), plane(), boat()]
for v in vehicles:
    v.move()
            