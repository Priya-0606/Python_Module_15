#12) Write a Python program to demonstrate the use of local and global variables in a class.

class A:
    a = 10
    def fun1(self):
        b = 20
        print("Global variable : ",self.a)
        print("Local Variable : ",b)
  
ob1 = A()
ob1.fun1()