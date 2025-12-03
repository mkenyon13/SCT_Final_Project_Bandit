"""This module describes the Subject class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod

class Subject(ABC):
    """This class maintains a list of its observers and notifies them of
    state changes or events.
    """

    def __init__(self) -> None:
        """Initializes an instance of the Subject class."""

        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attaches an observer list item.
        
        Args:
            observer (Observer): Contains a message related to the 
            transaction. 

        Returns:
            None:
        """

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detaches an observer list item.
        
        Args:
            observer (Observer): Contains a message related to the 
            transaction.

        Returns:
            None: 
        """

        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """Displays the message to the output.
        
        Args:
            Contains the string to be displayed.

        Returns:
            None:
        """

        pass
    