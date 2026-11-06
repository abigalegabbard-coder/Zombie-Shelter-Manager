from datetime import datetime; import json; import os

def pressEnter():
    print()
    move_on = input("Press enter to continue: ")
    if move_on:
        clearScreen()

def main_menu(prompt):
    print("Zombie Shelter Manager")
    choices = ["View shelter information", "Change a shelter value", "View change log", "Quit"]
    for x, choices in enumerate(choices, start = 1):
        print(f"{x}. {choices}")
    while True:
        try:
            userChoice = int(input(prompt))
            if 1 <= userChoice <= 4:
                return userChoice
        except ValueError:
            print("Enter a number 1-4 from above!")

def viewShelterInfo():
    print("SHELTER INFORMATION")
    print()
    with open("shelter.json", "r") as file:
        data = json.load(file)
    items = "\n".join(f"{k}: {v}" for k, v in data.items())
    print(items)

def clearScreen():
    """Clear the window's console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def changeValueSelect(prompt):
    clearScreen()
    choices = ["Shelter Name", "Leader", "Survivors", "Food", "Water", "Barricade Health", "Radio working"]
    for x, choices in enumerate(choices, start = 1):
        print(f"{x}. {choices}")
    while True:
        try:
            print()
            chooseValue = int(input(prompt))
            if 1 <= chooseValue <= 7:
                return chooseValue
        except ValueError:
            print("Enter a valid num (1-7) from above!")

def changeValue():
    selected = changeValueSelect("Select a num (1-7) from above: ")
    with open("shelter.json", "r") as file:
        data = json.load(file)
    selected_choice = (data[selected-1])
    

def main():
    main_menu("Enter a choice (1-4) from above: ")
    viewShelterInfo()
    changeValue()

if __name__ == "__main__":
    main()