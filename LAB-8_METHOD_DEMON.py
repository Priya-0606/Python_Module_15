#Write Python programs to demonstrate method overloading and method overriding.

#----------------Method Overriding------------------

class Austrich:
    def fly(self):
        print("Austrich can't fly.")

class Sparrow(Austrich):
    def fly(self):
        print("Sparrow can fly.")

a = Austrich()
d = Sparrow()

a.fly()  
d.fly()  

#----------------Method Overloading------------------