class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)


# Outside class
def create_students():

    students = []

    n = int(input("Enter the number of students: "))
    m = int(input("Enter the number of subjects: "))

    for i in range(n):

        name = input("Enter the student name: ")

        marks = tuple(map(int, input("Enter marks separated by space: ").split()))

        s = Student(name, marks)

        students.append(s)

    return students


def analyze_students(students):

    total_all = sum(s.total() for s in students)

    total_subjects = sum(len(s.marks) for s in students)

    overall_average = total_all / total_subjects

    print("Overall Average Marks:", overall_average)

    highest = max(students, key=lambda s: s.total())
    print("Highest Total:", highest.name, "-", highest.total())

    lowest = min(students, key=lambda s: s.total())
    print("Lowest Total:", lowest.name, "-", lowest.total())

    sorted_students = sorted(students, key=lambda s: s.total(), reverse=True)

    print("\nStudents Sorted By Total Marks (Descending):")
    for s in sorted_students:
        print(s.name, "-", s.total())


def main():

    students = create_students()
    analyze_students(students)


#if __name__ == "__main__":
main()

             
      
 
                  
                   
            