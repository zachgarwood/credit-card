from credit_card.ledger import Ledger
import unittest


class LedgerTest(unittest.TestCase):
    def test_commands_exist(self):
        for command_name in ['add', 'charge', 'credit']:
            self.assertTrue(hasattr(Ledger, command_name),
                            'Ledger class does not contain ' + command_name)

    def test_add(self):
        ledger = Ledger()
        ledger.add('Test', '12345', 1000)

        self.assertIn('Test', ledger.accounts)
        self.assertDictEqual(
            {'balance': 0, 'limit': 1000, 'number': '12345'},
            ledger.accounts['Test']
        )
