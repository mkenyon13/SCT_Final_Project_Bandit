"""This module defines the ClientLookupWindow Class."""

__author__ = "ACE Faculty"
__version__ = "2025.4.21"
__credits__ = "Matt Kenyon"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """This class describes behavior for the ClientLookup window."""
    
    def __init__(self) -> None:
        """Initializes the instance of ClientLookupWindow.
        Args:
            client_listing (dict): A dictionary of clients.
            accounts (dict): A dictionary of accounts from existing 
                clients.  
        Returns:
            None      
        """
        # client_listing: dict, accounts: dict
        super().__init__()
        self.__client_listing, self.__accounts = load_data()   

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)

        self.filter_button.clicked.connect(self.__on_filter_clicked)  

    @Slot()
    def __on_lookup_client(self) -> None:
        """Slot for lookup_button signal. Obtains the Client object from 
            client_listing based on the client number entered into the 
            client_number_edit widget. Also displays Client account 
            records.

        Returns:
            None
        """

        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.warning(self, 
                                "Invalid Input", 
                                "The Client number must be a numeric value.")
            self.reset_display()
            return

        # Check client number in listing
        if client_number not in self.__client_listing:
            QMessageBox.warning(self, 
                                "Client not found",
                                f"Client number: {client_number} not found.")
            self.reset_display()
            return
        
        # Get Client object
        client_first_name = self.__client_listing[client_number].first_name
        client_last_name = self.__client_listing[client_number].last_name

        self.client_info_label.setText(
            f"{client_first_name} {client_last_name}"
            )

        # Display BankAccounts
        matched_accounts = [acc for acc in self.__accounts.values() 
                            if acc.client_number == client_number]
                
        self.account_table.setRowCount(len(matched_accounts))

        for row, account in enumerate(matched_accounts):
            account_items = [
                QTableWidgetItem(str(account.account_number)),
                QTableWidgetItem(f"${account.balance:,.2f}"),
                QTableWidgetItem(str(account._date_created)),
                QTableWidgetItem(account.__class__.__name__)
            ]

            for col, item in enumerate(account_items):
                item.setTextAlignment(Qt.AlignCenter)
                self.account_table.setItem(row, col, item)

        self.account_table.resizeColumnsToContents()

        # Enable Filtering widgets and update text
        self.filter_button.setEnabled(True)
        self.__toggle_filter(False)
        
    @Slot()
    def __on_text_changed(self) -> None:
        """Slot for client_number_edit signal. Clears all bank account
            records from the account_table

        Returns:
            None    
        """
        self.account_table.setRowCount(0)

    @Slot()
    def __on_select_account(self, row: int, column: int) -> None:
        """Slot for account_table signal. Identifies the account 
            selected and and transfers control to the Account Details
            window based on the selected account.
        
        Args:
            row (int): The row of account_table
            column (int): The column of account_table

        Returns:
            None
        """
    
        selected_account = int(self.account_table.item(row, 0).text())

        if not selected_account or selected_account == 0:
            QMessageBox.critical(self,
                                 "Invalid Selection",
                                 "Please select a valid record.")
            return
        
        if selected_account in self.__accounts:
            account_obj = self.__accounts[selected_account]
            details_window = AccountDetailsWindow(account_obj)
            details_window.balance_updated.connect(self.__update_data)
            details_window.exec()

    def get_user_input():
        user_input = input('Enter your name: ')
        return user_input
        

    @Slot()
    def __update_data(self, account: BankAccount) -> None:
        """Slot for balance_updated signal. Updates and formats data
            in account_table based off of transactions.

        Args: 
            account (BankAccount): An instance of the BankAccount class.
        
        Returns:
            None
        """
        
        # loop through rows in account table.
        for row in range(self.account_table.rowCount()):
            
            # get account number from first column
            item = self.account_table.item(row, 0)
            if item is not None:
                try:
                    table_account_number = int(item.text())

                    # compare the account number with BankAccount
                    if table_account_number == account.account_number:
                        
                        # update the display
                        balance_item = QTableWidgetItem(
                            f"${account.balance:,.2f}"
                            )
                        balance_item.setTextAlignment(Qt.AlignCenter)
                        self.account_table.setItem(row, 1, balance_item)

                        # Update the dictionary
                        self.__accounts[
                            account.account_number
                            ] = account

                        # update file
                        update_data(account)
                        break
                except ValueError:
                    continue

    @Slot()                
    def __on_filter_clicked(self) -> None:
        """Obtain user-defined criteria from filter_combo_box and the 
        filter_edit widgets and then filter the records currently 
        displayed. Then toggle the display of the filtering widgets so 
        the user can tell if the listing in the account_table is 
        complete or filtered.

        Returns:
            None
        """

        if self.filter_button.text() == "Apply Filter":
            # Get filter criteria
            filter_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text()

            # Get matching rows
            matching_rows = []
            row_count = self.account_table.rowCount()

            # Merge Sort algorithm for filtering data
            def merge_sort(arr):
                if len(arr) <= 1:
                    return arr
            
                mid = len(arr) // 2
                left = merge_sort(arr[:mid])
                right = merge_sort(arr[mid:])
                
                return merge(left, right)
        
            def merge(left, right):
                result = []
                i = j = 0
        
                while i < len(left) and j < len(right):
                    left_item = self.account_table.item(
                        left[i], filter_index).text()
                    right_item = self.account_table.item(
                        right[j], filter_index).text()
                    
                    if filter_text in left_item:
                        result.append(left[i])
                        i += 1
                    elif filter_text in right_item:
                        result.append(right[j])
                        j += 1
                    else:
                        i += 1
                        j += 1
                
                # Add remaining elements
                while i < len(left):
                    left_item = self.account_table.item(
                        left[i], filter_index).text()
                    if filter_text in left_item:
                        result.append(left[i])
                    i += 1
                    
                while j < len(right):
                    right_item = self.account_table.item(
                        right[j], filter_index).text()
                    if filter_text in right_item:
                        result.append(right[j])
                    j += 1
                    
                return result
            
            # Create array of row data
            rows = list(range(row_count))
            matching_rows = merge_sort(rows)

            # hide rows that don't match the filter
            for row in range(row_count):
                self.account_table.setRowHidden(
                    row, row not in matching_rows
                    )

            # Update filter label and button text
            self.filter_label.setText("Data is Currently Filtered")
            self.filter_button.setText("Remove Filter")
            self.__toggle_filter(True)
        else:
            # show all rows
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            # Update filter label and button text
            self.filter_label.setText("Data is not currently filtered")
            self.filter_button.setText("Apply Filter")
            self.__toggle_filter(False)


    def __toggle_filter(self, filter_on: bool) -> None:
        """Toggles the state of filtering widgets and their appearance. 
    
        Args:
            filter_on (bool): True if filtering is active, False if not.

        Returns:
            None:
        """

        if filter_on:
            # Filtering on
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
            self.filter_label.setEnabled(True)
        else:
            # Filtering off
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")
            self.filter_label.setEnabled(True)

            # Show all rows
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
