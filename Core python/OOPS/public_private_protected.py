class Person:
    def __init__(self, name):
        self.name = name  # Public attribute

# Usage
person = Person("Alice")
print(person.name)  # Accessible from outside the class
person.name = "Bob"  # Can be modified freely

class Employee:
    def __init__(self, name, salary):
        self.name = name        # Public attribute
        self._salary = salary   # Protected attribute

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}")

# Usage
employee = Employee("Bob", 50000)
employee.display_info()  # Accessible via method
print(employee._salary)  # Accessible but discouraged


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance               # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance  # Can access private attribute

# Usage
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)     # Raises AttributeError
