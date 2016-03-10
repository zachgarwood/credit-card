class Ledger:
    def __init__(self):
        self.accounts = {}

    def add(self, subject, number, limit):
        self.accounts[subject] = {'number': number,
                                  'limit': limit,
                                  'balance': 0}

    def charge(self, subject, *args):
        print('charge')

    def credit(self, subject, *args):
        print('credit')
