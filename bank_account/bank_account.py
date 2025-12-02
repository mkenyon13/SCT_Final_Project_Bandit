"""This module defines the bank_account class."""

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject

__author__ = "Matt Kenyon"
__version__ = "2025.3.16"

class BankAccount(Subject, ABC):
    """This Class is used to store the input of bank_account
    information.  
    """

    LARGE_TRANSACTION_THRESHOLD = 9999.99 
    """LARGE_TRANSACTION_THRESHOLD (float): The maximum transaction 
        amount before a warning is displayed.
    """
    LOW_BALANCE_LEVEL = 50.0
    """LOW_BALANCE_LEVEL (float): The minimum transaction amount before
            a warning is displayed.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date):
        """Initializes a new instance of the bank_account class.

        Args:
            account_number (int): An integer value representing the bank 
                account number.
            client_number (int): An integer value representing the 
                client number representing the account holder.
            balance (float): A float value representing the current 
                balance of the bank account.
            date_created (date): An instance of the date class from the 
                datetime module. The date that the account was created.

        Raises:
            ValueError: Raises when account_number or client_number 
                are not int values.
        """

        super().__init__()

        if not isinstance(account_number, int):
            raise ValueError("Account Number must be numeric.")
        
        if not isinstance(client_number, int):
            raise ValueError("Client Number must be numeric.")
        
        try:
            balance = float(balance)
        except:
            balance = 0.0

        if not isinstance(date_created, date):
            date_created = date.today()

        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance
        self._date_created = date_created


    @property
    def account_number(self) -> int:
        """Gets the account number for the bank account.

        Returns:
            account_number (int): An integer value representing the
                account number.
        """

        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """Gets the client number for the bank account.

        Returns:
            client_number (int): An integer value representing the 
                client number.
        """

        return self.__client_number
    
    @property
    def balance(self) -> float:
        """Gets the balance for the bank account.

        Returns:
            balance (float): A float value representing the balance.
        """

        return self.__balance
        
    def update_balance(self, amount: float) -> None: # This logic is incorrect
        """Updates the balance of the bank account.

        Args:
            amount (float): A float value representing the amount to be
                added to the current balance.
        """

        if isinstance(amount, float):
            self.__balance += amount

        # set the amount to 0 if it fails
        # amount = 0
        
        if abs(self.__balance) < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.__balance:,.2f}:"
                        f" on account {self.__account_number}.")
        
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:,.2f}:"
                        f" on account {self.__account_number}.") 
        
    def deposit(self, amount: float) -> None:
        """Deposits an amount into the bank account.

        Args:
            amount (float): A float value representing the amount to be
                deposited into the account.

        Raises:
            ValueError: Raises if amount is not a numeric value, or if
                amount is negative.
        """
        
        if not isinstance(amount, float):
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be numeric.")
        elif amount < 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be" 
                             f" positive.")
        
        self.update_balance(amount)
    
    def withdraw(self, amount: float) -> None:
        """Withdraws an amount from the bank account.

        Args:
            amount (float): A float value representing the amount to be
                withdrawn from the account.

        Raises:
            ValueError: Raises if amount is not a numeric value, or if
                amount is negative, or if amount exceeds the current balance.
        """
        
        if not isinstance(amount, float):
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")
        elif amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be" 
                             f" positive.")
        elif amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed" 
                             f" balance.")
        
        self.update_balance(-amount)
    
    def __str__(self) -> str:
        """Returns the string representation of the bank account abject.
        
        Returns:
            str: The string representation of the bank account object.

        Example:
            "Account Number: 123456 Balance: $100.00"
        """

        string_representation = ( 
        f"Account Number: {self.__account_number} Balance: "
        f"${self.__balance:,.2f}")

        return string_representation
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """Will return the calculated service charges that a BankAccount
            incur, using a specific formula based on the type of account.

        Returns: 
            float: The amount of service charges as float value.        
        """
        pass

    def attach(self, observer: Observer) -> None:
        """Attaches an observer list item.
        
        Args:
            observer (Observer): Contains a message related to the 
            transaction.

        Returns:
            None. 
        """

        if observer not in self._observers:
            self._observers.append(observer)


    def detach( self, observer: Observer) -> None:
        """Detaches an observer list item.
        
        Args:
            observer (Observer): Contains a message related to the 
            transaction.

        Returns:
            None. 
        """

        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Displays the message to the output.
        
        Args:
            message (str): Contains the string to be displayed.

        Returns:
            None.
        """

        for observer in self._observers:
            observer.update(message)
    