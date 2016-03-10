import credit_card.money as money
import luhn


class Ledger:
    def __init__(self):
        self.accounts = {}

    def add(self, name, number, limit):
        self.accounts[name] = {'is_valid': luhn.verify(number),
                               'limit': money.unformat(limit),
                               'balance': 0}

    def charge(self, name, amount):
        account = self.accounts[name]
        if not account['is_valid']:
            return
        amount = money.unformat(amount)
        if ((account['balance'] + amount) <= account['limit']):
            account['balance'] += amount

    def credit(self, name, amount):
        account = self.accounts[name]
        if not account['is_valid']:
            return
        amount = money.unformat(amount)
        account['balance'] -= amount
