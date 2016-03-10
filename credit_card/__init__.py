from .ledger import Ledger, format_amount
import fileinput
import sys


def main():
    ledger = Ledger()

    # Execute commands
    for command in fileinput.input():
        try:
            name, *args = command.split()
            getattr(ledger, name.lower())(*args)
        except Exception as exception:
            sys.stderr.write(
                'There was an unexpected error: "' + str(exception) + '"!\n'
            )

    # Display summary
    for account in sorted(ledger.accounts.items()):
        name = account[0]
        data = account[1]
        print(name, format_amount(data['balance']))
