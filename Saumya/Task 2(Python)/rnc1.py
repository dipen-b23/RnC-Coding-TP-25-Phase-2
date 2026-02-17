class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = tuple(marks)
    
    def total(self):
        return sum(self.marks)
    
    def average(self):
        return sum(self.marks)/len(self.marks)
    
def create_students():
    students = []

    n = int(input("Enter number of students: "))
    m = int(input("Enter number of subjects: "))

    for i in range(n):
        print("Details of student ", (i+1), ": ")
        name = input("Enter name: ")
        while True:
            marks0 = input("Enter " + str(m) + " marks(space separated):")
            marks = list(map(float,marks0.split()))

            if len(marks) == m:
                break
            else:
                print("Incorrect number of marks. Try again")
        student = Student(name, marks)
        students.append(student)

    return students

def analyze_students(students):
    total, l = 0, 0
    for i in range(len(students)):
        total += students[i].total()
        l += len(students[i].marks)
    avg = total/l

    print("\nCombined average of marks of all students in all subjects is ", format(avg, ".2f"))

    highest = max(students,key = lambda x : x.total())
    lowest = min(students,key = lambda x : x.total())

    print("\nThe student with the highest marks is ", highest.name, " with a total of ", highest.total(), " marks")
    print("The student with the lowest marks is ", lowest.name, " with a total of ", lowest.total(), " marks")

    sorted_students = sorted(students, key = lambda s: s.total(), reverse = True)

    print("\nStudents sorted by total (descending):")
    for student in sorted_students:
        print(student.name, "- Total: ", student.total(), ", Average: ", format(student.average(),".2f"))

def main():
    students = create_students()
    analyze_students(students)

if __name__ == "__main__":
    main()






        
