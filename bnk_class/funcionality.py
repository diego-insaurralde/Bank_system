import random
from bnk_class.client import Client
import bnk_class.screen as screen


def open_account(bank):
    print()
    print(" ACCOUNT OPENING ".center(55, "*"))
    print()
    account_type = define_account_type()
    print()
    print(f"Account Type: {account_type}")
    print()
    name = input("Insert your complete name: ")
    age = input("Insert your age: ")
    doc_id = input("Insert your ID Doc: ")

    while True:
        balance = input("Insert a value to deposit (MIN: 20$): ")
        try:
            balance = float(balance)
        except ValueError as e:
            print("Insert a value valid")
            continue

        if balance >= 20:
            break
        else:
            print("Deposit must be higher than 20$")

    client = Client(name, age, doc_id)
    acc_num = random.randrange(1000, 5000)

    while acc_num in [cli.account.acc_num for cli in bank.clients]:
        acc_num = random.randrange(1000, 5000)

    client.bank_account(account_type, acc_num, bank.bank_num, balance)
    bank.add_clients(client)

    print("\nAccount Created\n")
    client.account.acc_info()
    input("PRESS ANY BUTTON TO RETURN")
    return


def define_account_type():
    while True:
        print("Select your type account:")
        print("1 - Current Account")
        print("2 - Saving Account")

        decision = input("\nOption: ")
        if decision == '1':
            account_type = "Current Account"
            break
        elif decision == '2':
            account_type = "Saving Account"
            break
        else:
            print("Insert a option valid")
            input("PRESS ANY BUTTON TO CONTINUE")
            continue
    return account_type


def access_account(bank):
    print()
    print(" ACCOUNT ACCESS ".center(55, "*"))
    print()
    id_doc = input("Insert your ID Doc: ")
    bank_num = input("Insert your Bank Number: ")
    acc_num = input("Insert your Account Number: ")

    validation1 = acc_num in [str(cli.account.acc_num) for cli in bank.clients]
    validation2 = bank_num in [str(cli.account.bank_num) for cli in bank.clients]
    validation3 = id_doc in [cli.doc_id for cli in bank.clients]

    if validation1 and validation2 and validation3:
        print("\nAllowed Access")
        client = bank.search_client(id_doc)

        access_account_options(client)
    else:
        print("\nDenied Access")
        return

def access_account_options(client):
    while True:
        print()
        screen.access_account_menu(client.name)
        decision = input("\noption: ")

        if decision == '1':
            print()
            client.account.acc_info()
            input("PRESS ANY BUTTON TO CONTINUE")
        elif decision == '2':
            print()
            print("DEPOSIT".center(55,'*'))
            print()
            while True:
                try:
                    value = float(input("Please, insert a value to deposit: "))
                except ValueError:
                    print("Insert a numeric value")
                    input("\nPRESS ANY BUTTON TO CONTINUE")
                else:
                    break

            client.account.deposit(value)
            input("PRESS ANY BUTTON TO CONTINUE")
        elif decision == '3':
            pass
        elif decision == '4':
            print()
            print("WITHDRAWAL".center(55, '*'))
            print()
            while True:
                try:
                    value = float(input("Please, insert a value to withdrawal: "))
                except ValueError:
                    print("Insert a numeric value")
                    input("PRESS ANY BUTTON TO CONTINUE")
                else:
                    break

            client.account.withdrawal(value)
            input("\nPRESS ANY BUTTON TO CONTINUE")
        elif decision == '9':
            break
        else:
            print("Please, insert a valid value")
            input("\nPRESS ANY BUTTON TO CONTINUE")