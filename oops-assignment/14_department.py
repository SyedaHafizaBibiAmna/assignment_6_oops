class Employee():

    def __init__(self, name):
        self.name =  name


class Department():
    def __init__(self, employee):
        self.employee = employee


emp = Employee("Bibi Amna")
dep = Department(emp)

print(dep.employee.name)