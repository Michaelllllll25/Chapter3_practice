class Student:
    def __init__(self, name: str, grade: int, average: float):
        self.name = name
        self.grade = grade
        self.average = average

stud1 = Student('Esteban', 12, 79.3)
stud2 = Student('Dave', 10, 91)
stud3 = Student('Michelle', 11, 98)


print(f"The names are: {stud1.name} {stud2.name} {stud3.name}")
print(f"The grades are: {stud1.grade} {stud2.grade} {stud3.grade}")
print(f"The averages are: {stud1.average} {stud2.average} {stud3.average}")
