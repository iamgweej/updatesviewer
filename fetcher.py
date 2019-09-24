"""
Provides the Fetcher class, representing an abstract Update fetching mechanism.
"""

from abc import ABC, abstractmethod
from typing import Iterable
from datetime import datetime

class Update(ABC):
    """
    An update recieved from a Fetcher.
    """
    
    @property
    @abstractmethod
    def title(self) -> str:
        """
        The title of the update.
        """
        pass

    @property
    @abstractmethod
    def link(self) -> str:
        """
        The link to the update.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        The description of the update.
        """
        pass

    @property
    @abstractmethod
    def pub_date(self) -> datetime:
        """
        The publication date of the update.
        """
        pass

class Fetcher(ABC):
    """
    An abstract class that all the concrete Fetchers should implement.
    """

    @abstractmethod
    def fetch(self) -> Iterable[Update]:
        """
        Fetch the updates.
        """
        pass
