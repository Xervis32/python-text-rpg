import characters as char
from items import items
from random import choice, randint
import os
import time
class hero (char.character):
    def __init__(self, name="", species="Człowiek", con=0, str=0, dex=0, int=0, wis=0, cha=0, pArmor=0, mArmor=0, pClass=0, attackRange=0, attackType=""):
        super().__init__(name, species, con, str, dex, int, wis, pArmor, mArmor, attackRange, attackType, pClass)
        self.pClass = pClass
        self.cha = cha
        self.maxHp = 3200
        self.armor = None
        self.weapon = None
        self.neklace = None
        self.ring1 = None
        self.ring2 = None
        self.level = 1
        self.exp = 0
        self.money = 25
        self.progress = 0
        self.eq = []
        self.equipment = []
    
    
    def start(self):
        while True:
            while True:
                print('\033[1;37;1m' + "Wybierz poziom trudności:" + '\033[0m')
                print("\n (1) Łatwy")
                print(" (2) Normalny")
                print(" (3) Trudny")
                print("\n (0) Powrót")

                try:
                    opt = int(input("\n> "))
                except:
                    os.system('cls')
                    continue
                match opt:
                    case 1:
                        char.difficulty = 0.5
                        break
                    case 2:
                        char.difficulty = 1
                        break
                    case 3:
                        char.difficulty = 2
                        break
                    case 0:
                        return False
                    case _:
                        os.system('cls')
                        continue
            os.system('cls')
            while True:
                print('\033[1;37;1m' + "Wpisz imię swojej postaci:" + '\033[0m')
                iname = input("\n> ")
                if (iname.isalpha() == False):
                    os.system('cls')
                    continue
                self.name = iname
                os.system('cls')
                break
            while True:
                print('\033[1;37;1m' + "Wybierz swoją klasę:"+ '\033[0m')
                print("")
                print(" (1) Wojownik\n (2) Łucznik\n (3) Łotrzyk\n (4) Mag")
                try:
                    opt = int(input("\n> "))
                except:
                    os.system('cls')
                    continue
                if (opt==1):
                    self.pClass="Warrior"
                    self.weapon = items["trainingSword"]
                    self.str = 6
                    self.con = 6
                    self.dex = 4
                    self.int = 3
                    self.wis = 3
                    self.cha = 5
                    break
                elif (opt==2):
                    self.pClass="Archer"
                    self.weapon = items["shortBow"]
                    self.str = 4
                    self.con = 5
                    self.dex = 6
                    self.int = 3
                    self.wis = 4
                    self.cha = 5
                    break
                elif (opt==3):
                    self.pClass="Rouge"
                    self.weapon = items["dagger"]
                    self.str = 4
                    self.con = 5
                    self.dex = 6
                    self.int = 3
                    self.wis = 4
                    self.cha = 5
                    break
                elif (opt==4):
                    self.pClass="Mage"
                    self.weapon = items["apprenticeWand"]
                    self.str = 3
                    self.con = 4
                    self.dex = 3
                    self.int = 7
                    self.wis = 5
                    self.cha = 5
                    break
                else:
                    os.system('cls')
                    continue
            os.system('cls')
            self.armor = items["leatherVest"]
            self.pArmor += self.armor["pArmor"]
            self.mArmor += self.armor["mArmor"]
            self.take("smallHpPotion")        
            self.take("smallHpPotion")  
            self.take("smallHpPotion")  
            i = 9
            print('\033[1;37;1m' + "Rozwój postaci\n" + '\033[0m')
            match self.pClass:
                    case "Warrior":
                        print(" Początkowe statyski wojownika:")
                    case "Archer":
                        print(" Początkowe statyski łucznika:")
                    case "Rouge":
                        print(" Początkowe statyski łotrzyka:")
                    case "Mage":
                        print(" Początkowe statyski maga:")
            while (i > 0):
                if (i != 9):
                    print('\033[1;37;1m' + "Rozwój postaci\n" + '\033[0m')
                    print(" Twoje statystki:")
                print(f"  (1) Siła: {self.str}")
                print(f"  (2) Witalność: {self.con}")
                print(f"  (3) Zręczność: {self.dex}")
                print(f"  (4) Inteligencja: {self.int}")
                print(f"  (5) Wiedza: {self.wis}")
                print(f"  (6) Charyzma: {self.cha}")
                print(f"\n Punkty do rozdysponowania: {i}")
                try:
                    a = int(input("\n> "))
                except:
                    os.system('cls')
                    continue
                match a:
                    case 1:
                        self.str += 1
                        i -= 1
                        os.system('cls')
                        continue
                    case 2:
                        self.con += 1
                        i -= 1
                        os.system('cls')
                        continue
                    case 3:
                        self.dex += 1
                        i -= 1
                        os.system('cls')
                        continue
                    case 4:
                        self.int += 1
                        i -= 1
                        os.system('cls')
                        continue
                    case 5:
                        self.wis += 1
                        i -= 1
                        os.system('cls')
                        continue
                    case 6:
                        self.cha += 1
                        i -= 1
                        os.system('cls')
                        continue
                    case _:
                        os.system('cls')
                        continue
            while True:
                self.calcMaxHp()
                self.calcSpeed()
                print('\033[1;37;1m' +"Podsumowanie\n" + '\033[0m')
                print(f" Imię: {self.name}")
                if (self.pClass == "Warrior"):
                    print(" Klasa: Wojownik")
                elif (self.pClass == "Archer"):
                    print(" Klasa: Łucznik")
                elif (self.pClass == "Rouge"):
                    print(" Klasa: Łotrzyk")
                elif (self.pClass == "Mage"):
                    print(" Klasa: Mag")
                print("\n Statyski:")
                print(f"  - Zdrowie: {self.hp}  \t(10 + witalność * 4)")
                print(f"  - Szybkość: {self.speed} \t(5 + zręczność / 3)")
                print(f"  - Siła: {self.str}")
                print(f"  - Witalność: {self.con}")
                print(f"  - Zręczność: {self.dex}")
                print(f"  - Inteligencja: {self.int}")
                print(f"  - Wiedza: {self.wis}")
                print(f"  - Charyzma: {self.cha}")
                print("\n Początkowe wyposażenie:")
                print(f'  - {self.weapon["name"]}\n  - {self.armor["name"]}\n  - {self.equipment[0]}\n  - 25 złota')
                print("\n (1) Rozpocznij grę")
                print(" (2) Zacznij jeszcze raz")
                try:
                    b = int(input("\n> "))
                except:
                    os.system('cls')
                    continue
                match b:
                    case 1:
                        os.system('cls')
                        return True
                    case 2:
                        os.system('cls')
                        break
                    case _:
                        os.system('cls')
                        continue

    def fight(self, dist=1, boardSize=100,*target):
        os.system('cls')
        def getDist(e):
            return e['dist']
        self.dist = dist
        char.board = set(range(boardSize))
        char.board.remove(self.dist)
        goldAcquired = 0
        expAcquired = 0
        x = -21
        if (self.pClass == "Warrior"):
            klasa = "Wojownik"
        elif (self.pClass == "Archer"):
            klasa = "Łucznik"
        elif (self.pClass == "Rouge"):
            klasa = "Łotrzyk"
        elif (self.pClass == "Mage"):
            klasa = "Mag"
        for enemy in target:
            char.board.remove(enemy.dist)
            char.board.add(x)
            x -= 1
            char.eList.append(enemy)
        while (len(char.eList) != 0):
            pr = [{"name": "P1", "dist": self.dist}]
            for i in range(len(char.eList)):
                pr.append({"name": char.eList[i].name, "dist": char.eList[i].dist})
            pr.sort(key=getDist)           
            print("\u2554", end="")
            for s in range(len(char.board)):
                s += 1
                if (s % 10 == 0):
                    print("\u2555\u2552", end="")
                else:
                    print(2*"\u2550", end="")
            print("\u2557")
            
            print("\u2551", end="")
            for s in range(len(char.board)):
                s += 1
                if (s % 10 == 0):
                    print(s, end="")
                else:
                    print(2*" ", end="")
            print("\u2551")

            print("\u2551"+ '\033[1;90;1m' + len(char.board) * 2 * "\u2594" + '\033[0m' + "\u2551")

            print("\u2551", end="")
            for i in range(len(pr)):
                if (pr[i]['name'] != "P1"):
                    if (i == 0):
                        print((pr[i]['dist']-1) * 2 * '\u00A0' + '\033[1;31;1m' + pr[i]['name'] + '\033[0m', end="")
                    else:
                        print((pr[i]['dist'] - pr[i-1]['dist']-1) * 2 * " " + '\033[1;31;1m' + pr[i]['name'] + '\033[0m', end="")
                else:
                    if (i == 0):
                        print((pr[i]['dist']-1) * 2 * " " + '\033[1;32;1m' + pr[i]['name'] + '\033[0m', end="")
                    else:
                        print((pr[i]['dist'] - pr[i-1]['dist']-1) * 2 * " " + '\033[1;32;1m' + pr[i]['name'] + '\033[0m', end="")
            print(((len(char.board) - pr[-1]['dist']) * 2) * " " + "\u2551")
            
            print("\u2551"+ '\033[1;90;1m' + len(char.board) * 2 * "\u2581" + '\033[0m' + "\u2551")
            
            print("\u2551"+ len(char.board) * 2 * " " + "\u2551")
            
            print("\u255A"+ len(char.board) * 2 * "\u2550" + "\u255D")

#1 
            print(f"\n  P1 - {self.name}" + (27-len(self.name))*" ", end="")
            for enemy in char.eList:
                print(enemy.name + 22*" ", end="")
#2
            print("\n \u250C" + 20 * "\u2500" + "\u2510" + 10*" ", end="")
            for enemy in char.eList:
                print("\u250C" + 20 * "\u2500" + "\u2510" + 2*" ", end="")
#3
            print("\n \u2502Klasa: " + klasa + (13-len(klasa))*" "+ "\u2502" + 10*" ", end="")
            for enemy in char.eList:
                print("\u2502Klasa: " + enemy.pClass + (13-len(enemy.pClass))* " " + "\u2502" + 2*" ", end="")
#4
            print("\n \u2502Rasa: " + self.species + (14-len(self.species))*" "+ "\u2502" + 10*" ", end="")
            for enemy in char.eList:
                print("\u2502Rasa: " + enemy.species + (14-len(enemy.species))* " " + "\u2502" + 2*" ", end="")
#5            
            print("\n \u2502Zasięg: " + str(self.weapon['range']) + (12-len(str(self.weapon['range'])))*" "+ "\u2502" + 10*" ", end="")
            for enemy in char.eList:
                print("\u2502Zasięg: " + str(enemy.attackRange) + (12-len(str(enemy.attackRange)))* " " + "\u2502" + 2*" ", end="")
#6            
            print("\n \u2502Pozycja: " + str(self.dist) + (11-len(str(self.dist)))*" "+ "\u2502" + 10*" ", end="")
            for enemy in char.eList:
                print("\u2502Pozycja: " + str(enemy.dist) + (11-len(str(enemy.dist)))* " " + "\u2502" + 2*" ", end="")
#7
            print("\n \u2502Szybkość: " + str(self.speed) + (10-len(str(self.speed)))*" "+ "\u2502" + 10*" ", end="")
            for enemy in char.eList:
                print("\u2502Szybkość: " + str(enemy.speed) + (10-len(str(enemy.speed)))* " " + "\u2502" + 2*" ", end="")
#8            
            print(f"\n \u2502Hp: {self.hp}/{self.maxHp}" + (15-len(str(self.hp))-len(str(self.maxHp)))*" "+ "\u2502" + 10*" ", end="")
            for enemy in char.eList:
                print(f"\u2502Hp: {enemy.hp}/{enemy.maxHp}" + (15-len(str(enemy.hp))-len(str(enemy.maxHp)))* " " + "\u2502" + 2*" ", end="")
#9            
            print("\n \u2514" + 20 * "\u2500" + "\u2518" + 10*" ", end="")
            for enemy in char.eList:
                print("\u2514" + 20 * "\u2500" + "\u2518" + 2*" ", end="")


            print("\n\n(1) Atakuj!\n(2) Podejdź\n(3) Cofnij się\n(4) Czekaj\n(5) Ekwipunek\n")
            match (input("> ")):
                case "1":
                    while True:
                        if (len(char.eList) == 1):
                            target = 1
                        else:
                            print("\nWybierz cel. Wpisz \"0\" by anulować")
                            i = 0
                            for enemy in char.eList:
                                i += 1
                                print(f" ({i}) {enemy.name}")
                            try:
                                target = int(input("\n> "))
                            except:
                                time.sleep(1.5)
                                continue
                            if (target == 0):
                                break
                            if (target < 0 or target > len(char.eList)):
                                continue
                        break
                    if (self.attack(char.eList[target-1]) != False):
                        if (char.eList[target-1].hp <= 0):
                            print('\033[1;31;1m' + char.eList[target-1].name + '\033[0m' + " umiera")
                            time.sleep(0.5)
                            expAcquired += char.eList[target-1].exp
                            goldAcquired += char.eList[target-1].worth
                            x += 1
                            char.board.remove(x)
                            char.board.add(char.eList[target-1].dist)
                            del char.eList[target-1]
                    else:
                        print("Jesteś za daleko\n")
                        time.sleep(1)
                        os.system('cls')
                        continue
                case "2":
                    if (self.moveForward() == True):
                        continue     
                    os.system('cls')
                                       
                case "3":
                    if (self.moveBack() == True):
                        continue     
                    os.system('cls')
                case "4":
                    os.system('cls')
                case "5":
                    os.system('cls')
                    if (self.showEq(1) == False):
                        os.system('cls')
                        continue
                    # os.system('cls')
                    continue
                case _:
                    os.system('cls')
                    continue
            for enemy in char.eList:
                enemy.attack(self)
                if (self.hp <= 0):
                    os.system('cls')
                    print('\033[0;31;1m' + "Umarłeś" + '\033[0m')
                    print(f"\n Postęp: " + '[\033[1;34;1m' + self.progress*"\u25AE" + 5*" " + '\033[0m]' )
                    while (len(char.eList) != 0):
                        del char.eList[0]
                    del self
                    char.board = set(range(1,100))
                    input("\n\t(Enter) Kontynuuj\n\n> ")
                    return False
        os.system('cls')
        print('\033[1;37;1m' + "Wygrałeś!" + '\033[0m')
        print("\n Zdobyte złoto: \033[1;32;1m" + f"{goldAcquired}" + '\033[0m')
        print(" Zdobyte doświadczenie: \033[1;32;1m" + f"{expAcquired}" + '\033[0m')
        char.board = set(range(1,100))
        self.money += goldAcquired
        self.exp += expAcquired
        input("\n\t(Enter) Kontynuuj\n\n> ")

    def attack(self, target):
        a = False
        dmg = 0
        if (self.weapon["range"] < 5):
            if (self.weapon["range"] + self.speed -1 > abs(self.dist - target.dist)):
                if (abs(target.dist - self.dist) == 1):
                    a = True
                elif (target.dist - self.dist > 0):
                    if (target.dist - 1 in char.board):
                        char.board.add(self.dist)
                        self.dist = target.dist - 1
                        char.board.remove(self.dist)
                        a = True
                    elif (target.dist + 1 in char.board):
                        char.board.add(self.dist)
                        self.dist = target.dist + 1 
                        char.board.remove(self.dist)     
                        a = True      
                elif (target.dist - self.dist < 0):
                    if (target.dist + 1 in char.board):
                        char.board.add(self.dist)
                        self.dist = target.dist + 1
                        char.board.remove(self.dist)
                        a = True
                    elif (target.dist - 1 in char.board):
                        char.board.add(self.dist)
                        self.dist = target.dist - 1   
                        char.board.remove(self.dist)   
                        a = True 
        else:
            if (self.weapon["range"] >= abs(self.dist - target.dist)):
                a = True
        if (a == True):
            os.system('cls')
            print("Atakujesz...")
            time.sleep(1)
            if (self.weapon["scale"] == "str"):
                if (randint(1,100) <= self.str*2 + 55):
                    dmg = self.str//2 + self.weapon["damage"] - target.pArmor
                    target.hp -= dmg
                    # os.system('cls')
                    print(" Trafiłeś!")
                    print(' \033[1;31;1m' + target.name + '\033[0m' + f" traci {dmg} HP")
                else:
                    # os.system('cls')
                    print(" Nie trafiłeś!")
            if (self.weapon["scale"] == "dex"):
                if (randint(1,100) <= self.dex*2 + 55):
                    dmg = self.dex//2 + self.weapon["damage"] - target.pArmor
                    target.hp -= dmg
                    # os.system('cls')
                    print(" Trafiłeś!")
                    print(' \033[1;31;1m' + target.name + '\033[0m' + f" traci {dmg} HP")
                else:
                    # os.system('cls')
                    print("Nie trafiłeś!")
            if (self.weapon["scale"] == "int"):
                if (randint(1,100) <= self.int*2 + 55):
                    dmg = self.int//2 + self.weapon["damage"] - target.mArmor
                    target.hp -= dmg
                    # os.system('cls')
                    print(" Trafiłeś!")
                    print(' \033[1;31;1m' + target.name + '\033[0m' + f" traci {dmg} HP")
                else:
                    # os.system('cls')
                    print(" Nie trafiłeś!")
        else:
            return False

    def moveForward(self):
        fieldTaken = False
        wrongInput = False
        moveOpt = []
        for i in range (1, self.speed + 1):
            moveOpt.append(i)
       
        while True:
            print(f"Możesz się ruszyć na {self.speed} metrów. Wpisz \"0\" by anulować")
            if (fieldTaken == True):
                print("Pole zajęte.")
                time.sleep(1)
            if (wrongInput == True):
                print("Podaj poprawną wartosć.")
                time.sleep(1)
            fieldTaken = False
            wrongInput = False
            try:
                move = int(input("Jak daleko chcesz podejsć: "))
            except:
                print("Podaj poprawną wartosć.")
                time.sleep(1)
                continue
            if (move in moveOpt):
                if (self.dist + move in char.board):
                    char.board.add(self.dist)
                    self.dist += move
                    char.board.remove(self.dist)
                    break
                elif (self.dist == len(char.board)-1):
                    wrongInput = True
                elif (self.dist + move > len(char.board)):
                    char.board.add(self.dist)
                    self.dist = len(char.board)-1
                    while (self.dist not in char.board):
                        self.dist -= 1
                    char.board.remove(self.dist)
                    break
                else:
                    fieldTaken = True
            elif (move == 0):
                os.system('cls')
                return True
            else:
                wrongInput = True

    def moveBack(self):
        fieldTaken = False
        wrongInput = False
        moveOpt = []
        for i in range (1, self.speed + 1):
            moveOpt.append(i)

        while True:
            print(f"Możesz się ruszyć na {self.speed} metrów. Wpisz \"0\" by anulować")
            if (fieldTaken == True):
                print("Pole zajęte.")
                time.sleep(1)
            if (wrongInput == True):
                print("Podaj poprawną wartosć.")
                time.sleep(1)
            fieldTaken = False
            wrongInput = False
            try:
                move = int(input("Jak bardzo chcesz się cofnąć: "))
            except:
                print("Podaj poprawną wartosć.")
                time.sleep(1)
                continue
            if (move in moveOpt):
                if (self.dist == 1):
                    wrongInput = True
                elif (self.dist - move < 1):
                    char.board.add(self.dist)
                    self.dist = 1
                    while (self.dist not in char.board):
                        self.dist += 1
                    char.board.remove(self.dist)
                    break
                elif (self.dist - move in char.board):
                    char.board.add(self.dist)
                    self.dist -= move
                    char.board.remove(self.dist)
                    break
                
                else:
                    fieldTaken = True
            elif (move == 0):
                os.system('cls')
                return True
            else:
                wrongInput = True

    def showEq(self, inFight = 0, inShop = 0):
        
        while True:
            notEquipble = False
            notEquipbleF = False
            print('\033[1;37;1m' + "Ekwipunek:"  + '\033[0m')
            print(" -------------------------------------")
            if (self.armor != None):
                print(f'  Zbroja - {self.armor["name"]}')
            else:
                print(f"  Zbroja - ")
            if (self.weapon != None):    
                print(f'  Broń - {self.weapon["name"]}')
            else:
                print(f"  Broń - ")
            if (self.neklace != None):
                print(f'  Naszyjnik - {self.neklace["name"]}')
            else:
                print(f"  Naszyjnik - ")
            if (self.ring1 != None):
                print(f'  Pierścień (lewa ręka) - {self.ring1["name"]}')
            else:
                print(f"  Pierścień (lewa ręka) - ")
            if (self.ring2 != None):
                print(f'  Pierścień (prawa ręka) - {self.ring2["name"]}')
            else:
                print(f"  Pierścień (prawa ręka) - ")
            print(" -------------------------------------")
            print(" Plecak:")
            for i in range(len(self.equipment)):
                print(f"  ({i+1}) {self.equipment[i]}")
            print("\n  (0) Wyjdź")
            try:
                a = int(input("\n> "))
            except:
                os.system('cls')
                continue
            if (a == 0):
                os.system('cls')
                return False
            elif (a > len(self.equipment)):
                os.system('cls')
                continue
           
            while True:
                os.system('cls')
                print(self.eq[a-1]["desc"])
                if (inShop == 1):
                    print(f' Wartość: {self.eq[a-1]["worth"]}')
                if (notEquipble == True):
                    print("\nNie możesz tego założyć")
                if (notEquipbleF == True):
                    print("\nNie możesz założyć przedmiotu podczas walki")
                if (self.eq[a-1]["type"] == "armor" or self.eq[a-1]["type"] == "weapon" or self.eq[a-1]["type"] == "ring" or self.eq[a-1]["type"] == "neklace"):
                    x = "equip"
                    print("\n (1) Załóż")
                elif (self.eq[a-1]["type"] == "usable"):
                    x = "use"
                    print("\n (1) Użyj")
                print(" (2) Zniszcz")
                if (inShop == 1):
                    print(" (3) Sprzedaj")
                print("\n (0) Anuluj")
                try:
                    b = int(input("\n> "))
                except:
                    continue
                match b:
                    case 1:
                        if (x == "equip"):
                            if (inFight == 0):
                                if (self.equip(self.eq[a-1]) == False):
                                    notEquipble = True
                                    continue
                                break
                            else:
                                notEquipbleF = True
                                continue
                        elif (x == "use"):
                            if (self.hp == self.maxHp):
                                print("\n Masz pełne zdrowie")
                                time.sleep(1)
                                os.system('cls')
                                break
                            else:
                                os.system('cls')
                                h = self.maxHp - self.hp
                                if (self.hp + self.eq[a-1]["heal"] > self.maxHp):
                                    print('\033[1;32;1m' + self.name + '\033[0m' + " leczy się o " + str(h))
                                    self.hp = self.maxHp
                                else:
                                    print('\033[1;32;1m' + self.name + '\033[0m' + f' leczy się o {self.eq[a-1]["heal"]}')
                                    self.hp += self.eq[a-1]["heal"]
                                self.eq.pop(a-1)
                                self.equipment.pop(a-1)
                                return True
                    case 2:
                        os.system('cls')
                        print("Czy jesteś pewny?\n\n (1) Tak\n (2) Nie")
                        while True:
                            try:
                                c = int(input("\n> "))
                            except:
                                continue
                            match c:
                                case 1:
                                    self.eq.pop(a-1)
                                    self.equipment.pop(a-1)
                                    os.system('cls')
                                    break
                                case 2:
                                    os.system('cls')
                                    break
                                case _:
                                    continue
                        if (c == 1):
                            break
                    case 3:
                        os.system('cls')
                        print("Czy jesteś pewny?\n\n (1) Tak\n (2) Nie")
                        while True:
                            try:
                                c = int(input("\n> "))
                            except:
                                continue
                            match c:
                                case 1:
                                    self.money += self.eq[a-1]["worth"]
                                    self.eq.pop(a-1)
                                    self.equipment.pop(a-1)
                                    os.system('cls')
                                    break
                                case 2:
                                    os.system('cls')
                                    break
                                case _:
                                    continue
                        if (c == 1):
                            break
                    case 0:
                        os.system('cls')
                        break
                    case _:
                        os.system('cls')
                        continue

    def take(self, item):
        self.eq.append(items[item])
        self.equipment.append(items[item]["name"])

    def equip(self, item):
        canNotEquip = False
        if (item in self.eq and item["name"] in self.equipment):
            if (self.str >= item["req"]["str"] and self.con >= item["req"]["con"] and self.dex >= item["req"]["dex"] and self.int >= item["req"]["int"] and self.wis >= item["req"]["wis"]):
                if (item["type"] == "armor"):
                    if (self.armor != None):
                        self.eq.append(self.armor)
                        self.equipment.append(self.armor["name"])
                        self.pArmor -= self.armor["pArmor"]
                        self.mArmor -= self.armor["mArmor"]
                        self.speed += self.armor["weight"]
                    self.armor = item
                    self.eq.remove(item)
                    self.equipment.remove(item["name"])
                    self.pArmor += item["pArmor"]
                    self.mArmor += item["mArmor"]
                    self.speed -= item["weight"]
                    os.system('cls')
                elif (item["type"] == "weapon"):
                    if (self.weapon != None):
                        self.eq.append(self.weapon)
                        self.equipment.append(self.weapon["name"])
                    self.weapon = item
                    self.speed -= item["weight"]
                    self.eq.remove(item)
                    self.equipment.remove(item["name"])
                    os.system('cls')
                elif (item["type"] == "ring"):
                    if (self.ring1 == None):
                        self.ring1 = item
                        if (item["give" == "str"]):
                            self.str += item["value"]
                        elif (item["give" == "con"]):
                            self.con += item["value"]
                        elif (item["give" == "dex"]):
                            self.dex += item["value"]
                        elif (item["give" == "int"]):
                            self.int += item["value"]
                        elif (item["give" == "wis"]):
                            self.wis += item["value"]
                        self.eq.remove(item)
                        self.equipment.remove(item["name"])
                        os.system('cls')
                    elif (self.ring2 == None):
                        self.ring2 = item
                        if (item["give" == "str"]):
                            self.str += item["value"]
                        elif (item["give" == "con"]):
                            self.con += item["value"]
                        elif (item["give" == "dex"]):
                            self.dex += item["value"]
                        elif (item["give" == "int"]):
                            self.int += item["value"]
                        elif (item["give" == "wis"]):
                            self.wis += item["value"]
                        self.eq.remove(item)
                        self.equipment.remove(item["name"])
                        os.system('cls')
                    else:
                        self.eq.append(self.ring1)
                        self.equipment.append(self.ring1["name"])
                        if (self.ring1["give" == "str"]):
                            self.str -= self.ring1["value"]
                        elif (self.ring1["give" == "con"]):
                            self.con -= self.ring1["value"]
                        elif (self.ring1["give" == "dex"]):
                            self.dex -= self.ring1["value"]
                        elif (self.ring1["give" == "int"]):
                            self.int -= self.ring1["value"]
                        elif (self.ring1["give" == "wis"]):
                            self.wis -= self.ring1["value"]
                        self.ring1 = self.ring2
                        self.ring2 = item
                        if (item["give" == "str"]):
                            self.str += item["value"]
                        elif (item["give" == "con"]):
                            self.con += item["value"]
                        elif (item["give" == "dex"]):
                            self.dex += item["value"]
                        elif (item["give" == "int"]):
                            self.int += item["value"]
                        elif (item["give" == "wis"]):
                            self.wis += item["value"]
                        self.eq.remove(item)
                        self.equipment.remove(item["name"])
                        os.system('cls')
                elif (item["type"] == "neklace"):
                    if (self.neklace != None):
                        self.eq.append(self.neklace)
                        self.equipment.append(self.neklace["name"])
                        if (self.neklace["give"] == "hp"):
                            self.hp -= self.neklace["value"]
                        elif (self.neklace["give"] == "mArmor"):
                            self.mArmor -= self.neklace["value"]
                    self.neklace = item
                    if (item["give"] == "hp"):
                        self.hp += item["value"]
                    elif (item["give"] == "mArmor"):
                        self.mArmor += item["value"]
                    self.eq.remove(item)
                    self.equipment.remove(item["name"])
                    os.system('cls')
            else:
                os.system('cls')
                return False
        else: 
            return False

    def loot(self):
        i = 0
        a = 20 + self.level * 7
        b = a - 30
        lootItems = []
        while (i < randint(1,4)):
            lootItem = (choice(list(items.keys())))
            if (b < items[lootItem]["rarity"] <= a):
                if (items[lootItem] not in lootItems):
                    lootItems.append(items[lootItem])
                    i += 1
        for item in lootItems:
            self.eq.append(item)
            self.equipment.append(item["name"])
            print(f' - {item["name"]}')
        input("\n\t(Enter)\n\n> ")
        
    def shop(self):
        os.system('cls')
        notEnoughMoney = False
        st = []
        i = 0
        a = 20 + self.level * 15
        b = a - 40
        if (b <= 0):
            b = 1
        st.append(items["smallHpPotion"])
        while (i < randint(6,10)):
            shopItem = (choice(list(items.keys())))
            if (b < items[shopItem]["rarity"] <= a):
                if (items[shopItem] not in st):
                    st.append(items[shopItem])
                    i += 1
        while True:
            print('\033[4;37;1m' + "Sklep" + '\033[0m')
            print("\n (1) Kup")
            print(" (2) Sprzedaj")
            print("\n (0) Wyjdź")
            try:
                a = int(input("\n> "))
            except:
                os.system('cls')
                continue
            match a:
                case 1:
                    os.system('cls')
                    while True:
                        print('\033[4;37;1m' + "Sklep" + '\033[0m\n')
                        for i in range(len(st)):
                            print(f' ({i+1}) {st[i]["name"]}')
                        print("\n(0) Powrót")
                        try:
                            b = int(input("\n> "))
                        except:
                            os.system('cls')
                            continue
                        if (b == 0):
                            os.system('cls')
                            break
                        elif (0 < b <= len(st)):
                            os.system('cls')
                            while True:
                                print('\033[4;37;1m' + "Sklep" + '\033[0m\n')
                                print(f'{st[b-1]["desc"]}')
                                print(f"\n  Cena: ",end="")
                                if (self.money >= st[b-1]["worth"]):
                                    print(st[b-1]["worth"])
                                else:
                                    print('\033[38;5;1m' + str(st[b-1]["worth"]) + '\033[0m\n')
                                if (st[b-1]['type'] == 'weapon'):
                                    if (self.weapon != None):
                                        print('\033[1;90;1m' + " Twój oręż:" + '\033[0m')
                                        print(self.weapon['desc'])
                                elif (st[b-1]['type'] == 'armor'):
                                    if (self.armor != None):
                                        print('\033[1;90;1m' + " Twoja zbroja:" + '\033[0m')
                                        print(self.armor['desc'])
                                elif (st[b-1]['type'] == 'neklace'):
                                    if (self.neklace != None):
                                        print('\033[1;90;1m' + " Twój naszyjnik:" + '\033[0m')
                                        print(self.neklace['desc'])
                                elif (st[b-1]['type'] == 'ring'):
                                    if (self.ring1 != None and self.ring2 == None):
                                        print('\033[1;90;1m' + " Twój pierścień:" + '\033[0m')
                                        print(self.ring1['desc'])
                                    elif (self.ring1 == None and self.ring2 != None):
                                        print('\033[1;90;1m' + " Twój pierścień:" + '\033[0m')
                                        print(self.ring2['desc'])     
                                    elif (self.ring1 != None and self.ring2 != None):
                                        print('\033[1;90;1m' + " Twoje pierścienie:" + '\033[0m')
                                        print(self.ring1['desc'])    
                                        print(self.ring2['desc'])   
                                print(f"\n Twoje złoto: {self.money}")
                                if (notEnoughMoney):
                                    print('\033[0;31;5m' + "  Nie masz wystarczającej ilości złota." + '\033[0m')
                                print("\n (1) Kup")
                                print("\n (0) Anuluj")
                                try:
                                    c = int(input("\n> "))
                                except:
                                    os.system('cls')
                                    continue
                                match c:
                                    case 1:
                                        if (self.money >= st[b-1]["worth"]):
                                            os.system('cls')
                                            while True:
                                                print('\033[4;37;1m' + "Sklep" + '\033[0m')
                                                print(f'\n{st[b-1]["desc"]}')
                                                print(f'\n  Cena: {st[b-1]["worth"]}')
                                                print(f"\n Twoje złoto: {self.money}")
                                                print("\nCzy jesteś pewien?\n\n (1) Tak\n (2) Nie")
                                                try:
                                                    d = int(input("\n> "))
                                                except:
                                                    os.system('cls')
                                                    continue
                                                match d:
                                                    case 1:
                                                        self.eq.append(st[b-1])
                                                        self.equipment.append(st[b-1]["name"])
                                                        self.money -= st[b-1]["worth"]
                                                        del st[b-1]
                                                        os.system('cls')
                                                        break
                                                    case 2:
                                                        os.system('cls')
                                                        break
                                                    case _:
                                                        os.system('cls')
                                                        continue
                                        else:
                                            notEnoughMoney = True
                                            os.system('cls')
                                            continue
                                    case 0:
                                        os.system('cls')
                                        break
                                    case _:
                                        os.system('cls')
                                        continue
                                if (d == 1):
                                    break
                        else:
                            os.system('cls')
                            continue
                case 2:
                    os.system('cls')
                    print('\033[4;37;1m' + "Sklep" + '\033[0m')
                    self.showEq(0,1)
                case 0:
                    os.system('cls')
                    break
                case _:
                    os.system('cls')
                    continue

    def calcLevel(self):
        i = 0
        while (self.exp >= 10):
            self.exp -= 10
            self.level += 1
            i += 3
        if (i > 0):
            klasa = 0
            self.hp = self.maxHp
            os.system('cls')
            if (self.pClass == "Warrior"):
                klasa = "Wojownik"
            elif (self.pClass == "Archer"):
                klasa = "Łucznik"
            elif (self.pClass == "Rouge"):
                klasa = "Łotrzyk"
            elif (self.pClass == "Mage"):
                klasa = "Mag"
            while (i > 0):
                print(f'''\033[4;37;1mStatus\033[0m
.---------------------------------------------.   \033[1;32;1mAwansowałeś!\033[0m
|'.-----------------------------------------.'|   Imię: {self.name}            
| |             _,..._  ,.  | //  /  //,'Y  | |   Rasa: {self.species}
| |           ,'   `  `'  l | :  :  :|/  `,'| |   Klasa: {klasa}
| |          /  -"`  : ` _) : /_.:--'"``--._| |   Poziom postaci: {self.level}
| |         ; ,  -  -  ._ ``"",'  .  ' ' ,  | |   Doświadczenie: {self.exp}/10
| |         l _._--j`.`-.---.' ;-  \ : .'  /| |   '''+ f"Postęp: " + '[\033[1;34;1m' + self.progress*"\u25AE" + (5 - self.progress) * " " + '\033[0m]\n' 
f'''| |          `. ,     .  `.`  ; . `-.._.- : | |   Złoto: {self.money}
| |            \ `               `.  `-._/-.| |   Zdrowie: {self.hp}/{self.maxHp}
| |             *`.  ,'`.    ' .   :     ``_| |     
| |                ``   /)  /     /  ,  ,-' | |   Statystyki  
| |                     ;'       :  / ,', . | |    \033[1;37;5m(1)\033[0m Siła: {self.str}  
| |                    / ` : : ,' ,',C,  ,-.| |    \033[1;37;5m(2)\033[0m Witalność: {self.con} 
| |                    ;`; ._ `,'  /|   `-| | |    \033[1;37;5m(3)\033[0m Zręczność: {self.dex} 
| |                   r,/   -.`  ,'  (,   ' | |    \033[1;37;5m(4)\033[0m Inteligencja: {self.int} 
| |                   |-:  '/ .`.   ,:      | |    \033[1;37;5m(5)\033[0m Wiedza: {self.wis} 
| |                   3 -`._  ;| , / /   '  | |    \033[1;37;5m(6)\033[0m Charyzma: {self.cha}  
| |                   ; _,','`-,',','`: '   | |    - Szybkość: {self.speed}
| |                   /.--'  /',','   l: __.| |    
| |                  :    _,',','  ---.``   | |    Punkty do rozdysponowania: {i}
| |                  /_,-' ,','_...___  r`-,| |    
| |             __  ,' _ ,' /         ``  / | |    
| |        _,--' _`'    / ,'``--''" ",', : `| |    
| |    _,-'    ,'  ..`;','-.    ,-'"" /   | | |    
|.'-----------------------------------------'.|    
'---------------------------------------------' ''')
                try:
                    a = int(input("\n> "))
                except:
                    os.system('cls')
                    continue
                match a:
                    case 1:
                        self.str += 1
                        i -= 1
                        os.system('cls')
                    case 2:
                        self.con += 1
                        i -= 1
                        os.system('cls')
                    case 3:
                        self.dex += 1
                        i -= 1
                        os.system('cls')
                    case 4:
                        self.int += 1
                        i -= 1
                        os.system('cls')
                    case 5:
                        self.wis += 1
                        i -= 1
                        os.system('cls')
                    case 6:
                        self.cha += 1
                        i -= 1
                        os.system('cls')
                    case _:
                        os.system('cls')
            self.calcMaxHp()
            self.calcSpeed()
        else:
            return False
            
    def calcMaxHp(self):
        self.maxHp = self.con * 4 + 10
        self.hp = self.maxHp

    def calcSpeed(self):
        self.speed = (self.dex // 3) + 5