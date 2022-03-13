class Bank:
    def __init__(self, name, bank_num):
        self._name = name
        self._bank_num = bank_num
        self._clients = []

    @property
    def name(self):
        return self._name

    @property
    def bank_num(self):
        return self._bank_num

    @property
    def clients(self):
        return self._clients

    def add_clients(self, client):
        try:
            self._clients.append(client)
        except Exception as e:
            print("Error: Client cannot be registered")
            print(e)

    def list_clients(self):
        for client in self.clients:
            print(client.name, client.age, client.account.acc_num)

    def search_client(self, doc_id):
        for client in self.clients:
            if client.doc_id == doc_id:
                return client
