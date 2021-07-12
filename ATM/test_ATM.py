from unittest import TestCase
from ATM import ATM

class TestATM(TestCase):

    def test_configurations_for_withdraw(self):
        bills = [100, 50, 20, 10]
        bill_amounts = [10, 10, 10, 10]
        initial_variation = [0] * 4
        withdraw_amount = 300
        atm = ATM()
        result = atm.solutions(bills, bill_amounts, initial_variation, withdraw_amount, 0)
        assert([2, 2, 0, 0] in result)
        assert([1, 3, 2, 1] in result)

