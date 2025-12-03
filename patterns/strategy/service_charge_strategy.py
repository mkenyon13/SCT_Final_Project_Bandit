"""This module defines the ServiceChargeStrategy class."""

__author__ = "Matt Kenyon"
__version__ = "2025-3-10"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """This class is used to define service charge strategy behavior."""

    BASE_SERVICE_CHARGE = 0.50 
    """BASE_SERVICE_CHARGE (float): The base fee amount added to 
        service charges."""

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the base service charges.
        
        Args: 
            account (BankAccount): This Class is used to store the input
                of bank_account information.

        Returns:
            float: A float value for the amount of the service charge. 
        """

        pass
