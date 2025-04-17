#13) Write a Python program to show single inheritance.

class A:
    def fun1(self):
        print("Hello World!!")
class B(A):
    def fun2(self):
        print("Welcome to the world of python.")
ob = B()
ob.fun1()
ob.fun2()