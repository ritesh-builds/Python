class Employee:
    company = "Amazon" 
    name = "Ritesh"
    salary = 12345
    def show(self):
        print(f"The name of Employee is {self.name} and the salary is {self.salary}.")


# class programmer():
#     company = "AWS"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}.")

#     def showLanguage(self):
#         print(f"The name is {self.name} and the language is {self.language}.")


class Programmer(Employee):
    company = "AWS"
    def languge(self):

        print(f"The name is {self.company} and the language is {self.languge}.")


a = Employee()
a.show()
b = Programmer()
b.show()

print(a.company, b.company)


