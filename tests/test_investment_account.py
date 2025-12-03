"""
Description: Unit tests for the ChequingAccount class.
Author: Matt Kenyon
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

__author__ = "Matt Kenyon"
__version__ = "1.0.0"

from unittest import TestCase
from datetime import date
from bank_account.investment_account import InvestmentAccount

class InvestmentAccountTests(TestCase): 
    """Contains the tests for the Chequing Account class."""

    def setUp(self):
        # Setup runs AUTOMATICALLY before each test method and
        # provides initial values for the class attributes.
        self.account_number = 123456
        self.client_number = 314159
        self.balance = 500.50
        self.date_created = date(2025, 2, 14)
        self.management_fee = 2

        self.investment_account = InvestmentAccount(self.account_number, 
                                                    self.client_number,
                                                    self.balance, 
                                                    self.date_created,
                                                    self.management_fee)
    # __init__tests
    def test_init_valid_parameters(self):
        self.assertEqual(self.account_number, 
                         self.investment_account._BankAccount__account_number)
        self.assertEqual(self.client_number, 
                         self.investment_account._BankAccount__client_number)
        self.assertEqual(self.balance, 
                         self.investment_account._BankAccount__balance)
        self.assertEqual(self.date_created, 
                         self.investment_account._date_created)
        self.assertEqual(
            self.management_fee, 
            self.investment_account._InvestmentAccount__management_fee)
        
    def test_init_management_fee_invalid_set_default(self):
        # Arrange 
        management_fee = "invalid"
        expected = 2.25

        # Act
        self.investment_account = InvestmentAccount(self.account_number, 
                                                    self.client_number,
                                                    self.balance,
                                                    self.date_created,
                                                    management_fee)        

        # Assert
        self.assertEqual(
            expected, 
            self.investment_account._InvestmentAccount__management_fee)
        
    def test_get_service_charges_more_than_ten_years_ago(self):
        # Arrange
        date_created = date(2010, 2, 14)
        expected = 0.5

        investment_account = InvestmentAccount(self.account_number, 
                                               self.client_number, 
                                               self.balance, 
                                               date_created, 
                                               self.management_fee)
        
        # Act
        service_charge = investment_account.get_service_charges()

        # Assert
        self.assertEqual(expected, service_charge)

    def test_get_service_charges_ten_years_ago(self):
        # Arrange
        date_created = date(2015, 2, 16)
        expected = 0.5

        investment_account = InvestmentAccount(self.account_number, 
                                               self.client_number, 
                                               self.balance, 
                                               date_created, 
                                               self.management_fee)
        
        # Act
        service_charge = investment_account.get_service_charges()

        # Assert
        self.assertEqual(expected, service_charge)

    def test_get_service_charges_before_ten_years_ago(self):
        # Arrange
        date_created = date(2020, 2, 16)
        expected = 2.5

        investment_account = InvestmentAccount(self.account_number, 
                                               self.client_number, 
                                               self.balance, 
                                               date_created, 
                                               self.management_fee)
        
        # Act
        service_charge = investment_account.get_service_charges()

        # Assert
        self.assertEqual(expected, service_charge)

    def test_str_date_created_older_returns_correctly_representation(self):
        # Arrange
        date_created = date(2010, 2, 14)
        expected = ("Account Number: 123456 Balance: $500.50"
                    "\nDate Created: 2010-02-14 Management Fee: Waived "
                    "Account Type: Investment")
        

        investment_account = InvestmentAccount(self.account_number, 
                                               self.client_number, 
                                               self.balance, 
                                               date_created, 
                                               self.management_fee)
        
        # Act
        actual = investment_account.__str__() 

        # Assert
        self.assertEqual(expected, actual)
        