import subprocess
import unittest


EXPECTED_OUTPUT = """Lisa: $-93
Quincy: error
Tom: $500
"""


class CreditCardTest(unittest.TestCase):
    def test_output(self):
        output = subprocess.check_output(
            ['credit-card', 'test/fixtures/input.txt'],
            universal_newlines=True
        )
        self.assertEqual(EXPECTED_OUTPUT, output)
