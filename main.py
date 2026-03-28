import characters as char
from hero import hero
from items import items
import os
from random import randint
from math import ceil
import json

enc3 = 1
j = 1
r = 0
script_dir = os.path.dirname(__file__)

def readMFile(fileName):
    with open(f"{script_dir}/enc/{fileName}", encoding="UTF-8") as f:
                file = f.readline()
                print('\033[4;37;1m' + file + '\033[0m')
                file = f.readlines()
                for line in file:
                    print(line, end="")

def readFile(fileName):
    with open(f"{script_dir}/enc/{fileName}", encoding="UTF-8") as f:
                file = f.readlines()
                for line in file:
                    print(line, end="")

def save():
    while True:
        os.system('cls')
        print('\033[4;37;1m' + "Zapisz grę" + '\033[0m')
        if (os.path.isfile("saves/save1.txt")):
            print("\n (1) Zapis#1")
        else:
            print('\n\033[1;90;1m' + " (1) -" + '\033[0m')
        if (os.path.isfile("saves/save2.txt")):
            print("\n (2) Zapis#2")
        else:
            print('\n\033[1;90;1m' + " (2) -" + '\033[0m')
        if (os.path.isfile("saves/save3.txt")):
            print("\n (3) Zapis#3")
        else:
            print('\n\033[1;90;1m' + " (3) -" + '\033[0m')
        print("\n (0) Powrót")
        try:
            x = int(input("\n> "))
        except:
            continue
        if (x == 0):
            os.system('cls')
            break
        if (os.path.isfile(f"{script_dir}/saves/save{x}.txt")):
            while True:
                os.system('cls')
                print('\033[4;37;1m' + "Zapisz grę" + '\033[0m')
                print("\nCzy chcesz nadpisać zapis?")
                print("\n (1) Tak")
                print(" (2) Nie")
                try:
                    z = int(input("\n> "))
                except:
                    continue
                match z:
                    case 1:
                        with open(f"{script_dir}/saves/save{x}.txt","w", encoding="UTF-8") as f:
                            f.writelines([str(j)+'\n', str(r)+'\n', player.name+'\n', str(player.con)+'\n', str(player.str)+'\n', str(player.dex)+'\n', str(player.int)+'\n', str(player.wis)+'\n', str(player.cha)+'\n', player.pClass+'\n', json.dumps(player.armor, ensure_ascii=False)+'\n', json.dumps(player.weapon, ensure_ascii=False)+'\n', json.dumps(player.neklace, ensure_ascii=False)+'\n', json.dumps(player.ring1, ensure_ascii=False)+'\n', json.dumps(player.ring2, ensure_ascii=False)+'\n', str(player.level)+'\n', str(player.exp)+'\n', str(player.money)+'\n', str(player.progress)+'\n', json.dumps(player.eq, ensure_ascii=False)+'\n', json.dumps(player.equipment, ensure_ascii=False)+'\n', str(char.difficulty)+'\n'])
                            os.system('cls')
                            print('\033[1;37;1m' + "Gra pomyślnie zapisana." + '\033[0m')
                            input("\n (Enter) Kontynuuj.\n\n> ")
                            return True
                    case 2:
                        break
        elif (x == 1 or x == 2 or x == 3):
            with open(f"{script_dir}/saves/save{x}.txt","w", encoding="UTF-8") as f:
                f.writelines([str(j)+'\n', str(r)+'\n', player.name+'\n', str(player.con)+'\n', str(player.str)+'\n', str(player.dex)+'\n', str(player.int)+'\n', str(player.wis)+'\n', str(player.cha)+'\n', player.pClass+'\n', json.dumps(player.armor, ensure_ascii=False)+'\n', json.dumps(player.weapon, ensure_ascii=False)+'\n', json.dumps(player.neklace, ensure_ascii=False)+'\n', json.dumps(player.ring1, ensure_ascii=False)+'\n', json.dumps(player.ring2, ensure_ascii=False)+'\n', str(player.level)+'\n', str(player.exp)+'\n', str(player.money)+'\n', str(player.progress)+'\n', json.dumps(player.eq, ensure_ascii=False)+'\n', json.dumps(player.equipment, ensure_ascii=False)+'\n', str(char.difficulty)+'\n'])
                os.system('cls')
                print('\033[1;37;1m' + "Gra pomyślnie zapisana." + '\033[0m')
                input("\n (Enter) Kontynuuj.\n\n> ")
                return True
        else:
            continue

def load():
    global j,r
    while True:
        os.system('cls')
        print('\033[4;37;1m' + "Wczytaj grę" + '\033[0m')
        if (os.path.isfile("saves/save1.txt")):
            print("\n (1) Zapis#1")
        else:
            print('\n\033[1;90;1m' + " (1) -" + '\033[0m')
        if (os.path.isfile("saves/save2.txt")):
            print("\n (2) Zapis#2")
        else:
            print('\n\033[1;90;1m' + " (2) -" + '\033[0m')
        if (os.path.isfile("saves/save3.txt")):
            print("\n (3) Zapis#3")
        else:
            print('\n\033[1;90;1m' + " (3) -" + '\033[0m')
        print("\n (0) Powrót")
        try:
            x = int(input("\n> "))
        except:
            continue
        if (x == 0):
            os.system('cls')
            return False
        if (os.path.isfile(f"{script_dir}/saves/save{x}.txt")):
            while True:
                os.system('cls')
                print('\033[4;37;1m' + "Wczytaj grę" + '\033[0m')
                print("\nCzy na pewno chcesz wczytać grę?")
                print("\n (1) Tak")
                print(" (2) Nie")
                try:
                    z = int(input("\n> "))
                except:
                    continue
                match z:
                    case 1:
                        with open(f"{script_dir}/saves/save{x}.txt", encoding="UTF-8") as f:
                            data = [line.rstrip('\n') for line in f]
                        char.difficulty = 1
                        player = hero(data[2],"Człowiek",int(data[3]),int(data[4]),int(data[5]),int(data[6]),int(data[7]),int(data[8]),0,0,data[9])
                        player.armor = json.loads(data[10])
                        player.weapon = json.loads(data[11])
                        player.neklace = json.loads(data[12])
                        player.ring1 = json.loads(data[13])
                        player.ring2 = json.loads(data[14])
                        player.level = int(data[15])
                        player.exp = int(data[16])
                        player.money = int(data[17])
                        player.progress = int(data[18])
                        player.eq = json.loads(data[19])
                        player.equipment = json.loads(data[20])
                        player.calcMaxHp()
                        player.calcSpeed()
                        char.difficulty = float(data[21])
                        os.system('cls')
                        print('\033[1;37;1m' + "Gra wczytana pomyślnie." + '\033[0m')
                        input("\n (Enter) Kontynuuj.\n\n> ")
                        return player
                    case 2:
                        break
        else:
            continue

def status():
    player.calcLevel()
    klasa = 0
    os.system('cls')
    if (player.pClass == "Warrior"):
        klasa = "Wojownik"
    elif (player.pClass == "Archer"):
        klasa = "Łucznik"
    elif (player.pClass == "Rouge"):
        klasa = "Łotrzyk"
    elif (player.pClass == "Mage"):
        klasa = "Mag"
    while True:
        print(f'''\033[4;37;1mStatus\033[0m
.---------------------------------------------.   
|'.-----------------------------------------.'|   Imię: {player.name}            
| |             _,..._  ,.  | //  /  //,'Y  | |   Rasa: {player.species}
| |           ,'   `  `'  l | :  :  :|/  `,'| |   Klasa: {klasa}
| |          /  -"`  : ` _) : /_.:--'"``--._| |   Poziom postaci: {player.level}
| |         ; ,  -  -  ._ ``"",'  .  ' ' ,  | |   Doświadczenie: {player.exp}/10
| |         l _._--j`.`-.---.' ;-  \ : .'  /| |   '''+ f"Postęp: " + '[\033[1;34;1m' + player.progress*"\u25AE" + (5 - player.progress) * " " + '\033[0m]\n' 
f'''| |          `. ,     .  `.`  ; . `-.._.- : | |   Złoto: {player.money}
| |            \ `               `.  `-._/-.| |   Zdrowie: {player.hp}/{player.maxHp} 
| |             *`.  ,'`.    ' .   :     ``_| |   
| |                ``   /)  /     /  ,  ,-' | |   Statystyki 
| |                     ;'       :  / ,', . | |    - Siła: {player.str}
| |                    / ` : : ,' ,',C,  ,-.| |    - Witalność: {player.con}
| |                    ;`; ._ `,'  /|   `-| | |    - Zręczność: {player.dex}
| |                   r,/   -.`  ,'  (,   ' | |    - Inteligencja: {player.int}
| |                   |-:  '/ .`.   ,:      | |    - Wiedza: {player.wis}
| |                   3 -`._  ;| , / /   '  | |    - Charyzma: {player.cha}
| |                   ; _,','`-,',','`: '   | |    - Szybkość: {player.speed}
| |                   /.--'  /',','   l: __.| |
| |                  :    _,',','  ---.``   | |    
| |                  /_,-' ,','_...___  r`-,| |    
| |             __  ,' _ ,' /         ``  / | |    
| |        _,--' _`'    / ,'``--''" ",', : `| |    (1) Kontynuuj
| |    _,-'    ,'  ..`;','-.    ,-'"" /   | | |    (2) Ekwipunek
|.'-----------------------------------------'.|    (3) Opcje
'---------------------------------------------' ''')
        try:
            x = int(input("\n> "))
        except:
            os.system('cls')
            continue
        match x:
            case 1:
                os.system('cls')
                return True
            case 2:
                print("")
                player.showEq()
                os.system('cls')
            case 3:
                options()
                os.system('cls')
            case _:
                os.system('cls')
                continue

def options():
    global player
    while True:
        os.system('cls')
        print('\033[4;37;1m' + "Opcje" + '\033[0m')
        print("\n (1) Zapisz grę")
        print(" (2) Wczytaj grę")
        print(" (3) Zmień poziom trudności")
        print(" (4) Wyjdź z gry")
        print("\n (0) Anuluj")
        try:
            x = int(input("\n> "))
        except:
            os.system('cls')
            continue
        match x:
            case 1:
                save()
            case 2:
                player = load()
            case 3:
                os.system('cls')
                while True:
                    print('\033[1;37;1m' + "Wybierz poziom trudności:" + '\033[0m')
                    print("\n (1) Łatwy")
                    print(" (2) Normalny")
                    print(" (3) Trudny")
                    print("\n (0) Anuluj")

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
                            break
                        case _:
                            os.system('cls')
                            continue
            case 4:
                os.system('cls')
                while True:
                    print("Czy jesteś pewien?")
                    print("\n (1) Tak")
                    print(" (2) Nie")
                    try:
                        y = int(input("\n> "))
                    except:
                        os.system('cls')
                        continue
                    match y:
                        case 1:
                            quit()
                        case 2:
                            os.system('cls')
                            break
            case 0:
                return False
            case _:
                os.system('cls')
                continue   

def randEnc(isShop=0):
    if (isShop == 1):
        player.shop()
        return True
    global enc3
    os.system('cls')
    while True:
        enc = randint(1,5)
        # enc = 5
        match enc:
# enc 1
            case 1:
                while True:
                    readMFile("enc1.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        os.system('cls')
                        continue
                    match choice:
                        case 1:
                            readFile("enc1_1.txt")
                            wraith = char.ghost(10, "E1")
                            input("\n\t(Enter) Atakuj.\n\n>")
                            os.system('cls')
                            if (player.fight(1, 16, wraith) == False):
                                return False
                            # input("\n\t(Enter) Kontynuuj.\n\n>")
                            return True
                        case 2:
                            readFile("enc1_2.txt")
                            wraith = char.ghost(10, "E1")
                            input("\n\t(Enter) Atakuj.\n\n>")
                            os.system('cls')
                            if (player.fight(1, 16, wraith) == False):
                                return False
                            # input("\n\t(Enter) Kontynuuj.\n\n>")
                            return True
                        case 3:
                            readFile("enc1_3.txt")
                            player.exp += 1
                            print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                            input("\n\t(Enter) Kontynuuj.\n\n>")
                            return True
                        case _:
                            os.system('cls')
                            continue
# enc 2            
            case 2:
                while True:
                    readMFile("enc2.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        os.system('cls')
                        continue
                    match choice:
                        case 1:
                            wolf = char.greyWolf(15,"E1")
                            os.system('cls')
                            if (player.fight(1, 30, wolf) == False):
                                return False
                            return True
                            
                        case 2:
                            if (player.cha/22*100 >= randint(1,100)):
                                readFile("enc2_2s.txt")
                                player.take("warriorSword")
                                player.exp += 1
                                print('\033[1;32;1m' + "\n + Miecz Wojownika" + '\033[0m')
                                print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                input("\n\t(Enter) Kontynuuj.\n\n>")
                                return True
                            else:
                                wolf = char.greyWolf(3,"E1")
                                readFile("enc2_2f.txt")
                                input("\n\t(Enter) Atakuj.\n\n>")
                                os.system('cls')
                                if (player.fight(1, 30, wolf) == False):
                                    return False
                                return True
                        case 3:
                            if (player.dex/15*100+10 >= randint(1,100)):
                                readFile("enc2_3s.txt")
                                player.exp += 1
                                print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                input("\n\t(Enter) Kontynuuj.\n\n>")
                                return True
                            else:
                                wolf = char.greyWolf(3,"E1")
                                readFile("enc2_3f.txt")
                                input("\n\t(Enter) Atakuj.\n\n>")
                                os.system('cls')
                                if (player.fight(1, 30, wolf) == False):
                                    return False
                                return True
                        case _:
                            os.system('cls')
                            continue
# enc 3            
            case 3:
                if (enc3 == 1):
                    while True:
                        readMFile("enc3.txt")
                        try:
                            choice = int(input("\n> "))
                            print("")
                        except:
                            os.system('cls')
                            continue
                        match choice:
                            case 1:
                                if (player.str/20*100+10 >= randint(1,100)):
                                    readFile("enc3_1s.txt")
                                    enc3 = 2
                                    player.exp += 1
                                    print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                    input("\n\t(Enter) Kontynuuj.\n\n>")
                                    return True
                                else:
                                    readFile("enc3_1f.txt")
                                    player.exp += 1
                                    print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                    input("\n\t(Enter) Kontynuuj.\n\n>")
                                    return True
                            case 2:
                                readFile("enc3_1f.txt")
                                loss = ceil(0.05 * player.money)
                                print('\033[1;31;1m' + f"\n - {loss} złota" + '\033[0m')
                                player.money -= loss
                                input("\n\t(Enter) Kontynuuj.\n\n>")
                                return True
                            case 3:
                                if (player.dex/18*100+10 >= randint(1,100)):
                                    readFile("enc3_3s.txt")
                                    player.exp += 1
                                    print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                    input("\n\t(Enter) Kontynuuj.\n\n>")
                                    return True
                                else:
                                    readFile("enc3_3f.txt")
                                    oldMan = char.oldMan(14, "E1")
                                    input("\n\t(Enter) Atakuj.\n\n>")
                                    os.system('cls')
                                    if (player.fight(1, 30, oldMan) == False):
                                        return False
                                    return True
                            case _:
                                os.system('cls')
                                continue
                elif (enc3 == 2):
                    enc3 = 3
                    while True:
                        readMFile("enc3.1.txt")
                        try:
                            choice = int(input("\n> "))
                            print("")
                        except:
                            os.system('cls')
                            continue
                        match choice:
                            case 1:
                                readFile("enc3.1_1.txt")
                                try:
                                    choice = int(input("\n> "))
                                    print("")
                                except:
                                    os.system('cls')
                                    continue
                                match choice:
                                    case 1:
                                        if (player.int/25*100+10 >= randint(1,100)):
                                            readFile("enc3.1_1_1s.txt")
                                            player.money += 75
                                            player.take("ancientDagger")
                                            print('\033[1;32;1m' + "\n + 75 złota" + '\033[0m')
                                            print('\033[1;32;1m' + " + Starożytny Sztylet" + '\033[0m')
                                            print('\033[1;32;1m' + " + 3 doświadczenia" + '\033[0m')
                                            input("\n\t(Enter) Kontynuuj.\n\n>")
                                            return True
                                        else:
                                            readFile("enc3.1_1_1f.txt")
                                            gargoyle = char.gargoyle(7,"E1")
                                            input("\n\t(Enter) Atakuj.\n\n>")
                                            if (player.fight(1, 20, gargoyle) == False):
                                                return False
                                            print("Po pokonaniu gargulca okazuje się, że mechanizm jest zbyt trudny do otwarcia. Z ciężkim sercem opuszczasz podziemia, zostawiając tajemnicę nienaruszoną.")
                                            input("\n\t(Enter) Kontynuuj.\n\n>")
                                            return True
                                    case 2:
                                        if (player.str/30*100+10 >= randint(1,100)):
                                            readFile("enc3.1_1_2s.txt")
                                            player.money += 75
                                            player.take("ancientDagger")
                                            print('\033[1;32;1m' + "\n + 75 złota" + '\033[0m')
                                            print('\033[1;32;1m' + " + Starożytny Sztylet" + '\033[0m')
                                            print('\033[1;32;1m' + " + 3 doświadczenia" + '\033[0m')
                                            input("\n\t(Enter) Kontynuuj.\n\n>")
                                            return True
                                        else:
                                            readFile("enc3.1_1_2f.txt")
                                            player.exp += 1
                                            print('\n\033[1;32;1m' + " + 1 doświadczenia" + '\033[0m')
                                            input("\n\t(Enter) Kontynuuj.\n\n>")
                                            return True
                                    case _:
                                        os.system('cls')
                                        continue
                            case 2:
                                if (player.wis/15*100+10 >= randint(1,100)):
                                    readFile("enc3.1_2s.txt")
                                    player.money += 15
                                    player.exp += 1
                                    player.take("antiMagicNeklace")
                                    print('\033[1;32;1m' + "\n + 15 złota" + '\033[0m')
                                    print('\033[1;32;1m' + " + Naszyjnik anty-magiczny" + '\033[0m')
                                    print('\033[1;32;1m' + " + 1 doświadczenia" + '\033[0m')
                                    input("\n\t(Enter) Kontynuuj.\n\n>")
                                    return True
                                else:
                                    readFile("enc3.1_2f.txt")
                                    player.exp += 1
                                    print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                    input("\n\t(Enter) Kontynuuj.\n\n>")
                                    return True
                            case 3:
                                readFile("enc3.1_3.txt")
                                player.exp += 1
                                print('\033[1;32;1m' + "\n + 1 doświadczenia" + '\033[0m')
                                input("\n\t(Enter) Kontynuuj.\n\n>")
                                return True
                            case _:
                                os.system('cls')
                                continue
                else:
                    continue
# enc 4            
            case 4:
                while True:
                    readMFile("enc4.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        os.system('cls')
                        continue
                    match choice:
                        case 1:
                            readFile("enc4_1.txt")
                            missHp = player.maxHp - player.hp
                            player.exp += 1
                            print("\n\033[1;32;1m" + f" + {missHp} HP" + '\033[0m')
                            print('\033[1;32;1m' + " + 1 doświadczenia" + '\033[0m')
                            player.hp += missHp
                            input("\n\t(Enter) Kontynuuj.\n\n>")
                            return True
                        case 2:
                            readFile("enc4_2.txt")
                            player.exp += 1
                            print('\n\033[1;32;1m' + " + 1 doświadczenia" + '\033[0m')
                            input("\n\t(Enter) Kontynuuj.\n\n>")
                            return True
                        case _:
                            os.system('cls')
                            continue
# enc 5            
            case 5:
                while True:
                    readMFile("enc5.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        os.system('cls')
                        continue
                    match choice:
                        case 1:
                            readFile("enc5_1.txt")
                            bandit1 = char.banditWarrior(12,"E1")
                            bandit2 = char.banditArcher(16,"E2")
                            input("\n\t(Enter) Atakuj.\n\n>")
                            os.system('cls')
                            if (player.fight(1, 34, bandit1, bandit2) == False):
                                return False
                            os.system('cls')
                            print(" Nie chcesz się wtrącać w sprawy, które mogą przynieść kłopoty. Przyspieszasz kroku, zostawiając tajemniczych\n nieznajomych za sobą. Po chwili ich sylwetki znikają w ciemności, a ty kontynuujesz swoją podróż.")
                            return True
                        case 2:
                            readFile("enc5_2.txt")
                            player.exp += 1
                            print('\n\033[1;32;1m' + " + 1 doświadczenia" + '\033[0m')
                            input("\n\t(Enter) Kontynuuj.\n\n>")
                            return True
                        case _:
                            os.system('cls')
                            continue

def mainEnc():
    match player.progress:
        case 0:
            os.system('cls')
            readMFile("menc1.txt")
            player.progress += 1
            input("\n\t (Enter) Kontynuuj.\n\n> ")  
            return True      
        case 1:
            while True:
                    os.system('cls')
                    readMFile("menc2.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        continue
                    match choice:
                        case 1:
                            goblinW = char.goblinWarrior(35,"E1")
                            goblinA = char.goblinArcher(60,"E2")
                            goblinS = char.goblinShaman(55,"E3")
                            chGoblin = char.goblinChieftain(72,"E4")
                            if (player.fight(15,95,goblinW,goblinA,goblinS,chGoblin) == False):
                                return False
                            while True:
                                readFile("menc2_1.txt")
                                try:
                                    choice = int(input("\n> "))
                                    print("")
                                except:
                                    os.system('cls')
                                    continue
                                match choice:
                                    case 1:
                                        readFile("menc2_1_1.txt")
                                        player.progress += 1
                                        input("\n\t (Enter) Kontynuuj.\n\n> ")
                                        return True
                                    case 2:
                                        readFile("menc2_1_2.txt")
                                        player.progress += 1
                                        input("\n\t (Enter) Kontynuuj.\n\n> ")
                                        return True
                        case 2:
                            if (player.dex/15*100 >= randint(1,100)):
                                while True:
                                    readFile("menc2_2s.txt")
                                    try:
                                        choice = int(input("\n> "))
                                        print("")
                                    except:
                                        os.system('cls')
                                        continue
                                    match choice:
                                        case 1:
                                            readFile("menc2_2_1.txt")
                                            player.progress += 1
                                            input("\n\t (Enter) Kontynuuj.\n\n> ")
                                            return True
                                        case 2:
                                            readFile("menc2_2_2.txt")
                                            input("\n\t (Enter) Atakuj.\n\n> ")
                                            goblinW = char.goblinWarrior(85,"E1")
                                            goblinA = char.goblinArcher(70,"E2")
                                            goblinS = char.goblinShaman(65,"E3")
                                            if (player.fight(90,95,goblinW,goblinA,goblinS) == False):
                                                return False
                                            readFile("menc2_2_2s.txt")
                                            player.progress += 1
                                            input("\n\t (Enter) Kontynuuj.\n\n> ")
                                            return True
                            else:
                                readFile("menc2_2f.txt")
                                input("\n\t (Enter) Atakuj.\n\n> ")
                                goblinW = char.goblinWarrior(35,"E1")
                                goblinA = char.goblinArcher(60,"E2")
                                goblinS = char.goblinShaman(55,"E3")
                                chGoblin = char.goblinChieftain(72,"E4")
                                if (player.fight(25,95,goblinW,goblinA,goblinS,chGoblin) == False):
                                    return False
                                while True:
                                    readFile("menc2_1.txt")
                                    try:
                                        choice = int(input("\n> "))
                                        print("")
                                    except:
                                        os.system('cls')
                                        continue
                                    match choice:
                                        case 1:
                                            readFile("menc2_1_1.txt")
                                            player.progress += 1
                                            input("\n\t (Enter) Kontynuuj.\n\n> ")
                                            return True
                                        case 2:
                                            readFile("menc2_1_2.txt")
                                            player.progress += 1
                                            input("\n\t (Enter) Kontynuuj.\n\n> ")
                                            return True
                                

        case 2:
            while True:
                    os.system('cls')
                    readMFile("menc3.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        continue
                    match choice:
                        case 1:
                            if (player.int/100000*100 >= randint(1,100)):
                                readFile("menc3_1s.txt")
                                match player.pClass:
                                    case "Warrior":
                                        print('\n\033[1;32;1m' + "+ Pierścień siły" + '\033[0m')
                                        player.take("strRing")
                                    case "Archer":
                                        print('\n\033[1;32;1m' + "+ Pierścień zwinnności" + '\033[0m')
                                        player.take("dexRing")
                                    case "Rouge":
                                        print('\n\033[1;32;1m' + "+ Pierścień zwinnności" + '\033[0m')
                                        player.take("dexRing")
                                    case "Mage": 
                                        print('\n\033[1;32;1m' + "+ Pierścień inteligencji" + '\033[0m')
                                        player.take("intRing")
                                input("\n\t (Enter) Kontynuuj.\n\n> ")
                                player.progress += 1
                                return True
                            else:
                                readFile("menc3_1f.txt")
                                input("\n\t (Enter) Kontynuuj.\n\n> ")
                                player.progress += 1
                                return True
                        case 2:
                            readFile("menc3_2.txt")
                            input("\n\t (Enter) Kontynuuj.\n\n> ")
                            player.progress += 1
                            return True
        case 3:
            while True:
                    os.system('cls')
                    readMFile("menc4.txt")
                    try:
                        choice = int(input("\n> "))
                        print("")
                    except:
                        continue
                    match choice:
                        case 1:
                            if (player.dex/15*100 >= randint(1,100)):
                                readFile("menc4_1s.txt")
                                input("\n\t (Enter) Kontynuuj.\n\n> ")
                                player.progress += 1
                                return True
                            else:
                                readFile("menc4_1f.txt")
                                guard1 = char.banditWarrior(10,"E1","Człowiek",6,8,6,3,5,1,1)
                                guard2 = char.banditWarrior(13,"E2","Człowiek",7,8,6,3,5,1,1)                            
                                input("\n\t (Enter) Atakuj.\n\n> ")
                                if (player.fight(3,20,guard1,guard2) == False):
                                        return False
                                readFile("menc4_2s.txt")
                                input("\n\t (Enter) Kontynuuj.\n\n> ")
                                player.progress += 1
                                return True
                        case 2:
                            readFile("menc4_2.txt")
                            guard1 = char.banditWarrior(10,"E1","Człowiek",6,8,6,3,5,1,1)
                            guard2 = char.banditWarrior(13,"E2","Człowiek",7,8,6,3,5,1,1)                           
                            input("\n\t (Enter) Atakuj.\n\n> ")
                            if (player.fight(3,30,guard1,guard2) == False):
                                    return False
                            readFile("menc4_2s.txt")
                            input("\n\t (Enter) Kontynuuj.\n\n> ")
                            player.progress += 1
                            return True
        case 4:
            while True:
                    os.system('cls')
                    readMFile("menc5.txt")
                    dragon = char.dragon(49,"E1")                            
                    input("\n\t (Enter) Atakuj.\n\n> ")
                    if (player.fight(2,50,dragon) == False):
                            return False
                    readFile("menc5s.txt")
                    input("\n\t (Enter) KONIEC.\n\n> ")
                    exit()

def menu():
    global player, r, j, enc3
    enc3 = 1
    r = 0
    j = 1
    while True:
        os.system('cls')
        print('\033[4;37;1m' + "Menu główne" + '\033[0m')
        print("\n (1) Nowa gra")
        print(" (2) Wczytaj grę")
        print(" (3) Wyjście")
        try:
            x = int(input("\n> "))
        except:
            os.system('cls')
            continue
        match x:
            case 1:
                os.system('cls')
                player = hero()
                if (player.start() == False):
                    continue
                break
            case 2:
                player = load()
                if (player == False):
                    continue
                status()
                break
            case 3:
                while True:
                    os.system('cls')
                    print("Czy na pewno chcesz wyjsć?")
                    print("\n\t(1) Tak")
                    print("\t(2) Nie")
                    try:
                        z = int(input("\n> "))
                    except:
                        continue
                    match z:
                        case 1:
                            exit()
                        case 2:
                            os.system('cls')
                            break