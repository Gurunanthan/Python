class Student:
    def __init__(self,name,rollno,year,section):
        self.name = name
        self.rollNo = rollno
        self.year = year
        self.section = section
    @classmethod
    def getValues(cls):
        name = input("Enter the name of the student: ")
        rollNo = input("Enter the roll number of the student: ")
        year = int(input("Enter the year of the student: "))
        section = (input("Enter the section of the student: "))
        return cls(name,rollNo,year,section)

    def display(self):
        print(f"My Name is {self.name}, my rollNo is {self.rollNo}, and I am studying year {self.year} {self.section} section")

# Create a Student instance from user input
guru = Student.getValues()

# Display student details
guru.display()
