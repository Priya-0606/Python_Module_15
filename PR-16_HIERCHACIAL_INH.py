#16) Write a Python program to show hierarchical inheritance.

class Parent1():
    def Mother(self):
        print("This is Parent-1 Class.")
class Parent2():
    def Father(self):
        print("This is Parent-2 Class.")
class Child(Parent1, Parent2):
    def child(self):
        print("This is a Child Class.")

c = Child()

c.Mother()
c.Father()
c.child()
