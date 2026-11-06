import utilities as ut

def main():
    while True:
        try:
            ut.clearScreen()
            userChoice = ut.main_menu("Enter a choice (1-4) from above: ")
            if userChoice == 1:
                ut.clearScreen()
                ut.viewShelterInfo()
                ut.pressEnter()
            elif userChoice == 2:
                print("second test")
            elif userChoice == 3:
                print("third test")
            else:
                print("Thanks for playing!")
                break
        except ValueError:
            print("Enter a number (1-3) from above: ")


if __name__ == "__main__":
    main()