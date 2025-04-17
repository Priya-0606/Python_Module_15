#18) Write a Python program to demonstrate the use of super() in inheritance

class A:
    def fun(self):
        print("Hello World!!")
class B(A):
    def fun(self):
        super().fun()
        print("Welcome to the world of python.")
class C(B):
    def fun(self):
        super().fun()
        print("This is Super method in Multilevel Inheritence.")
ob = C()
ob.fun()
