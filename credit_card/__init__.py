import fileinput
import sys


def main():
    try:
        for command in fileinput.input():
            name, subject, *args = command.split()
            getattr(sys.modules[__name__], name.lower())(subject, *args)
    except Exception as exception:
        sys.stderr.write("There was an unexpected error: \"" + str(exception) + "\"!\n")


def add(subject, *args):
    print('add')


def charge(subject, *args):
    print('charge')


def credit(subject, *args):
    print('credit')
