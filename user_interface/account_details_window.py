"""This module defines the AccountDetailsWindow class."""

__author__ = "ACE Faculty"
__version__ = "2025.04.21"
__credits__ = "Matt Kenyon"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):

            self.__account = copy.deepcopy(account)

            self.account_number_label.setText(
                str(self.__account.account_number)
                )
            self.balance_label.setText(f"${self.__account.balance:,.2f}")
        else:
            QMessageBox.critical(self, 
                                 "Error", 
                                 "Must be an instance of BankAccount")
            self.reject()

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)

    @Slot()
    def __on_apply_transaction(self) -> None:
        """Slot for deposit_button signal. Attempts to perform a 
            transaction (deposit or withdraw) using the amount entered 
            into the BankAccount definition. 
        
        Returns:
            None
        """
        
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        # Check for button click.
        try:
            sender = self.sender()
            transaction_type = ""

            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.__account.deposit(amount)
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__account.withdraw(amount)

            # Set the balance text.
            self.balance_label.setText(f"${self.__account.balance:,.2f}")

            # Clear data and set focus.
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

            # Emit signal for updated balance.
            self.balance_updated.emit(self.__account)

        except Exception as e:
            QMessageBox.warning(self, f"{transaction_type} Failed", f"{e}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
    
    @Slot()
    def __on_exit(self) -> None:
        """Slot for exit_button signal. Will close the QDialog returning
            the user to the Client Lookup Window.

        Returns:
            None    
        """
        self.close()
