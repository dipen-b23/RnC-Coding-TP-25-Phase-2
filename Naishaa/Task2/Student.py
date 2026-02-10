class Student:
    def __init__(self,marks,name):
        self.marks=tuple(marks)
        self.name=name
        
    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total()/len(self.marks)

    def create_students():
        students=[]
        n=int(input("enter the number of students:"))
        sub=int(input("enter number of subjects:"))
        for i in range(n):
            print("enter details for student {i+1}:")
            name=input("enter name of the student:")
            marks=list(map(int,input("enter marks separated by space:").split()))
            stud=Student(name,marks)
            students.append(stud)
        return students

    def analyze_students(students):
        for stud in students:
            total_all=sum(stud.total())
            average_all=total_all/(len(stud.marks))
            highest=students[0]
            lowest=students[0]
        for stud in students:
            if stud.total()>highest.total():
                highest=stud
            if stud.total()<lowest.total():
                lowest=stud
        sorted_students = students.copy()
        n = len(sorted_students)
        for i in range(n):
            for j in range(i + 1, n):
                 if sorted_students[i].total() < sorted_students[j].total():
                     sorted_students[i], sorted_students[j] = sorted_students[j], sorted_students[i]
        print("\nAfter analysing:")
        print("Average marks of all students:", average_all)
        print("Student with highest marks:",highest.name,highest.total())
        print("Student with lowest marks:",lowest.name,lowest.total())
        print("Students sorted by total marks (descending):")
        for stud in sorted_students:
            print(stud.name,"->",stud.total(),stud.average())

    def main():
        students=create_students()
        analyze_students(students)
        main()
