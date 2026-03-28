from math import ceil
from random import randint
import time
difficulty = 1

if (difficulty == 0.5):
    hitChance = 75
elif (difficulty == 1):
    hitChance = 85
elif (difficulty == 2):
    hitChance = 95

board = set(range(1,100))
eList = []
enemyList = []

class character:
    
    def __init__(self, name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass, position = 0):
        self.species = species
        self.hp = ceil(con * 4 * difficulty + 8)
        self.maxHp = self.hp
        self.con = ceil(con * difficulty)
        self.str = ceil(str * difficulty)
        self.dex = ceil(dex * difficulty)
        self.int = ceil(int * difficulty)
        self.wis = ceil(wis * difficulty)
        self.pArmor = ceil(pArmor * difficulty * 0.5)
        self.mArmor = ceil(mArmor * difficulty * 0.5)
        self.speed = dex // 3 + 4
        self.attackRange = attackRange
        self.name = name
        self.dist = position
        self.attackType = attackType
        self.pClass = pClass
        
        # board.remove(self.dist)
    
    def attack(self, target):

        a = False
        b = 0
        c = 0
        if (self.attackRange < 5):
            if (self.attackRange + self.speed -1 >= abs(self.dist - target.dist)):
                if (abs(target.dist - self.dist) == 1):
                    print('\033[1;31;1m' + self.name + '\033[0m' + " atakuje...")
                    a = True
                elif (target.dist - self.dist > 0):
                    if (target.dist - 1 in board):
                        b = target.dist - self.dist - 1
                        board.add(self.dist)
                        self.dist = target.dist - 1
                        board.remove(self.dist)
                        print('\033[1;31;1m' + self.name + '\033[0m' + f" porusza się o {b}m i atakuje...")
                        a = True
                    elif (target.dist + 1 in board):
                        b = target.dist - self.dist + 1
                        board.add(self.dist)
                        self.dist = target.dist + 1 
                        board.remove(self.dist)
                        print('\033[1;31;1m' + self.name + '\033[0m' + f" porusza się o {b}m i atakuje...")    
                        a = True      
                elif (target.dist - self.dist < 0):
                    if (target.dist + 1 in board):
                        b = self.dist - target.dist - 1
                        board.add(self.dist)
                        self.dist = target.dist + 1
                        board.remove(self.dist)
                        print('\033[1;31;1m' + self.name + '\033[0m' + f" porusza się o {b}m i atakuje...")
                        a = True
                    elif (target.dist - 1 in board):
                        b = self.dist - target.dist + 1
                        board.add(self.dist)
                        self.dist = target.dist - 1   
                        board.remove(self.dist)
                        print('\033[1;31;1m' + self.name + '\033[0m' + f" porusza się o {b}m i atakuje...") 
                        a = True 
        else:
            if (self.attackRange >= abs(self.dist - target.dist)):
                print('\033[1;31;1m' + self.name + '\033[0m' + " atakuje...")
                a = True
        if (a == True):
            time.sleep(1)
            if (self.attackType == "str"):
                if (randint(1,100) <= hitChance):
                    print(" Trafia!")
                    if (self.str - target.pArmor < 1):
                        target.hp -= 1
                        print(' \033[1;32;1m' + target.name + '\033[0m' + " traci 1 HP")
                    else:
                        dmg = self.str - target.pArmor
                        target.hp -= dmg
                        print(' \033[1;32;1m' + target.name + '\033[0m' + f" traci {dmg} HP")
                else:
                    print(" Nie trafia!")
                    return False
            if (self.attackType == "dex"):
                if (randint(1,100) <= hitChance):
                    print(" Trafia!")
                    if (self.dex - target.pArmor < 1):
                        target.hp -= 1
                        print(' \033[1;32;1m' + target.name + '\033[0m' + " traci 1 HP")
                    else:
                        dmg = self.dex - target.pArmor
                        target.hp -= dmg
                        print(' \033[1;32;1m' + target.name + '\033[0m' + f" traci {dmg} HP")
                else:
                    print(" Nie trafia!")
                    return False
            if (self.attackType == "int"):
                if (randint(1,100) <= hitChance):
                    print(" Trafia!")
                    if (self.int - target.pArmor < 1):
                        target.hp -= 1
                        print(' \033[1;32;1m' + target.name + '\033[0m' + " traci 1 HP")
                    else:
                        dmg = self.int - target.pArmor
                        target.hp -= dmg
                        print(' \033[1;32;1m' + target.name + '\033[0m' + f" traci {dmg} HP")
                else:
                    print(" Nie trafia!")
                    return False
        else:
            if (self.dist > target.dist):
                b = self.dist
                board.add(self.dist)
                self.dist -= self.speed
                while (self.dist not in board):
                    self.dist += 1
                c = self.dist
                board.remove(self.dist)
                print('\033[1;31;1m' + self.name + '\033[0m' + f" rusza się o {abs(c-b)}m.")
            elif (self.dist < target.dist):
                b = self.dist
                board.add(self.dist)
                self.dist += self.speed
                while (self.dist not in board):
                    self.dist -= 1
                c = self.dist
                board.remove(self.dist)
                print('\033[1;31;1m' + self.name + '\033[0m' + f" rusza się o {abs(b-c)}m.")    
    def moveForward(self):
        self.dist -= self.speed
        if (self.dist < 1):
            self.dist = 1  
    def moveBack(self):
        self.dist += self.speed
        if (self.dist > len(board)):
            self.dist = len(board) - 1


class goblinWarrior (character):
    def __init__(self, position, name="", species="Goblin", con=6, str=6, dex=5, int=3, wis=3, pArmor=1, mArmor=0, attackRange=1, pClass = "Wojownik", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 3
        self.worth = 25
        board.remove(self.dist)
        
class goblinArcher (character):
    def __init__(self, position, name="", species="Goblin", con=3, str=5, dex=8, int=3, wis=3, pArmor=0, mArmor=0, attackRange=30, pClass = "Łucznik", attackType="dex"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 3
        self.worth = 25
        board.remove(self.dist)

class goblinShaman (character):
    def __init__(self, position, name="", species="Goblin", con=3, str=3, dex=4, int=7, wis=5, pArmor=0, mArmor=1, attackRange=15, pClass = "Szaman", attackType="int"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 3
        self.worth = 30
        board.remove(self.dist)

class goblinChieftain (character):
    def __init__(self, position, name="", species="Wódz Goblinów", con=9, str=9, dex=7, int=6, wis=6, pArmor=2, mArmor=1, attackRange=2, pClass = "Wojownik", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 8
        self.worth = 85
        board.remove(self.dist)

class ghost (character):
    def __init__(self, position, name="", species="Duch", con=5, str=3, dex=7, int=6, wis=6, pArmor=4, mArmor=0, attackRange=1, pClass = "Wojownik", attackType="int"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass, position)
        self.exp = 5
        self.worth = 35
        board.remove(self.dist)

class oldMan (character):
    def __init__(self, position, name="", species="Człowiek", con=5, str=3, dex=5, int=10, wis=10, pArmor=1, mArmor=3, attackRange=12, pClass = "Mag", attackType="int"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass, position)
        self.exp = 8
        self.worth = 60
        board.remove(self.dist)

class banditWarrior (character):
    def __init__(self, position, name="", species="Człowiek", con=5, str=7, dex=4, int=3, wis=3, pArmor=0, mArmor=0, attackRange=1, pClass = "Wojownikk", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass, position)
        self.exp = 3
        self.worth = 40
        board.remove(self.dist)

class banditArcher (character):
    def __init__(self, position, name="", species="Człowiek", con=3, str=3, dex=6, int=3, wis=3, pArmor=0, mArmor=0, attackRange=15, pClass = "Łucznik", attackType="dex"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass, position)
        self.exp = 3
        self.worth = 40
        board.remove(self.dist)

class gargoyle (character):
    def __init__(self, position, name="", species="Gargulec", con=9, str=8, dex=4, int=3, wis=3, pArmor=3, mArmor=1, attackRange=2, pClass = "Wojownikk", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass, position)
        self.exp = 7
        self.worth = 35
        board.remove(self.dist)

class greyWolf (character):
    def __init__(self, position, name="", species="Wilk", con=6, str=7, dex=7, int=2, wis=2, pArmor=1, mArmor=0, attackRange=1, pClass = "", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 5
        self.worth = 20
        board.remove(self.dist)

class alphaWolf (character):
    def __init__(self, position, name="", species="Wilk", con=9, str=9, dex=9, int=3, wis=3, pArmor=3, mArmor=1, attackRange=1, pClass = "", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 10
        self.worth = 40
        board.remove(self.dist)

class dragon (character):
    def __init__(self, position, name="", species="Smok", con=18, str=13, dex=9, int=10, wis=20, pArmor=5, mArmor=5, attackRange=15, pClass = "", attackType="str"):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange,  attackType, pClass, position)
        self.exp = 500
        self.worth = 1