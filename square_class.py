class square:
    def __init__(self):
        self.side=int(input("Enter side :"))
    def area(self):
        a=self.side*self.side
        return a

# sq1=square()
# area=sq1.area()
# print("Area :",area)

class cube(square):
    def __init__(self):
        super().__init__()

cb=cube()
side_area=cb.area()
print("Side area : ",side_area)