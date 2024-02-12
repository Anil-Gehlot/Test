class employee:
    def __init__(self):
        self.name=input("Name of the employee : ")
        self.employee_Id=input("Enter employee Id : ")
        self.contact=input("Contact No. : ")
        self.address=input("Address : ")
        self.department=input("Department name : ")
    def show_detail(self):
        print("Employee Id : ",self.employee_Id)
        print("Name : ",self.name)dm fdsf
        sdf
        print("Address : ",self.contact)
        print("Contact : ",self.address)
        print("Department name : ")
    def write(self):
        f=open("employee.txt","a")
        data=self.employee_Id + "," + self.name + "," + self.contact + "," + self.address + "," + self.department + "\n"
        f.write(data)
        print("Data entried successfully")

class Manager(employee):
    employee().__init__()
    def dept_employee_detail(self):
        f=open("employee.txt", 'r')
        data=f.read()
        data_row=data.split("\n")
        data_row.pop()
        valid_row=[]
        for i in data_row:
            x=i.split(",")
            if self.department==x[len(x)-1]:
                valid_row.append(i)

class owner (Manager,employee):
    def show_all(self):
        f=open("employee.txt","r")
        data=f.read()
        data_row=data.split("\n")
        data_row.pop()
        for i in data_row:
            x=i.split(",")
            print("--------------------------")
            
            print("Employee Id : ",x[0])
            print("Name : ",x[1])
            print("Address : ",x[2])
            print("Contact : ",x[3])
            print("Department name : ",x[4])
        print("------------------5--------------------")

s1=employee()
s2=Manager()
s3=owner()
s1.write()
s2.write()
s3.write()

s1.show_detail()
s2.show_detail()
s2.dept_employee_detail()
s3.show_detail()
s3.dept_employee_detail()
s3.show_all












