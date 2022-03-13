from bnk_class.bank import Bank
import bnk_class.screen as screen


def banks():
    north = Bank("North Bank", 4123)
    south = Bank("South Bank", 5321)
    east = Bank("East Bank", 6732)
    west = Bank("West Bank", 7231)

    return north, south, east, west


def init():
    north, south, east, west = banks()

    while True:
        screen.main_menu()
        decision = input("\nInsert option: ")

        if decision == '1':
            screen.bank_menu_options(north)

        elif decision == '2':
            screen.bank_menu_options(west)

        elif decision == '3':
            screen.bank_menu_options(east)

        elif decision == '4':
            screen.bank_menu_options(south)

        elif decision == '0':
            break
        else:
            print("Insert a valid option")


if __name__ == "__main__":
    init()
