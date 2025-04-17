#15) Write a Python program to show multiple inheritance.

class Bird():
    def fly(self):
        print("Some Birds can fly some can't.")
class Sparrow(Bird):
    def fly1(self):
        print("Sparrow can fly.")
class Austrich(Bird):
    def fly2(self):
        print("Austrich can't fly.")
S = Sparrow()
S.fly()
S.fly1()
A = Austrich()
A.fly()
A.fly2()
    