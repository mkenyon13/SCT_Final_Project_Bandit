"""This module defines the management fee strategy class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """This class describes the account management fee behavior."""

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25) 
    """TEN_YEARS_AGO (date): Finds the exact date ten years ago from 
        today's date.
    """

    def __init__(self, date_created: date, management_fee: float) -> None:
        """Initializes an instance of ManagementFeeStrategy class.
        
        Args:
            date_created (date): A date in YYYY-MM-DD format.
            management_fee (float): The float fee amount added for
                account management.

        Returns:
            None:
        """

        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the management fee comparing the 
            date created to the date ten years ago.

        Args:
            account (BankAccount): This Class is used to store the input
                of bank_account information. 

        Returns:
            float: The calculated service charge.    
        """

        service_charge = self.BASE_SERVICE_CHARGE 

        if self.__date_created > self.TEN_YEARS_AGO: 
            service_charge = service_charge + self.__management_fee
        
        return service_charge
