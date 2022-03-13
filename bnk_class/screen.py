import bnk_class.funcionality as funcionality


def main_menu():
    print(" WELCOME TO BANKS NETWORK ".center(55, "*"))
    print()
    print(f"Select a bank:")
    print("1 - North Bank", )
    print("2 - West Bank")
    print("3 - East Bank")
    print("4 - South Bank")
    print("\n0 - Quit")


def bank_menu(name):
    print()
    print(f" WELCOME TO {name.upper()} ".center(55, "*"))
    print()
    print(f"Select a option:")
    print("1 - Open Account")
    print("2 - Access Account")
    print("\n9 - Back")


def access_account_menu(name):
    print(f" WELCOME {name.upper()} ".center(55, "*"))
    print()
    print(f"Select a option:")
    print("1 - Account Details")
    print("2 - Deposit")
    print("3 - Statement")
    print("4 - Withdrawal")
    print("\n9 - Back")


def bank_menu_options(bank):
    while True:
        bank_menu(bank.name)
        decision = input("\nOption: ")
        if decision == '1':
            funcionality.open_account(bank)
        elif decision == '2':
            funcionality.access_account(bank)
        elif decision == '9':
            break
        else:
            print("Insert a option valid")
