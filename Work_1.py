

class Employee:
    def calculate_salary(self):
        pass

    def display_info(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, ):
        self.name = name
        self.basic_stavka = 50000
        self.kof = 1.2

    def calculate_salary(self):
        return self.basic_stavka * self.kof

    def display_info(self):
        return f'name: {self.name}, salary: {self.calculate_salary()}'


class PartTimeEmployee(Employee):
    def __init__(self, name, hours):
        self.name = name
        self.kof = 0.5
        self.hours = hours
        self.basic_stavka = 50000

    def calculate_salary(self):
        return self.basic_stavka * self.kof * self.hours

    def display_info(self):
        return f'name: {self.name}, salary: {self.calculate_salary()}'


def process_salary(employee):
    return f'{employee.calculate_salary()}\n{employee.display_info()}\n'


employee1 = FullTimeEmployee('Nicxai')

employee2 = PartTimeEmployee('Garry', 22)

print(process_salary(employee1))
print(process_salary(employee2))
