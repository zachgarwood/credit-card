class Ledger:
    def __init__(self):
        self.accounts = {}

    def add(self, name, number, limit):
        self.accounts[name] = {'number': number,
                               'limit': int(limit),
                               'balance': 0}

    def charge(self, name, amount):
        amount = int(amount)
        account = self.accounts[name]
        if ((account['balance'] + amount) <= account['limit']):
            account['balance'] += amount

    def credit(self, name, *args):
        print('credit')
