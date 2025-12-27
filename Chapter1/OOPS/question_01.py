class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pincode): # This is a onstructor.
        self.name = name
        self.salary = salary
        self.pincode = pincode


p = Programmer("Ritesh", 280790, 132001)
print(p.company,p.name,p.salary,p.pincode)

r = Programmer("Rohan", 100000, 127008)
print(r.name, r.company, r.salary, r.pincode)