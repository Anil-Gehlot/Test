roll_no=0

class Student:
    def __init__(self):
        self.name=input("Enter student's name : ")
        self.fathername=input("Enter student's father name : ")
        self.age=input("Enter age : ")
        self.year=input("Enter year : ")
        self.course=input("Enter course : ")
        self.contact=input("Enter contact : ")
    def show_detail(self):
        print("Name          : ",self.name)
        print("Father's Name : ", self.fathername)
        print("Age           : ",self.age)
        print("Year of joining : ",self.year)
        print("Course        : ",self.course)
        print("Contact       : ",self.contact)
    def generate_rollno(self):
        global roll_no
        roll_no=roll_no+1
        self.roll_no=roll_no
        print("Roll no. of student : ",self.roll_no)

print(roll_no)
s1=Student()
s1.generate_rollno()
s1.show_detail() 
print(roll_no)1


