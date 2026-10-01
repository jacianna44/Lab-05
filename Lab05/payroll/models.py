# Author: Jacianna Dockery
# Date: 9/28/2026
# File: models.py
# Description: Defines the Person, Employee, and employee subclass models
# used for the payroll system.

from payroll.payable import Payable


class Person:
    # Initialize a person with their personal information
    def __init__(self, first_name: str, last_name: str, gender: str, ssn: str):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.ssn = ssn

    # Return the person's information as a dictionary
    def to_dict(self) -> dict:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "ssn": self.ssn
        }


class Employee(Payable):
    # Keep track of the total number of employees created
    employee_count = 0

    # Initialize the basic employee information
    def __init__(self, person: Person, emp_id: int, years_of_service: int):
        self.person = person
        self.emp_id = emp_id
        self.years_of_service = years_of_service

        Employee.employee_count += 1

    # Return the employee's information as a dictionary
    def to_dict(self) -> dict:
        data = self.person.to_dict()

        data.update({
            "emp_id": self.emp_id,
            "years_of_service": self.years_of_service
        })

        return data

    # Return the total number of employees
    @classmethod
    def get_employee_count(cls) -> int:
        return cls.employee_count


class Secretary(Employee):
    # Initialize the secretary and inherit the basic employee information
    def __init__(
        self,
        person: Person,
        emp_id: int,
        years_of_service: int,
        wage: float,
        hours: float
    ):
        super().__init__(person, emp_id, years_of_service)

        self.wage = wage
        self.hours = hours

    # Calculate the secretary's payment
    def calculate_payment(self) -> float:
        return self.wage * self.hours

    # Add the secretary's information to the employee dictionary
    def to_dict(self) -> dict:
        data = super().to_dict()

        data.update({
            "type": "Secretary",
            "wage": self.wage,
            "hours": self.hours,
            "payment_amount": self.calculate_payment()
        })

        return data


class Manager(Employee):
    # Initialize the manager and inherit the basic employee information
    def __init__(
        self,
        person: Person,
        emp_id: int,
        years_of_service: int,
        department: str,
        salary: float
    ):
        super().__init__(person, emp_id, years_of_service)

        self.department = department
        self.salary = salary

    # Return the manager's salary as their payment
    def calculate_payment(self) -> float:
        return self.salary

    # Add the manager's information to the employee dictionary
    def to_dict(self) -> dict:
        data = super().to_dict()

        data.update({
            "type": "Manager",
            "department": self.department,
            "salary": self.salary,
            "payment_amount": self.calculate_payment()
        })

        return data


class SalesPerson(Employee):
    # Initialize the salesperson and inherit the basic employee information
    def __init__(
        self,
        person: Person,
        emp_id: int,
        years_of_service: int,
        sales: float,
        commission_rate: float
    ):
        super().__init__(person, emp_id, years_of_service)

        self.sales = sales
        self.commission_rate = commission_rate

    # Calculate payment based on sales and commission rate
    def calculate_payment(self) -> float:
        return self.sales * self.commission_rate

    # Add the salesperson's information to the employee dictionary
    def to_dict(self) -> dict:
        data = super().to_dict()

        data.update({
            "type": "SalesPerson",
            "sales": self.sales,
            "commission_rate": self.commission_rate,
            "payment_amount": self.calculate_payment()
        })

        return data


class ExecutiveManager(Manager):
    # Initialize the executive manager and inherit the manager information
    def __init__(
        self,
        person: Person,
        emp_id: int,
        years_of_service: int,
        department: str,
        salary: float,
        bonus: float
    ):
        super().__init__(
            person,
            emp_id,
            years_of_service,
            department,
            salary
        )

        self.bonus = bonus

    # Calculate payment using salary and bonus
    def calculate_payment(self) -> float:
        return self.salary + self.bonus

    # Add the executive manager's information to the manager dictionary
    def to_dict(self) -> dict:
        data = super().to_dict()

        data.update({
            "type": "ExecutiveManager",
            "bonus": self.bonus,
            "payment_amount": self.calculate_payment()
        })

        return data