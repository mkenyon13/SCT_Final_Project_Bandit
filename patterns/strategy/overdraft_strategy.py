"""This module defines the OverdraftStrategy class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class OverdraftStrategy(ServiceChargeStrategy):
    """This class describes the account overdraft behavior."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float) -> None:
        """Initializes an instance of the OverdraftStrategy class.
        
        Args:
            overdraft_limit (float): A float value representing the 
                maximum amount a balance can be overdrawn before
                overdraft fees are applied.
            overdraft_rate (float): The rate to which overdraft fees 
                will be applied.

        Returns:
            None:
        """
        
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the amount of service charges comparing the 
            balance amount to the overdraft limit.

        Args:
            account (BankAccount): This Class is used to store the input
                of bank_account information. 

        Returns:
            float: The calculated service charge.    
        """

        service_charge = self.BASE_SERVICE_CHARGE
        
        if account.balance < self.__overdraft_limit:
            service_charge = service_charge + ((
                self.__overdraft_limit - account.balance) 
                * self.__overdraft_rate)

        return service_charge
