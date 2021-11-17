# UML
#       Student
# ---------------------
# name: str
# grade: int
# student_id: int

class Student:
    def __init__(self, name: str, grade: int, student_id: int) -> None:
        self.name = name
        self.grade = grade
        self.student_id = student_id

    

def filter_same_grade(students: list[Student], same_grade: int) -> list[Student]:
    """filters students in the same grade

    Args:
        students: list[Student]
        grade: int

    Returns:
        List of studnets in the grade
    """
    filtered = []
    for stud in students:
        if stud.grade == same_grade:
            filtered.append(stud)

    return filtered

students = [
    Student("Michael", 12, 12345),
    Student("Bob", 12, 24681),
    Student("Jack", 10, 36478),
    Student("Will", 9, 12563),
    Student("Mark", 10, 24635),
    Student("Christina", 11, 32569),
    Student("Olivia", 9, 25489),
    Student("Joe", 12, 36598),
    Student("Nick", 9, 26548)
]


same_grade = int(input("Enter Grade: "))
result = filter_same_grade(students, same_grade)
for student in result:
    print(f"Name: {student.name} | Grade: {student.grade} | Student ID: {student.student_id}")
