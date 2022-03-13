from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, acc_num, bank_num, balance=20):
        self._acc_num = acc_num
        self._bank_num = bank_num
        self._balance = balance
        self._acc_name = None

    @property
    def acc_num(self):
        return self._acc_num

    @property
    def bank_num(self):
        return self._bank_num

    @property
    def balance(self):
        return self._balance

    @property
    def acc_name(self):
        return self._acc_name

    @acc_name.setter
    def acc_name(self, name):
        self._acc_name = name

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be numeric")
        self._balance = value

    def deposit(self, value):
        self.balance += value
        info_value = f"Deposited Value: {value}"
        info_balance = f"Balance: {self.balance}"
        self.details("DEPOSIT INFO", info_balance, info_value)

    def details(self, text, text_balance, text_value):
        print()
        print(f"***{text}****")
        print(text_value)
        print(text_balance)
        print()

    def acc_info(self):
        print("****ACCOUNT INFO****")
        print()
        print(self._acc_name)
        print(f"Account Number: {self.acc_num}")
        print(f"Bank Number: {self.bank_num}")
        print(f"Balance: {self.balance}")

    def acc_statement(self):
        pass

    @abstractmethod
    def withdrawal(self, value):
        pass


class SavingAccount(Account):
    def withdrawal(self, value):
        if value > self.balance:
            print("Insufficient Funds")
            return

        self.balance -= value
        info_value = f"Amount Drawn: {value}"
        info_balance = f"Balance: {self.balance}"

        self.details("WITHDRAWAL INFO", info_balance, info_value)

    def acc_info(self):
        self.acc_name = "Saving Account"
        super().acc_info()
        print()


class CurrentAccount(Account):
    def __init__(self, acc_num, bank_num, balance=20, limit=100):
        super().__init__(acc_num, bank_num, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdrawal(self, value):
        if value > (self.limit + self.balance):
            print("Insufficient Funds")
            return
        self.balance -= value

        info_value = f"Amount Drawn: {value}"
        info_balance = f"Balance: {self.balance}"

        if self.balance < 0:
            self.details("WITHDRAWAL INFO", info_balance, info_value)
            print("WARNING: YOU ARE USING LIMIT")
            print(f"Limit Left: {self.limit + self.balance}")
            return

        self.details("WITHDRAWAL INFO", info_balance, info_value)

    def acc_info(self):
        self.acc_name = "Current Account"
        super().acc_info()
        print(f"Limit: {self.limit}")

        if self.balance < 0:
            print(f"Limit Left: {self.limit + self.balance}")

        print()


class Statement:
    def __init__(self, file, mode):
        self.file = open(file, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
