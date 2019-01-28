import random, os, sys

linesep = os.linesep

def execute():
    print("Willkommen zum Spiel rate die Zahl!{}".format(linesep))
    print("Bitte gebe den Zahlen bereich ein in welchem du Spielen möchtest!{}".format(linesep))

    # Die Zahlen Reichweite mit dem Boolean wert ob es eine Zahl ist
    numberRange = [0, False, 0, False]

    while not numberRange[1]:
        tmpMinimalValue = input("Minimum: ")

        if tmpMinimalValue.isdecimal():
            numberRange[0] = int(tmpMinimalValue)
            numberRange[1] = True            
        else:
            print("{}Bitte gebe eine Gültige Zahl ein!{}".format(linesep, linesep))

    while not numberRange[3]:
        tmpMaximumValue = input("Maximum: ")

        if tmpMaximumValue.isdecimal():
            if not int(tmpMaximumValue) < numberRange[0]:
                numberRange[2] = int(tmpMaximumValue)
                numberRange[3] = True
            else:
                print("{}Deine Maximale Zahl darf nicht kleiner sein als die Minimale Zahl!{}".format(linesep, linesep))
        else:
            print("{}Bitte gebe eine Gültige Zahl ein!{}".format(linesep, linesep))

    # Hier werden die Spielinformationen gespeichert, wie z.B. die Zahl und die Versuche
    # sowie ein Boolean wert zum beenden des Spiels
    gameValues = [random.randint(numberRange[0], numberRange[2]), 0, False]

    while not gameValues[2]:
        userInput = input("{}Bitte gebe deine Zahl ein: ".format(linesep))

        if userInput.isdecimal():
            gameValues[1] = gameValues[1] + 1
            userInputValue = int(userInput)

            if userInputValue == gameValues[0]:
                gameValues[2] = True
            elif userInputValue < gameValues[0]:
                print("Die Zahl ist Größer!{}".format(linesep))
            elif userInputValue > gameValues[0]:
                print("Die Zahl ist Kleiner!{}".format(linesep))
        else:
            print("{}Bitte gebe eine Gültige Zahl ein!".format(linesep))

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
    print("1) Spiel Starten")
    print("2) Spiel Beenden")
    
    eingabe = input()
    if eingabe.isdecimal():
        eingabe = int(eingabe)
        if eingabe == 1:
            execute()
        elif eingabe == 2:
            sys.exit()