'''Write a Python program that manages student marks using classes and functions.

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
'''


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = tuple(marks)

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)


def create_student():
    students = []

    n = int(input("Enter number of students: "))
    m = int(input("Enter number of subjects: "))

    for i in range(n):
        name = input("Enter student name: ")
        marks = list(map(int, input(f"Enter {m} marks: ").split()))
        students.append(Student(name, marks))

    return students


def analyze_students(students):
    totalmarks = 0

    for s in students:
        totalmarks += s.total()

    avg_all_marks = totalmarks / len(students)

    high = students[0]
    low = students[0]

    for s in students:
        if s.total() > high.total():
            high = s
        if s.total() < low.total():
            low = s
    
    print("Total of all marks:", totalmarks)
    print("Average marks of all students:", avg_all_marks)
    print("Highest Total:", high.name, high.total())
    print("Lowest Total:", low.name, low.total())
    

def main():
    students = create_student()
    analyze_students(students)


main()
