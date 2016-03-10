Credit Card
===============
# Installation
*Credit Card* is known to run on Python>=3.4. It may not run on older versions.

## Set up virtual environment
```bash
git clone git@github.com:zachgarwood/credit-card.git credit-card
virtualenv --python=python3 credit-card
cd credit-card 
source bin/activate
```

## Installing dev requirements
```bash
python setup.py develop
pip install --requirement dev-requirements.txt
```

## Running tests
```bash
tox
```

# Usage
```bash
credit-card [test/fixtures/input.txt] 
```

*Credit Card* can read commands from one or more files or stdin if no files are
provided. When reading from stdin, you must press `Ctrl-D` twice to flush the
buffer and receive the summary.

# Design
The code is broken up into three components.

## `credit_card.main()` script
Receives, parses, and dispatches the incoming commands to the ledger, outputs
a summary from the ledger's account data.

## `credit_card.ledger` module
Executes one of the three commands and manages the state of the user accounts. 

## `credit_card.money` module
Handles the formatting of money values.

# Exercise Review
I understood the requirements and I believe I accounted for all of them. I
managed to get pretty good test coverage.
