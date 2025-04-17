#17) Write a Python program to show hybrid inheritance.

class Grandpa():
    def Inherit(self):
        print("This is Grandpa.")
class Parent1(Grandpa):
    def Mother(self):
        print("This is Parent-1 Class.")
class Parent2(Grandpa):
    def Father(self):
        print("This is Parent-2 Class.")
class Child(Parent1, Parent2):
    def child(self):
        print("This is a Child Class.")

c = Child()

c.Inherit()
c.Mother()
c.Father()
c.child()