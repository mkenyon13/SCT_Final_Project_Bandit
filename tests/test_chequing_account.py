"""
Description: Unit tests for the ChequingAccount class.
Author: Matt Kenyon
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

__author__ = "Matt Kenyon"
__version__ = "1.0.0"

from unittest import TestCase
from datetime import date
from bank_account.chequing_account import ChequingAccount

class ChequingAccountTests(TestCase): 
    """Contains the tests for the Chequing Account class."""

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        account_number = 123456
        client_number = 314159
        balance = 500.50
        date_created = date(2025, 2, 14)
        overdraft_limit = -100
        overdraft_rate = 0.05

        self.chequing_account = ChequingAccount(account_number, 
                                                client_number, balance, 
                                                date_created, overdraft_limit, 
                                                overdraft_rate)
        
    # __init__ tests
    def test_init_valid_parameters(self):
        self.assertEqual(
            123456, self.chequing_account._BankAccount__account_number)
        self.assertEqual(
            314159, self.chequing_account._BankAccount__client_number)
        self.assertEqual(
            500.50, self.chequing_account._BankAccount__balance)
        self.assertEqual(date(2025, 2, 14), self.chequing_account._date_created)
        self.assertEqual(
            -100, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(
            0.05, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_init_invalid_overdraft_limit_type_sets_default(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = 500.50
        date_created = date(2025, 2, 14)
        overdraft_limit = "invalid"
        overdraft_rate = 0.05

        # Act
        self.chequing_account = ChequingAccount(account_number, 
                                                client_number, 
                                                balance, 
                                                date_created, 
                                                overdraft_limit,
                                                overdraft_rate)
        
        # Assert
        self.assertEqual(
            -100, self.chequing_account._ChequingAccount__overdraft_limit)

    def test_init_invalid_overdraft_rate_sets_default(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = 500.50
        date_created = date(2025, 2, 14)
        overdraft_limit = -100
        overdraft_rate = "invalid"

        # Act
        self.chequing_account = ChequingAccount(account_number, 
                                                client_number, 
                                                balance, 
                                                date_created, 
                                                overdraft_limit, 
                                                overdraft_rate)
        
        # Assert
        self.assertEqual(
            0.05, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_init_date_invalid_type_sets_default(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = 500.50
        date_created = "invalid"
        overdraft_limit = -100
        overdraft_rate = 0.05
        expected = date.today()

        # Act
        chequing_account = ChequingAccount(account_number, 
                                           client_number, 
                                           balance, 
                                           date_created, 
                                           overdraft_limit,
                                           overdraft_rate)
        
        # Assert
        self.assertEqual(expected, chequing_account._date_created)

    def test_get_service_charges_balance_greater_than_limit(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = 500.50
        date_created = date(2025, 2, 14)
        overdraft_limit = -100
        overdraft_rate = 0.05

        chequing_account = ChequingAccount(account_number, 
                                           client_number, 
                                           balance, 
                                           date_created, 
                                           overdraft_limit, 
                                           overdraft_rate)

        # Act

        service_charge = chequing_account.get_service_charges()

        # Assert
        self.assertEqual(0.5, service_charge)

    def test_get_service_charges_balance_less_than_limit(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = -200
        date_created = date(2025, 2, 14)
        overdraft_limit = -100
        overdraft_rate = 0.05

        chequing_account = ChequingAccount(account_number, 
                                           client_number, 
                                           balance, 
                                           date_created, 
                                           overdraft_limit, 
                                           overdraft_rate)

        # Act

        service_charge = chequing_account.get_service_charges()

        # Assert

        self.assertEqual(5.5, service_charge)

    def test_get_service_charges_balance_equal_to_limit(self):
        # Arrange
        account_number = 123456
        client_number = 314159
        balance = -100
        date_created = date(2025, 2, 14)
        overdraft_limit = -100
        overdraft_rate = 0.05

        chequing_account = ChequingAccount(account_number, 
                                           client_number, 
                                           balance, 
                                           date_created, 
                                           overdraft_limit, 
                                           overdraft_rate)

        # Act

        service_charge = chequing_account.get_service_charges()

        # Assert
        self.assertEqual(0.5, service_charge)

    def test_str_returns_correct_string_representation(self):
        # Arrange & Act
        actual = self.chequing_account.__str__()

        # Assert
        expected = (f"Account Number: 123456 Balance: $500.50\n"
            f"Overdraft Limit: $-100.00 " 
            f"Overdraft Rate: 5.00% "
            f"Account Type: Chequing")

        self.assertEqual(expected, actual)
