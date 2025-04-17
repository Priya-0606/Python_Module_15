#11) Write a Python program to create a class and access the properties of the class using an object.

class myClass:
    def fun1(self):
        print("This is My First Class.")
        a = 10
        print("Num : ", a)
ob1 = myClass()
ob1.fun1()