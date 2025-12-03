"""This module defines the chequing_account class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from patterns.strategy.management_strategy_fee import ManagementFeeStrategy
from .bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """This class is derived from BankAccount and adds method 
        implementations for an investment account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float) -> None:
        """Initializes attributes for the Investment Account.
        
        Args:
            account_number (int): An integer value representing the bank 
                account number.
            client_number (int): An integer value representing the 
                client number representing the account holder.
            balance (float): A float value representing the current 
                balance of the bank account.
            date_created (date): An instance of the date class from the 
                datetime module. The date that the account was created.

            management_fee (float): The float value representing the 
            management fee. 

        Raises:
            ValueError: Raises when account_number or client_number 
                are not int values.

        Returns:
            None:        
        """

        super().__init__(account_number, client_number, balance, date_created)

        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        # management_fee validation
        try:
            management_fee = float(management_fee)
        except:
            management_fee = 2.25
        
        self.__management_fee = management_fee
        self.__strategy = ManagementFeeStrategy(self._date_created, 
                                                self.__management_fee)

    def __str__(self) -> str:
        """Returns the string representation of the InvestmentAccount 
            object.
        
        Returns:
            The string value from the superclass along with the 
            following description for an Investment Account.

        Example:
            "Date Created: 2010-2-14 Management Fee: Waived 
            Account Type: Investment"

            "Date Created: 2020-2-14 Management Fee: $2.25 
            Account Type: Investment"
        """

        if self._date_created >= self.TEN_YEARS_AGO:
            string_representation = super().__str__()
            string_representation += (
                f"\nDate Created: {self._date_created} " 
                f"Management Fee: ${self.__management_fee:.2f} "
                f"Account Type: Investment")
        elif self._date_created < self.TEN_YEARS_AGO:
            string_representation = super().__str__()
            string_representation += (
                f"\nDate Created: {self._date_created} " 
                f"Management Fee: Waived "
                f"Account Type: Investment")
        
        return string_representation

    def get_service_charges(self) -> float:
        """Calculates the amount of service charges comparing the 
            date created.

        Returns:
            float: The calculated service charge.    
        """

        return self.__strategy.calculate_service_charges(self)
    