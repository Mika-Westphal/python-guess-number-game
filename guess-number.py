import random

print("Willkommen zum Spiel rate das Spiel!\n")
print("Bitte gebe den Zahlen bereich ein in welchem du Spielen möchtest!\n")

# Die Zahlen Reichweite mit dem Boolean wert ob es eine Zahl ist
numberRange = [0, False, 0, False]

while not numberRange[1] or not numberRange[3]:
    tmpMinimalValue = input("Minimum: ")

    if tmpMinimalValue.isdecimal():
        numberRange[0] = int(tmpMinimalValue)
        numberRange[1] = True

        tmpMaximumValue = input("Maximum: ")

        if tmpMinimalValue.isdecimal():
            numberRange[2] = int(tmpMaximumValue)
            numberRange[3] = True
        else:
            print("Bitte gebe eine Gültige Zahl ein!\n")
    else:
        print("Bitte gebe eine Gültige Zahl ein!\n")

# Hier werden die Spielinformationen gespeichert, wie z.B. die Zahl und die Versuche
# sowie ein Bollean wert zum beenden des Spiels
gameValues = [random.randint(numberRange[0], numberRange[2]), 0, False]

while not gameValues[2]:
    userInput = input("\nBitte gebe deine Zahl ein: ")

    if userInput.isdecimal():
        gameValues[1] = gameValues[1] + 1
        userInputValue = int(userInput)

        if userInputValue == gameValues[0]:
            gameValues[2] = True
        elif userInputValue < gameValues[0]:
            print("Die Zahl ist Größer!\n")
        elif userInputValue > gameValues[0]:
            print("Die Zahl ist Kleiner!\n")
    else:
        print("Bitte gebe eine Gültige Zahl ein!\n")

print("Herzlichen Glückwunsch, du hast die Zahl {} nach {} versuchen erraten!".format(gameValues[0], gameValues[1]))
input()