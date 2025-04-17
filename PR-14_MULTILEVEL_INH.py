#14) Write a Python program to show multilevel inheritance.

class A:
    def fun1(self):
        print("Hello World!!")
class B(A):
    def fun2(self):
        print("Welcome to the world of python.")
class C(B):
    def fun3(self):
        print("This is Multilevel Inheritence.")
ob = C()
ob.fun1()
ob.fun2()
ob.fun3()