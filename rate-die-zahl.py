import random, os, sys

linesep = os.linesep

def numberinput(usermessage: str, errormessage: str, oneexecute: bool) -> int:
    while True:
        userinput: str = input(usermessage)
        if userinput.isdecimal():
            return int(userinput)
        else:
            print(errormessage)
            if oneexecute:
                return hex(65535)

def getrange(numberone: int, numbertwo: int) -> list:
    if numberone > numbertwo:
        returnlist = [numbertwo, numberone]
        return returnlist
    elif numberone < numbertwo:
        returnlist = [numberone, numbertwo]
        return returnlist
    else:
        returnlist = [numberone, numbertwo]
        return returnlist

def game():
    print("Willkommen zum Spiel rate die Zahl!{}".format(linesep))
    print("Bitte gebe den Zahlen bereich ein in welchem du Spielen möchtest!{}".format(linesep))

    # Die Zahlen Reichweite mit dem Boolean wert ob es eine Zahl ist
    rangeNumber1: int = numberinput("Minimum: ", "{}Bitte gebe eine Gültige Zahl ein!{}".format(linesep, linesep), False)
    rangeNumber2: int = numberinput("Maximum: ", "{}Bitte gebe eine Gültige Zahl ein!{}".format(linesep, linesep), False)

    numberRange: list = getrange(rangeNumber1, rangeNumber2)

    # Hier werden die Spielinformationen gespeichert, wie z.B. die Zahl und die Versuche
    # sowie ein Boolean wert zum beenden des Spiels
    gameValues: list = [random.randint(numberRange[0], numberRange[1]), 0, False]

    while not gameValues[2]:
        userInput: int = numberinput("{}Bitte gebe deine Zahl ein: ".format(linesep), "{}Bitte gebe eine Gültige Zahl ein!".format(linesep), False)

        gameValues[1] = gameValues[1] + 1

        if userInput == gameValues[0]:
            gameValues[2] = True
        elif userInput < gameValues[0]:
            print("{}Die Zahl ist größer!".format(linesep))
        elif userInput > gameValues[0]:
            print("{}Die Zahl ist kleiner!".format(linesep))

    print("Herzlichen Glückwunsch, du hast die Zahl {} nach {} versuchen erraten!".format(gameValues[0], gameValues[1]))
    input()

while True:
    print("""    ______      _             _ _        ______      _     _ 
    | ___ \    | |           | (_)      |___  /     | |   | |
    | |_/ /__ _| |_ ___    __| |_  ___     / /  __ _| |__ | |
    |    // _` | __/ _ \  / _` | |/ _ \   / /  / _` | '_ \| |
    | |\ \ (_| | ||  __/ | (_| | |  __/ ./ /__| (_| | | | | |
    \_| \_\__,_|\__\___|  \__,_|_|\___| \_____/\__,_|_| |_|_|
    """)

    print("Hauptmenu{}".format(linesep))
    print("1) Spiel starten")
    print("2) Spiel beenden")

    menupunkt: int = numberinput("", "", True)
    if menupunkt == 1:
        game()
    elif menupunkt == 2:
        sys.exit()
