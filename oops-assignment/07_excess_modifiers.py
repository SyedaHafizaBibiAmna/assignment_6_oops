class Employee():

    def __init__(self, name, salary, ssn):
        self.name = name # public
        self._salary = salary # protected
        self.__ssn = ssn # private

emp = Employee("Amna", 50000 , "123-45-6789") 
print(emp.name)
print(emp._salary)
print(emp.__ssn)
print(emp._Employee__ssn) # Accessing private attribute using name mangling
# print(emp.__ssn) # AttributeError: 'Employee' object has no attribute '__ssn'
# print(emp._Employee__ssn) # Accessing private attribute using name mangling   


