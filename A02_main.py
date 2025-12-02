"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Matt Kenyon"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date
from bank_account.chequing_account import ChequingAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(
    123456, 314159, -200, date(2025, 2, 14), -100, 0.05)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
print(chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
chequing_account.deposit(500.50)
print(chequing_account)
print(chequing_account.get_service_charges())

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(
    123456, 314159, 1000, date(2025, 2, 14), 100)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account)
print(savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
savings_account.withdraw(950.50)
print(savings_account)
print(savings_account.get_service_charges())

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account = InvestmentAccount(
    123456, 314159, 1000, date(2025, 2, 14), 2)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account)
print(investment_account.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account = InvestmentAccount(
    123456, 314159, 1000, date(2010, 2, 14), 2)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_account)
print(investment_account.get_service_charges())

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing_account.withdraw(chequing_account.get_service_charges())
savings_account.withdraw(savings_account.get_service_charges())
investment_account.withdraw(investment_account.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account)
print(savings_account)
print(investment_account)


# strategy = OverdraftStrategy(100.00, 20.0)
# account = ChequingAccount(1234, 
#                           4567,
#                           500.0, 
#                           date(2025,3,13), 
#                           strategy.__overdraft_limit,
#                           strategy.__overdraft_rate)

# print(account)
