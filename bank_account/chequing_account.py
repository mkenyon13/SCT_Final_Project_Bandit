"""This module defines the chequing_account class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy
from .bank_account  import BankAccount

class ChequingAccount(BankAccount):
    """This class is derived from BankAccount and adds overdraft limits
        and rates for a chequing account.
    """

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, 
                 overdraft_limit: float, overdraft_rate: float) -> None:
        """Initializes attributes for Chequing Account.
        
        Args:
            account_number (int): An integer value representing the bank 
                account number.
            client_number (int): An integer value representing the 
                client number representing the account holder.
            balance (float): A float value representing the current 
                balance of the bank account.
            date_created (date): An instance of the date class from the 
                datetime module. The date that the account was created.

            overdraft_limit (float): A float value representing the 
                maximum amount a balance can be overdrawn before
                overdraft fees are applied.
            overdraft_rate (float): The rate to which overdraft fees 
                will be applied.

        Raises:
            ValueError: Raises when account_number or client_number 
                are not int values.

        Returns:
            None:  
        """

        super().__init__(account_number, 
                         client_number, 
                         balance, 
                         date_created)

        # validate overdraft_limit type
        try:
            overdraft_limit = float(overdraft_limit)
        except:
            overdraft_limit = -100

        # validate overdraft_rate type
        try:
            overdraft_rate = float(overdraft_rate)
        except:
            overdraft_rate = 0.05

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        self.__strategy = OverdraftStrategy(self.__overdraft_limit, 
                                            self.__overdraft_rate)

    def __str__(self) -> str:
        """Returns the string representation of the ChequingAccount 
            object.
        
        Returns:
            The string value from the superclass along with the 
            following description for an Chequing Account.
        """
        string_representation = super().__str__()
        string_representation += (
            f"\nOverdraft Limit: ${self.__overdraft_limit:.2f} " 
            f"Overdraft Rate: {(self.__overdraft_rate * 100):.2f}% "
            f"Account Type: Chequing")
        
        return string_representation

    def get_service_charges(self) -> float:
        """Calculates the amount of service charges comparing the 
            balance amount to the overdraft limit.

        Returns:
            float: The calculated service charge.    
        """

        return self.__strategy.calculate_service_charges(self)    
        