class Student:
    def __init__ (s, name, marks):
        s.name = name
        s.marks = tuple(marks)

    def total (s):
        return sum(s.marks)
     
    def average(s):
        return s.total()/len(s.marks)
    
def create_students():
    students = [];
    n = int(input("Enter number of students: "))
    sub = int(input("Enter number of subjects: "))

    for i in range (n):
        print (f"\nEnter details for Student {i+1}")
        name = input("Enter name: ")
        marks = list(map(float, input(f"Enter marks for {sub} subjects: ").split()))
        stu = Student (name, marks)
        students.append(stu)
    return students

def analyze_students(students):
    total_all = 0
    subjects =0
    for i in students:
        total_all += i.total()
        subjects += len(i.marks)

    overall_avg = total_all/subjects

    highest = max(students, key=lambda s: s.total())
    lowest = min(students, key=lambda s: s.total())

    sorted_students = sorted(students, key=lambda s: s.total(), reverse=True)
    print ("\nStudents sorted by total marks (in descending order): \n")
    
    for i in sorted_students:
        print ("name: ", i.name," Total: ", i.total(), " Average: ", i.average())

def main():
    students = create_students()
    analyze_students(students)

main()
