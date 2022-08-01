
#parent class
class User():
    def __init__(self,name,age,gender):
        self.name = name 
        self.age = age 
        self.gender = gender 

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)


#child class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0


    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"Account balance has been updated: $ {self.balance}")

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Funds | Avallieable Balance : $",self.balance)
        else:
            self.balance = self.balance - self.amount 
            print("Account has been updated: $",self.balance)

    def view_balance(self):
        self.show_details()
        print(f"Account balance: $ {self.balance}")




user1 = Bank("Mike",33,"male")
user1.deposit(99)
user1.withdraw(1)
print("")
user1.view_balance()

