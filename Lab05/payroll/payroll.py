# Author: Jacianna Dockery
# Date: 9/30/2026
# File: payroll.py
# Description: define the payroll data

from payroll.payable import Payable

def serialize_payroll(payable):
    return payable.to_dict()


def build_payroll_data():
    # Return data as a dictionary for Flask to render
    return {
        "payables": payables_data,
        "invoice_count": total_invoices,
        "employee_count": total_employees,
        "total_gross": total_gross
    }