# Author: Jacianna Dockery
# Date: 9/28/2026
# File: payable.py
# Description: Define the payable class
from abc import ABC, abstractmethod


class Payable(ABC):

    @abstractmethod
    def calculate_payment(self) -> float:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass




