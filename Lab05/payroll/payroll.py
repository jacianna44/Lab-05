# Author: Jacianna Dockery
# Date: 9/30/2026
# File: payroll.py
# Description: define the payroll data

from payroll.payable import Payable
from payroll invoice import Invoice



def serialize_payroll(payable):
    return payable.to_dict()


def build_payroll_data():
    # Return data as a dictionary for Flask to render
    return {
        "payables": payables_data,
        "invoice_count": total_invoices,
        "employee_count": total_employees,
        "total_gross": total_gross
        
    invoice1 = Invoice("Printer Cartridge", 75.5, 3)
    invoice2 = Invoice("Office Chair", 150.00, 2) 
    
    }
    # payables data 
    for payable in payables
    payables_data.append
    serialize_payroll(payable)
