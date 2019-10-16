"""
Employee classes
"""
import datetime


class Employee:
    """Represents an employee"""
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split()

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@example.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        def is_too_big(raise_amount):
            return raise_amount > 1.5

        if is_too_big(new_raise_amount):
            print('Are you crazy boss?')
            return False

        cls.raise_amount = new_raise_amount

    @staticmethod
    def is_workday(day):
        return day.weekday() not in (5, 6)


class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if not employees:
            self.employees = set()
        else:
            self.employees = set(employees)

    def add_employee(self, employee):
        self.employees.add(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def print_employee(self, employee):
        print(self.employees)


if __name__ == '__main__':
    python_dev = Developer('Jan', 'Nowak', 4000, 'Python')
    java_dev = Developer('Zenon', 'Kowalski', 3000, 'Java')
    manager = Manager('Janusz', 'Iksiński', 10000, [python_dev, java_dev])
    print(manager)
    manager.print_employee()
    tester = Tester('Roger', 'Pereiro', 3000)
    manager.add_employee(tester)
    manager.print_employee()
