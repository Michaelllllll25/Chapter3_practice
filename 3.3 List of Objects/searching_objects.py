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

def find_student(students: list[Student], student_id: int) -> str:
    """Search for student id

    Args:
        students: list[Student]
        student_id: int

    Returns:
        A single student object or none if it doesn't exist
    """
    for stud in students:
        if stud.student_id == student_id:
            return stud
        else:
            stud = "None"
            return stud

students = [
    Student("Michael", 12, 12345),
    Student("Bob", 12, 24681),
    Student("Jack", 10, 36478),
    Student("Will", 9, 12563)
]

run = True
while run == True:
    id = int(input("Enter student id: "))
    found = find_student(students, id)
    if found == "None":
        print("INVALID STUDENT ID")
    else:
        print(f"Name: {found.name} / Grade: {found.grade} / Student ID: {found.student_id}")
    print()
    print("Would you like to search for another student?")
    print("[1]- Yes")
    print("[2]- No")
    again = int(input("-> "))
    if again == 2:
        run = False
            
print("Bye")
