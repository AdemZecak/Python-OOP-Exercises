#warrior
#archer 
#knight

#battle
#points 
import random
import time
import os


#this could be the BOSS warrior

class Warrior():

    def __init__(self,name,health,attack):

        self.name = name 
        self.health = health
        self.attack = attack

    def action(self):
        print(f"{self.name} is attacking...with his maximum speed")

#simple battle between two lower rank warriors 

class Archer(Warrior):

    def __init__(self,name,health,attack,arrows):

        super().__init__(name,health,attack)
        self.arrows = arrows 


class Knight(Warrior):

    def __init__(self,name,health,attack,spear):

        super().__init__(name,health,attack)
        self.spear = spear





warrior = Warrior("Vega",200,50)

archer = Archer("Legolas",20,20,55)

knight = Knight("Cavalier",30,20,35)


warriors = (archer.name,knight.name)

#random health damage
damage = random.randint(1,7)

#knight weapon health damage
spear_damage = random.randint(3,9)
#archer weapon health damage
arrow_damage = random.randint(1,6)


#random weapon loss
weapon = random.randint(1,5)


print("The game has started")
print(f"There are two warriors in the field {knight.name} vs {archer.name}")
print("")

while True: 


    #battle
    choice = random.choice(warriors)

    if archer.health <= 0:
            print(knight.name,"Won!")
            break
    elif archer.arrows <= 0:
        print("You have loss all your arrows, prepare to die!")


    if knight.health <= 0:
            print(archer.name,"Won!")
            break
    elif knight.spear <= 0:
        print("You have loss all your arrows, prepare to die!")
        time.sleep(1)
        os.system("cls")

    if choice == archer.name: 
        print("Archer is attacking....")
        knight.health = knight.health - arrow_damage
        #archer arrows are decreasing
        archer.arrows = archer.arrows - weapon
        print("-"*55)
        print("Archer health: ",archer.health)
        print("Archer's arrows: ",archer.arrows)
        print("*"*55)
        print("Knight health: ",knight.health)
        print("Knight's weapon: ",knight.spear)
        print("*"*55)
        print("-"*55)
        print("")
        time.sleep(1)
        os.system("cls")



    if choice == knight.name: 
        print("Knight is attacking....")
        archer.health = archer.health - spear_damage
        #archer arrows are decreasing
        knight.spear = knight.spear - weapon
        print("-"*55)
        print("Archer health: ",archer.health)
        print("Archer's arrows: ",archer.arrows)
        print("*"*55)
        print("Knight health: ",knight.health)
        print("Knight's weapon: ",knight.spear)
        print("*"*55)
        print("-"*55)
        print("")
        os.system("cls")



    

        






    