"""algorithm

1. create class of object circle where area of the circle & circumference of the circle are defines as the method of 
the class& radius is the class circle.

2. create 2 function get() & put() to read & write data to a detail.txt file.
"""

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 3.14*2*self.radius
def dwrite(x):
    file1=open("detail.txt","a")
    # datarow ")
s'dlnmvdsvsd
vsd
vm';ldsmv
;dmbo'dfkgpodfekgl;ef vd v
vmdvm
def dread():df;lsdmf
    
    file1=open("detail.txt","r")
    data=file1.read()
    print(data)
    x=data.split("\n")
    print(x)
    x.pop
    print(x)
    file1.close()



# for i in range(1,6):
#     var1=Circle(i)
#     var2=var1.area()
#     var3=var1.circumference()

#     var4=" {},{},{} \n".format(var1.radius,var2,var3)
    
#     dwrite(var4)
#     print("Radius of circle = {} cm.".format(var1.radius))
#     print("Area of circle = {} sq cm.".format(var2))
#     print("Circumference of circle = {} cm.".format(var3))
#     print("-------------")
dread()



