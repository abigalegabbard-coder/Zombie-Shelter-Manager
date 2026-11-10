from datetime import datetime; import json; import os

def pressEnter():
    """Makes the user have to press enter to move on"""
    print()
    move_on = input("Press enter to continue: ")
    if move_on:
        clearScreen()

def main_menu(prompt):
    """Displays the main menu with all of the choices"""
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
    """Displays the shelter's information"""
    print("SHELTER INFORMATION")
    print("-------------------")
    with open("shelter.json", "r") as file:
        data = json.load(file)
    items = "\n".join(f"{k}: {v}" for k, v in data.items())
    print(items)

def clearScreen():
    """Clear the window's console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def changeValueSelect(prompt):
    """Grabs the user's input on what section they want to change"""
    clearScreen()
    choices = ["Shelter Name", "Leader","Survivors", "Food", "Water", "Barricade Health", "Radio working"]
    for x, choice in enumerate(choices, start=1):
        print(f"{x}. {choice}")
    while True:
        try:
            print()
            chooseValue = int(input(prompt))
            if 1 <= chooseValue <= 7:
                return chooseValue
            else:
                print("Enter a valid num (1-7) from above!")
        except ValueError:
            print("Enter a valid num (1-7) from above!")

def log_file(change, edited, original):
    """Adds the user's changes to a shelter.log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} | {edited} changed from {original} to {change}"
    with open("shelter.log", "a", encoding="utf-8") as file:
        file.write(entry + "\n")

def getNewValue(prompt):
    """Makes sure the user's input is compatable with the choice chosen"""
    while True:
        value = input("Enter the new value: ")
        if prompt in ["shelter_name", "leader"]:
            if value.strip():
                return value.strip()
            print("This field cannot be empty!")
        elif prompt in ["survivors", "food", "water", "barricade_health"]:
            try:
                value = int(value)
                if value < 0 or (prompt == "barricade_health" and value > 100):
                    print("Enter a valid number!")
                    continue
                return value
            except ValueError:
                print("Please enter a whole number!")
        elif prompt == "radio_working":
            if value.lower() in ["yes", "no"]:
                return value.lower() == "yes"
            print("Enter yes or no!")

def changeValue():
    """Updates the value"""
    keys = ["shelter_name", "leader", "survivors", "food", "water", "barricade_health", "radio_working"]
    selected = changeValueSelect("Select a num (1-7) from above: ")
    key = keys[selected - 1]
    with open("shelter.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    original = data[key]
    print(f"Current {key}: {original}")
    new_value = getNewValue(key)
    if new_value == original:
        print("Nothing changed!")
        return
    data[key] = new_value
    with open("shelter.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    log_file(new_value, key, original)
    print("Shelter data saved. Change recorded!")

def viewLog():
    """Let's the user view the changes"""
    try: 
        with open("shelter.log", "r", encoding="utf-8") as file: 
            journal_text = file.read() 
        if journal_text.strip(): 
            print(journal_text) 
        else: 
            print("The reading journal is empty.") 
    except FileNotFoundError: 
        print("No reading journal entries have been saved yet.")

def returnJSON():
    """Returns the 'shelter.json' back to what it was before"""
    stuff = {
        "shelter_name": "Last Hope",
        "leader": "Alex",
        "survivors": 8,
        "food": 40,
        "water": 30,
        "barricade_health": 75,
        "radio_working": True
    }
    with open("shelter.json", "w") as file:
        json.dump(stuff, file, indent=4)

def clearLog():
    """Get's rid of the shelter.log file"""
    file_name = "shelter.log"
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        return

def main():
    main_menu("Enter a choice (1-4) from above: ")
    viewShelterInfo()
    changeValue()
    viewLog()
    returnJSON()
    clearLog()

if __name__ == "__main__":
    main()