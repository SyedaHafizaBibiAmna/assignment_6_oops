class Student():
    def __init__(self, name, marks):
        self.name= name
        self.marks= marks

    def display(self):
        print(f"Name:{self.name} Marks:{self.marks}")    

student1= Student("Amna", 90)
student2 = Student("Ujala", 85)        
# print(student1.name, student1.marks)
# print(student2.name, student2.marks)
student1.display()
student2.display()