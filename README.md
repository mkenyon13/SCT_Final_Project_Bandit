# SCT Final Project With Bandit
There have been four vulnerabilities introduced into this project.
Record your findings as comments on the pull request.

# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Matt Kenyon

## Assignment

### Assignment 1

This part of the project will demonstrate the use of classes, accessors, and modifiers.

### Assignment 2

This part will demonstrate Abstraction, inheritance, and polymorphism through the use of
super classes and sub classes.

### Assignment 3

This assignment will leverage the use of design patterns to improve scalability of the
service charge calculation and notify a client whenever a large transaction will take place.

### Assignment 4

This assignment utilizes PySide6 to expand upon the previous assignment and create a UI for
the bank account data. Event listeners will be used to trigger events allowing for dynamic interactions.

### Assignment 5

Expanding on the GUI, an algorithm will be used to allow filtering of data. Also, HTML help
files will be generated based on the class documentation and the program will packaged together with an
installer so the software can be distributed.

## Encapsulation

Inside if the BankAccount class, certain attributes are set to be privately visible by using name mangling.
(Ex: self.__account_number = account_number)
Accessor property methods are included to give limited access to these values when needed for things such
as unit testing. This method of restricting access to variables is one example of Encapsulation.

## Polymorphsim

Examples of Polymorphsim can be found within the sub classes of BankAccount super class in the method
called get_service_charges. The method name is identical in each of the three sub classes, but the behavior
is different for each unique situation, as the sub classes have different goals.

## Strategy Pattern

In this section of the project, we created new classes to allow for additional behavior to be added to a
bank account class. The logic for the service charge iterations is stored in the sub-classes, this is done
in a way that if a new type of bank account class was created, these same strategy patterns could be applied
to the new account types. This could described as a type of behavioral design pattern.

## Observer Pattern

New to this assignment, we add two new classes the Observer and the Subject. The Subject class calls methods
to notify the Observer when there are any state changes, in this situation, large transactions or low balance
transactions. The Observer class creates an interface for all concrete observers, which perform an action when
BankAccount invokes the notify method. By decoupling the object being observed and the Observer, this helps
reduce redundancy in code and allows multiple concrete classes to react to events in the subject object.

## Event-Driven Programming Paradigm

Functionality for event-driven programming is brought into this assignment through the various libraries
in PySide6. Through the signal-slot mechanism, button clicks and text changes trigger corresponding slot
methods. For example, when the user clicks on a cell in account_table, a signal is emitted that calls the
__on_select_account method. This programming paradigm allows for the decoupling of components and
simplified asynchronous programming.

## Filtering

Expanding upon the ability to display data from user accounts in the GUI, this assignment add the functionality
to filter the results based on desired criteria. New behavior was added to the filter widgets that allowed the
user to interact, which would filter the data using a merge sort algorithm. The UI will update based on the state
of the __toggle_filter method and communicates to the user what actions can be performed.
