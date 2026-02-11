class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

def create_students():
    students = []
    b = int(input("Enter number of subjects:"))
    a = int(input("Enter number of students:"))
    for i in range(0, a):
        name = input("Enter name:")
        x = input("Enter marks of subjects")
        c = x.split()
        b = []
        for i in c:
            b.append(int(i))
        students.append([name,b])
    return students

def analyse_students(students):
    a = len(students)
    b = len(students[0][1])
    for i in range (0, b):
        s = 0
        for j in range(0, a):
            s += students[j][1][i]
        avg = s / a
        print(f"Avg in sub {i+1} :", avg)

    #print(students)
    tot = {}
    totm = []
    for i in students:
        tm = 0
        for j in i[1]:
            tm += j
        tot[i[0]] = tm
        totm.append(tm)
    #print(tot)
    totm.sort()

    min = totm[0]
    max = totm[-1]

    for i in tot:
        if tot[i] == min:
            minname = i
        if tot[i] == max:
            maxname = i

    print(f"Max marks by {maxname} is {max}")
    print(f"Min marks by {minname} is {min}")
    totm.sort(reverse=True)
    for i in totm:
        for j in tot:
            if tot[j] == i:
                print(f"Name : {j}, Total marks : {tot[j]}")

def main():
    students = create_students()
    analyse_students(students)

main()