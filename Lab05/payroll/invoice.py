# Author: Jacianna Dockery
# Date: 9/28/2026
# File: invoice.py
# Description: define the Invoice class

from payroll.payable import Payable

class Invoice(Payable):
    invoice_count = 0

    def __init__(self, part_name: str, price: float, quantity: int):
        self.part_name = part_name
        self.price = price
        self.quantity = quantity

        Invoice.invoice_count += 1

    def calculate_payment(self) -> float:
        return self.price * self.quantity

