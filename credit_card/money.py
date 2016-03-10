symbol = '$'


def format(amount):
    """Cast amount to a string and prepend a dollar sign"""
    return '{symbol}{amount}'.format(symbol=symbol, amount=amount)


def unformat(amount):
    """Remove the dollar sign from an amount and cast it to an integer."""
    return int(amount.replace(symbol, ''))
