#Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

# single Inheritence

"""class student():
    def get_name(self):
        n = input("Enter your Name : ")
        print("My Name is",n)
class Print(student):
    def get_age(self):
        a = input("Enter Your Age : ")
        print("My Age is",a)
p = Print()
p.get_name()
p.get_age()"""

# Multiple Inheritence

'''class Company():
    def comp_name(self):
        self.cn = input("Enter Company Name : ")
class Position():
    def pos_name(self):
        self.pn = input("Enter your Position : ")
class Employee(Company, Position):
    def emp_name(self):
        self.en = input("Enter your Name : ")
        print(f"My Name is {self.en} and i'm working at {self.cn} as {self.pn}.")  

em = Employee()
em.comp_name()
em.pos_name()
em.emp_name()'''

# Multilevel Inheritence

class Vamp_diaries():
    def male_lead(self):
        print("Gen - 2 Damon and Stefan - Salvatore Brothers.")
class Originals(Vamp_diaries):
    def main_lead(self):
        print("Gen - 1 Klaus and Elijah - Mikelson Brothers.")
class Legacy(Originals):
    def fem_lead(self):
        print("Gen - 3 Hope Daughter of Niklaus Mikelson.")

l = Legacy()
l.male_lead()
l.main_lead()
l.fem_lead()
