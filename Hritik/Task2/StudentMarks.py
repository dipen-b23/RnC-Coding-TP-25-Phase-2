class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = tuple(marks)
    
    def total(self):
        return sum(self.marks)
    
    def average(self):
        return self.total() / len(self.marks)
    
    @staticmethod
    def create_student():
        n=input("Enter the number of students: ")
        m=input("Enter the number of subjects: ")
        students=[]
        for i in range(int(n)):
            name=input("Enter the name of student: ")
            marks=tuple(map(int, input("Enter the marks of student (separated by spaces): ").split()))
            students.append(Students(name, marks))
        return students
    
    @staticmethod
    def analyze_students(students):
        total_marks=0
        for student in students:
            total_marks +=  student.total()
        average_marks = total_marks / len(students)
        print(f"Total Marks of the Class: {total_marks}\n")
        print(f"Average Marks of the Class: {average_marks:.2f}\n")    
            
        sorted_students = sorted(students, key=lambda s: s.total(), reverse=True)   
        print("Student with the highest total marks:")
        print(f"Student Name: {sorted_students[0].name}, Total Marks: {sorted_students[0].total()}\n")
        print("Student with the lowest total marks:")
        print(f"Student Name: {sorted_students[-1].name}, Total Marks: {sorted_students[-1].total()}\n")
        print("Sorted Students by Total Marks (Descending):")
        for student in sorted_students:
            print(f"Student Name: {student.name}, Total Marks: {student.total()}")

    @staticmethod
    def main():
        students = Students.create_student()
        Students.analyze_students(students)

Students.main()


