from credit_card.ledger import Ledger
import luhn
import unittest


class LedgerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_account_number = luhn.append('12345')

    def setUp(self):
        self.ledger = Ledger()

    def test_commands_exist(self):
        for command_name in ['add', 'charge', 'credit']:
            self.assertTrue(hasattr(Ledger, command_name),
                            'Ledger class does not contain ' + command_name)

    def test_add(self):
        self.ledger.add('Test', self.valid_account_number, '$1000')
        self.assertIn('Test', self.ledger.accounts)
        self.assertDictEqual(
            {'balance': 0, 'limit': 1000, 'is_valid': True},
            self.ledger.accounts['Test'],
            'The limit or number validation was not set and/or '
            'initialized to 0'
        )

        self.ledger.add('Invalid account', '12345', '$0')
        self.assertFalse(self.ledger.accounts['Invalid account']['is_valid'])

    def test_charge(self):
        self.ledger.add('Test', self.valid_account_number, '$1000')
        self.ledger.charge('Test', '$500')
        self.assertEqual(500,
                         self.ledger.accounts['Test']['balance'],
                         'The account balance was not increased')

        self.ledger.charge('Test', '$501')
        self.assertNotEqual(1001,
                            self.ledger.accounts['Test']['balance'],
                            'The account balance increased beyond the limit')

    def test_credit(self):
        self.ledger.add('Test', self.valid_account_number, '$1000')
        self.ledger.charge('Test', '$500')
        self.ledger.credit('Test', '$100')
        self.assertEqual(400,  # 500 - 100
                         self.ledger.accounts['Test']['balance'],
                         'The account balance was not decreased')

        self.ledger.credit('Test', '$401')
        self.assertEqual(-1,
                         self.ledger.accounts['Test']['balance'],
                         'The account balance did not go into the negative')
