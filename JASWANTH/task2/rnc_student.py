"""
Write a Python program that manages student marks using classes and functions.

Requirements:
Define a class Student with:

Attributes:
name — the student’s name
marks — a tuple containing marks in all subjects

Methods:
total() → returns the total marks
average() → returns the average marks
Define a function create_students() that:|

Asks the user to enter the number of students and subjects.
For each student, takes input for the name and marks (space-separated).
Creates a Student object for each and stores them in a list.

Define a function analyze_students(students) that:
Calculates and displays:
The average marks of all students combined.
The student with the highest total marks.
The student with the lowest total marks.
Prints all students sorted by their total marks in descending order.
Use a main() function to manage program execution.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def total(self):
        return sum(self.marks)
    def average(self):
        return self.total()/ len(self.marks)

def create_students():
    students = []
    n=int(input("Enter number of students: "))
    m=int(input("Enter no of subjects: "))
    for i in range(n):
        name=input("Enter student name: ")
       # for j in range(m):
        #    marks.append(input("Enter marks: "))
        marks = []
        for x in input(f"Enter {m} marks: ").split():
            marks.append(int(x))
        students.append(Student(name, marks))
    return students

def analyze_students(students):
    if not students:
        print("No students to analyze.")
        return

    total_marks_all = sum(s.total() for s in students)
    avg_all = total_marks_all / len(students)

    highest = max(students, key=lambda s: s.total())
    lowest = min(students, key=lambda s: s.total())

    print("\n---lol- Analysis-lol ---")
    print(f"Average marks of all students: {avg_all:.2f}")
    print(f"Highest total: {highest.name} ({highest.total()})")
    print(f"Lowest total: {lowest.name} ({lowest.total()})")

    print("\nStudents sorted by total marks (descending):")
    """
    def get_total_marks(student):
        return student.total()
    """
    for s in sorted(students, key=lambda s: s.total(), reverse=True):
        print(f"{s.name} → Total: {s.total()}, Average: {s.average():.2f}")

def main():
    students = create_students()
    analyze_students(students)


if __name__ == "__main__":
    main()