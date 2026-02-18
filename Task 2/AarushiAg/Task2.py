# TASK 2 
total_marks = []
class Student : 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def total(self):
        total = 0
        for x in self.marks:
            total += x 
        return total 
    def average(self):
        total = 0
        for x in self.marks:
            total += x 
        average_marks = total / len(self.marks)
        return average_marks

def descending(marks_list):
    marks_copy = marks_list.copy()
    while marks_copy:
        maxval = max(marks_copy)
        print(maxval, end = " ")
        marks_copy.remove(maxval)

def analyse_students(students):
    print("Averages : ")
    for x in students:
        print(x.average(), end = " ")
    marks_list = []
    for x in students :
        marks_list.append(x.total())

    print("\nHighest Total marks: ", max(marks_list))
    print("Lowest total Marks : ", min(marks_list))
    print("\nDescending order: ", end = "")
    descending(marks_list)

def main():
    students =[]
    n = int(input("Enter no. of students: "))
    s = int(input("Enter no. of subjects: "))
    for i in range(n):
        name = input("Enter name: ")
        marks = []
        subject_marks = input("Enter marks: ")
        for mark in subject_marks.split(','):
            marks.append(int(mark))
        if len(marks) != s:
            print("Invalid number of marks entered:")
            return
        students.append(Student(name, marks))
    analyse_students(students)
if __name__ == "__main__":
    main()
