from .ledger import Ledger
import fileinput
import sys


def main():
    ledger = Ledger()
    try:
        for command in fileinput.input():
            name, *args = command.split()
            getattr(ledger, name.lower())(*args)
    except Exception as exception:
        sys.stderr.write(
            'There was an unexpected error: "' + str(exception) + '"!\n'
        )
