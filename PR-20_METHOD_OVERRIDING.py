#20) Write a Python program to show method overriding

class Human():      # parent class
    def person(self):
        print("This is a 1st person.")

class human():      # child class, it will override parent class 
    def person(self):
        print("This is a 2nd person.")

h = human()
h.person()