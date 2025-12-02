"""This module defines the savings_account class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy
from .bank_account  import BankAccount
from datetime import date, timedelta

class SavingsAccount(BankAccount):
    """This class is derived from BankAccount and adds method 
        implementations for an savings account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, minimum_balance: float) -> None:
        """Initializes attributes for the Savings Account.
        
        Args:
            account_number (int): An integer value representing the bank 
                account number.
            client_number (int): An integer value representing the 
                client number representing the account holder.
            balance (float): A float value representing the current 
                balance of the bank account.
            date_created (date): An instance of the date class from the 
                datetime module. The date that the account was created.

            minimum_balance (float): The minimum value a balance can be 
                before further service charges can be applied. 

        Raises:
            ValueError: Raises when account_number or client_number 
                are not int values.

        Returns:
            None:        
        """

        super().__init__(account_number, client_number, balance, date_created)

        # minimum_balance Validation
        try:
            minimum_balance = float(minimum_balance)
        except:
            minimum_balance = 50
        
        self.__minimum_balance = minimum_balance
        self.__strategy = MinimumBalanceStrategy(minimum_balance)         

    def __str__(self) -> None:
        """Returns the string representation of the SavingsAccount 
            object.
        
        Returns:
            The string value from the superclass along with the 
            following description for an Savings Account.
        
        Example:
            "Account Number: 123456 Balance: 500.50
            Minimum Balance: 100 Account Type: Savings"
        """
        string_representation = super().__str__()
        string_representation += (
            f"\nMinimum Balance: ${self.__minimum_balance:.2f} "
            "Account Type: Savings")

        return string_representation

    def get_service_charges(self) -> float:
        """Calculates the amount of service charges comparing the 
            balance amount to the overdraft limit.

        Returns:
            float: The calculated service charge.    
        """
        
        return self.__strategy.calculate_service_charges(self)
    