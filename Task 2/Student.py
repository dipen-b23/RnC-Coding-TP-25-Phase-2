class Student:
    def __init__(self, name, marks):
         self.name = name
         self.marks = tuple(marks)

    def total(self):
        total = sum(self.marks)
        return total

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

def create_students():
    students = []
    try:
        n = int(input("Enter no. of students:"))
        subj = int(input("Enter no. of subjects:"))
    except ValueError:
        print("Invalid input. Please enter integers for counts.")
        return []

    for i in range(n):
        name=input("Enter name of student "+str(i+1)+": ")
        marks=tuple(map(int, input("Enter marks (space-separated): ").split()))
        students.append(Student(name, marks))


    return students


def analyze_students(students):
    total_marks_all = sum(student.total() for student in students)
    total_subjects_all = sum(len(student.marks) for student in students)
    overall_average = total_marks_all / total_subjects_all
    print("\nOverall average marks of all students: {overall_average:.2f}")

    highest = max(students, key=lambda s: s.total())
    lowest = min(students, key=lambda s: s.total())
    print(f"Highest total marks: {highest.name} ({highest.total()})")
    print(f"Lowest total marks: {lowest.name} ({lowest.total()})")

    sorted_students = sorted(students, key=lambda s: s.total(), reverse=True)
    print("\nStudents sorted by total marks (descending):")
    for student in sorted_students:
        print(f"{student.name}: Total = {student.total()}, Average = {student.average():.2f}")

def main():
    students = create_students()
    analyze_students(students)

if __name__ == "__main__":
    main()