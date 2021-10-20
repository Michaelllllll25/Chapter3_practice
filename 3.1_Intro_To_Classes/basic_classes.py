class Student:
    name: str
    grade: int
    average: float

student1 = Student()                   
student1.name = "Esteban"
student1.grade = 12
student1.average = 79.3

student2 = Student()                   
student2.name = "Dave"
student2.grade = 10
student2.average = 91

student3 = Student()                   
student3.name = "Michelle"
student3.grade = 11
student3.average = 98.6

print(f"The names are: {student1.name} {student2.name} {student3.name}")
print(f"The grades are: {student1.grade} {student2.grade} {student3.grade}")
print(f"The averages are: {student1.average} {student2.average} {student3.average}")

average = student1.average + student2.average + student3.average / 3

print(f"The average for the three students is: {average}")

