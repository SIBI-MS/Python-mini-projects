class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.roll_no)
    class laptop:
        def __init__(self):
            self.brand="HP"
            self.ram=8

s1=student('sibi',2)
s2=student('setha',3)

s1.show()