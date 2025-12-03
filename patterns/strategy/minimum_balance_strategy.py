"""This module defines the MinimumBalanceStrategy class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """This class describes the minimum balance behavior."""

    SERVICE_CHARGE_PREMIUM = 2.0 
    """SERVICE_CHARGE_PREMIUM (float): The multiplier for service 
        charge fees.
    """

    def __init__(self, minimum_balance: float) -> None:
        """Initializes an instance of the MinimumBalanceStrategy class.

        Args:
            minimum_balance (float): The minimum value a balance can be 
                before further service charges can be applied.

        Returns:
            None:
        """

        self.__minimum_balance = minimum_balance

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

        if account.balance < self.__minimum_balance:
            service_charge = (service_charge * self.SERVICE_CHARGE_PREMIUM)
            
        return service_charge
