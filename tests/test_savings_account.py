"""
Description: Unit tests for the ChequingAccount class.
Author: Matt Kenyon
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""

__author__ = "Matt Kenyon"
__version__ = "1.0.0"

from unittest import TestCase
from datetime import date
from bank_account.savings_account import SavingsAccount

class savingsAccountTests(TestCase): 
    """Contains the tests for the Savings Account class."""

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.account_number = 123456
        self.client_number = 314159
        self.balance = 500.50
        self.date_created = date(2025, 2, 14)
        self.minimum_balance = 100

        self.savings_account = SavingsAccount(self.account_number, 
                                                    self.client_number,
                                                    self.balance, 
                                                    self.date_created,
                                                    self.minimum_balance)

    # __init__tests
    def test_init_valid_parameters(self):
        self.assertEqual(self.account_number, 
                         self.savings_account._BankAccount__account_number)
        self.assertEqual(self.client_number, 
                         self.savings_account._BankAccount__client_number)
        self.assertEqual(self.balance, 
                         self.savings_account._BankAccount__balance)
        self.assertEqual(self.date_created, 
                         self.savings_account._date_created)
        self.assertEqual(self.minimum_balance, 
                         self.savings_account._SavingsAccount__minimum_balance)

    def test_init_minimum_balance_invalid_set_default(self):
        # Arrange 
        minimum_balance = "invalid"
        expected = 50

        # Act
        self.investment_account = SavingsAccount(self.account_number, 
                                                    self.client_number,
                                                    self.balance,
                                                    self.date_created,
                                                    minimum_balance)        

        # Assert
        self.assertEqual(
            expected, self.investment_account._SavingsAccount__minimum_balance)
        
    def test_get_service_charges_balance_greater_than_minimum(self):
        # Arrange
        expected = 0.5

        investment_account = SavingsAccount(self.account_number, 
                                               self.client_number, 
                                               self.balance, 
                                               self.date_created, 
                                               self.minimum_balance)
        
        # Act
        service_charge = investment_account.get_service_charges()

        # Assert
        self.assertEqual(expected, service_charge)

    def test_get_service_charges_balance_equal_to_minimum(self):
        # Arrange
        balance = 100
        expected = 0.5

        investment_account = SavingsAccount(self.account_number, 
                                               self.client_number, 
                                               balance, 
                                               self.date_created, 
                                               self.minimum_balance)
        
        # Act
        service_charge = investment_account.get_service_charges()

        # Assert
        self.assertEqual(expected, service_charge)

    def test_get_service_charges_balance_less_than_minimum(self):
        # Arrange
        balance = 10
        expected = 1

        investment_account = SavingsAccount(self.account_number, 
                                               self.client_number, 
                                               balance, 
                                               self.date_created, 
                                               self.minimum_balance)
        
        # Act
        service_charge = investment_account.get_service_charges()

        # Assert
        self.assertEqual(expected, service_charge)

    def test_str_returns_correct_string_representation(self):
        # Arrange
        actual = self.savings_account.__str__()

        # Act
        expected = ("Account Number: 123456 Balance: $500.50"
                    "\nMinimum Balance: $100.00 Account Type: Savings")
        
        # Assert
        self.assertEqual(expected, actual)        
