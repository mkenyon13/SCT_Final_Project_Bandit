"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "2025.3.16"
__credits__ = "Matt Kenyon"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.
try:
    client = Client(1337, "George", "Miller", "joji@mymts.net")
except ValueError as e:
    print(e)

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    chequing = ChequingAccount(9001, client.client_number, 1000.00, 
                               date(2025,3,13), 100, 5)
except ValueError as e:
    print(e)

try:
    savings = SavingsAccount(9002, client.client_number, 500.00, 
                             date(2020, 3, 15), 50)
except ValueError as e:
    print(e)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing.attach(client)

savings.attach(client)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    second_client = Client(9876, "Doctor", "Evil", "doctorevil@gmail.com")
except ValueError as e:
    print(e)

try:    
    second_savings = SavingsAccount(8001, second_client.client_number, 
                                    1500.00, date(2016,2,20), 50)
except ValueError as e:
    print(e)

second_savings.attach(second_client)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.

# Chequing Account
# High deposit amounts
try:
    chequing.deposit(10000.0)
except ValueError as e:
    print(e)

# normal deposits
try:
    chequing.deposit(1000.0)
except ValueError as e:
    print(e)

# normal withdrawals
try:
    chequing.withdraw(1000.0)
except ValueError as e:
    print(e)

# low balance withdrawals
try:
    chequing.withdraw(10990.0)
except ValueError as e:
    print(e)

# Savings Account
# high deposit amount
try:
    savings.deposit(10500.0)
except ValueError as e:
    print(e)

# normal deposit
try:
    savings.deposit(1000.0)
except ValueError as e:
    print(e)

# normal withdrawal 
try:
    savings.withdraw(1000.0)
except ValueError as e:
    print(e) 

# low balance withdrawal
try:
    savings.withdraw(10960.0)
except ValueError as e:
    print(e)

# Second Savings Account
# High deposit amounts
try:
    second_savings.deposit(10000.0)
except ValueError as e:
    print(e)

# normal deposits
try:
    second_savings.deposit(1000.0)
except ValueError as e:
    print(e)

# normal withdrawals
try:
    second_savings.withdraw(1000.0)
except ValueError as e:
    print(e)

# low balance withdrawals
try:
    second_savings.withdraw(11460.0)
except ValueError as e:
    print(e)
