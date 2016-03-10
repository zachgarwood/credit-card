class Ledger:
    def __init__(self):
        self.accounts = {}

    def add(self, name, number, limit):
        self.accounts[name] = {'number': number,
                               'limit': unformat_amount(limit),
                               'balance': 0}

    def charge(self, name, amount):
        amount = unformat_amount(amount)
        account = self.accounts[name]
        if ((account['balance'] + amount) <= account['limit']):
            account['balance'] += amount

    def credit(self, name, amount):
        amount = unformat_amount(amount)
        account = self.accounts[name]
        account['balance'] -= amount


def unformat_amount(amount):
    return int(amount.replace('$', ''))
