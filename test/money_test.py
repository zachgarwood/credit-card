from credit_card import money
import unittest


class MoneyTest(unittest.TestCase):
    def test_format(self):
        self.assertEquals('$1000', money.format(1000))
        self.assertEquals('$-1000', money.format(-1000))

    def test_unformat(self):
        amount = money.unformat('$1000')
        self.assertIsInstance(amount, int)
        self.assertEqual(1000, amount)
