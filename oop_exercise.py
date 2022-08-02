#warrior
#archer 
#knight

#battle
#points 


class Warrior():

    def __init__(self,name,health,speed,attack):

        self.name = name 
        self.health = health 
        self.speed = speed 
        self.attack = attack 

    def action(self):
        print(f"{self.name} is attacking...with his maximum speed of {self.speed}")



class Archer(Warrior):

    def __init__(self,name,health,speed,attack,arrows):

        super().__init__(name,health,speed,attack)
        self.arrows = arrows 


class Knight(Warrior):

    def __init__(self,name,health,speed,attack,spear):

        super().__init__(name,health,speed,attack)
        self.spear = spear

    def battle(self):

        battle_mode = True

        if battle_mode == True:
            print("The game has started")
            print("There are two warriors on the field {knight.name} vs {archer.name}")



    



warrior = Warrior("Vega",100,50,20)

archer = Archer("Legolas",100,60,30,50)

knight = Knight("Cavalier",120,40,30,35)
knight.battle()







    