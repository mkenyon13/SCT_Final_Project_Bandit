"""This module describes the Observer class."""

__author__ = "Matt Kenyon"
__version__ = "2025.04.21"

from abc import ABC, abstractmethod

class Observer(ABC):
    """This class defines the interface for all concrete observers that 
    need to be notified of changes in the subject
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """Implemented in the concrete classes to notify observers when
        there are changes in the subject.
        
        Args:
            message (str): Shows a message related to the transaction.

        Returns:
            None:
        """

        pass
    