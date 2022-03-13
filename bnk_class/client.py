from bnk_class.account import SavingAccount, CurrentAccount


class Person:
    def __init__(self, name, age, doc_id):
        self._name = name
        self._age = age
        self._doc_id = doc_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def doc_id(self):
        return self._doc_id


class Client(Person):
    def __init__(self, name, age, doc_id):
        super().__init__(name, age, doc_id)
        self._account = None

    @property
    def account(self):
        return self._account

    def bank_account(self, account_type, acc_num, bank_num, balance):
        if account_type == "Saving Account":
            self._account = SavingAccount(acc_num, bank_num, balance)

        elif account_type == "Current Account":
            self._account = CurrentAccount(acc_num, bank_num, balance)
