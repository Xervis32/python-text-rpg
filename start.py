import main
import os
from random import randint

while True:
    os.system('cls')
    main.menu()
    while True:
        if (main.r == 0):
            if (main.mainEnc() == False):
                break
            main.r = randint(3,6)
            os.system('cls')
            main.status()
        if (main.j % 4 == 0):
            main.randEnc(1)
        else:
            if(main.randEnc() == False):
                break
        main.j += 1
        main.r -= 1
        main.status()