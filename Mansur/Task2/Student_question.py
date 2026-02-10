import statistics

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    def total(self):
        total = sum(self.marks)
        return total

    def average(self):
        average = statistics.mean(self.marks)
        return average



list_students = []

def create_student():
    
    num_of_students = int(input("Enter number of students: "))
    num_of_subjects = int(input("Enter number of subjects: "))

    for i in range(0,num_of_students):
        name_of_student = input("Enter name of student: ")
        temp_list = []
        
        for i in range(0,num_of_subjects):
            temp_list.append(int(input(f"Enter marks of subject {i+1}: ")))
            
        marks_tup = tuple(temp_list)
        obj = Student(name_of_student,marks_tup)
        list_students.append(obj)

    return num_of_subjects


x = create_student()


def analyze_students(list_students,num_of_students):
     
    total_marks_list = []
    highest_marks = list_students[0].total()
    highest_marks_index = 0
    lowest_marks = list_students[0].total()
    lowest_marks_index = 0
    

    for i in range(0,len(list_students)):
        total_marks_list.append(list_students[i].total())
        
        if(list_students[i].total() > highest_marks):
               hightest_marks = list_students[i].total()
               highest_marks_index = i

        elif(list_students[i].total() < lowest_marks):
               lowest_marks = list_students[i].total()
               lowest_marks_index = i

    average_marks = statistics.mean(total_marks_list)

    highest_scorer = list_students[highest_marks_index].name
    lowest_scorer = list_students[lowest_marks_index].name

    print("Average marks of all students combined is: ", average_marks)
    print("Highest scorer is: ",highest_scorer)
    print("Lowest scorer is: ",lowest_scorer)

analyze_students(list_students,x)

     


