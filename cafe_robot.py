#robot waiter 
#guest 
#guest happiness
#robot rate 
#robot battery level


import time
import random 
import os

cafe_items = {
    "beer":"Calsberg",
    "juice":"Fanta",
    "coffe":"Julius Meinl",
}

class Robot():


    #rate service
    rate = 0
    battery = 90

    def __init__(self,name):

        self.name = name 

    #say hello to guests
    def hello(self):
        print("")
        print("Hello, welcome to our cafe!")


    #menu - order
    def order(self):

        #variable for random waiting 
        
        a = random.randint(1,10)

        print(f"Today, we offer: ",cafe_items)
        choose = input("Please choose one item: ")

        #checking if guest is waiting too long
        #more than 5sec robot.rate - 1, less than 5 sec robot.rate + 1 
        if choose == "beer": 
            print("Waiting...")
            waiting = time.sleep(a)
            if a <=5: 
                Robot.rate += 1
            else:
                Robot.rate -= 1
                print("Sorry for waiting...")
            print("Your waiting time is: ",a)

            print(f"You choose {cafe_items['beer']}. Enjoy your drink.")
        elif choose == "juice":
            print("Waiting...")
            waiting = time.sleep(a)
            if a <=5: 
                Robot.rate += 1
            else:
                Robot.rate -= 1
                print("Sorry for waiting...")
            print("Your waiting time is: ",a)
            print(f"You choose {cafe_items['juice']}. Enjoy your drink.")
        elif choose == "coffe":
            print("Waiting...")
            waiting = time.sleep(a)
            if a <=5: 
                Robot.rate += 1
            else:
                Robot.rate -= 1
                print("Sorry for waiting...")
            print("Your waiting time is: ",a)
            print(f"You choose {cafe_items['coffe']}. Enjoy your drink.")
        else:
            print("Wrong input. Please pick drink from the menu. ")


class Guest():

    #guest happines
    def __init__(self,happiness):

        self.happiness = happiness

    #service rating
    def rate_service(self):
        rate = int(input("Please rate our service (1-10): "))
        if rate >=5:
            Robot.rate += rate
            Robot.battery += 2
            self.happiness += rate

        else: 
            Robot.rate -= rate
            self.happiness -= rate
        
    def current_rating(self):

        print(f"Current robot rate is: {Robot.rate} points.")
        print("")
        print(f"Current guests happiness score is: {guest.happiness}")
        print("")
        print(f"Robot battery level: {Robot.battery}")




robot = Robot("Max")
guest = Guest(0)


while True: 

    robot.hello()
    print("-"*81)
    robot.order()

    guest.rate_service()
    print("-"*81)
    print(f"Current robot rate is: {Robot.rate} points.")
    print("")
    print(f"Current guests happiness score is: {guest.happiness}")
    print("")
    print(f"Robot battery level: {Robot.battery}")
    print("-"*81)

    current_status = input("To check current rate status press 1) to get order, press 2)")

    if current_status == "1":
        print("")
        guest.current_rating()
    elif current_status == "2":
        continue
    
    else: 
        print("Something went wrong...")










