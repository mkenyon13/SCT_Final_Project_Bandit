"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

__author__ = "Matt Kenyon"
__version__ = "1.1.0"

from unittest import TestCase
from bank_account.bank_account import BankAccount

class BankAccount_tests(TestCase):
    """Used to contain the tests for the BankAccount class."""

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        account_number = 123456
        client_number = 314159
        balance = 500.50

        self.bank_account = BankAccount(account_number, client_number, balance)

    # __init__ tests
    def test_init_valid_parameters(self):
        self.assertEqual(123456, self.bank_account._BankAccount__account_number)
        self.assertEqual(314159, self.bank_account._BankAccount__client_number)
        self.assertEqual(500.50, self.bank_account._BankAccount__balance)

    def test_init_invalid_balance(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = "invalid"

        # Act
        bank_account = BankAccount(account_number, client_number, balance)

        # Assert
        expected = 0.0
        actual = bank_account.balance
        self.assertEqual(expected, actual)

    def test_init_invalid_account_number(self):
        # Arrange
        account_number = "invalid"
        client_number = 314159
        balance = 500.50

        # Act 
        with self.assertRaises(ValueError) as context:
            bank_account = BankAccount(account_number, client_number, balance)

        # Assert 
        expected = "Account Number must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_init_invalid_client_number(self):
        # Arrange
        account_number = 123456
        client_number = "invalid"
        balance = 500.50

        # Act
        with self.assertRaises(ValueError) as context:
            bank_account = BankAccount(account_number, client_number, balance)

        # Assert
        expected = "Client Number must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual) 

    # Property Method Tests
    def test_account_number_returns_correct_state(self):
        # Act
        actual = self.bank_account.account_number
        expected = 123456

        # Assert
        self.assertEqual(expected, actual)

    def test_client_number_returns_correct_state(self):
        # Act
        actual = self.bank_account.client_number
        expected = 314159

        # Assert
        self.assertEqual(expected, actual)

    def test_balance_returns_correct_state(self):
        # Act
        actual = self.bank_account.balance
        expected = 500.50

        # Assert
        self.assertEqual(expected, actual)

    # Update Balance Tests
    def test_update_balance_positive_amount(self):
        # Act
        self.bank_account.update_balance(100.50)

        # Assert
        expected = 601.0
        actual = self.bank_account.balance
        self.assertEqual(expected, actual)

    def test_update_balance_negative_amount(self):
        # Act
        self.bank_account.update_balance(-100.50)

        # Assert 
        expected = 400.0
        actual = self.bank_account.balance
        self.assertEqual(expected, actual)

    def test_update_balance_invalid_amount(self):
        # Arrange
        amount = "invalid"
        print(type(amount))
        # Act
        with self.assertRaises(ValueError) as context:
            self.bank_account.update_balance(amount)
            print(type(amount+"After the assertRaises"))

        # Assert
        expected = "Amount must be a numeric value."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    # Deposit Tests
    def test_deposit_valid_amount(self):
        # Arrange
        amount = 100.50

        # Act
        self.bank_account.deposit(amount)

        # Assert
        expected = 601.0
        actual = self.bank_account.balance
        self.assertEqual(expected, actual)

    def test_deposit_negative_amount(self):
        # Arrange
        amount = -100.50
        
        # Act
        with self.assertRaises(ValueError) as context:
            self.bank_account.deposit(amount)

        # Assert
        expected = "Deposit amount: $-100.50 must be be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_deposit_invalid_amount(self):
        # Arrange
        amount = "invalid"

        # Act
        with self.assertRaises(ValueError) as context:
            self.bank_account.deposit(amount)

        # Assert
        expected = "Deposit amount: invalid must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_valid_amount(self):
        # Arrange
        amount = 100.50

        # Act
        self.bank_account.withdraw(amount)

        # Assert
        expected = 400.0
        actual = self.bank_account.balance
        self.assertEqual(expected, actual)

    def test_withdraw_invalid_amount(self):
        # Arrange
        amount = "invalid"
        print(type(amount))
        
        # Act
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(amount)

        # Assert
        expected = "Withdrawal amount: invalid must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_negative_amount_raises_exception(self):
        # Arrange
        amount = -100.50

        # Act
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(amount)

        # Assert
        expected = "Withdrawal amount: $-100.50 must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_amount_exceeds_balance_raises_exception(self):
        # Arrange
        amount = 600.50

        # Act
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(amount)

        # Assert
        expected = "Withdrawal amount: $600.50 must not exceed balance."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_str_method(self):
        # Act
        actual = self.bank_account.__str__()

        # Assert
        expected = "Account Number: 123456 Balance: $500.50"
        self.assertEqual(expected, actual)
        