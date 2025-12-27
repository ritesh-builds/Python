class employee:      #Here employee is class."
    language = "Python"   # This is a class attribute.
    salary = 1200000

    def getInfo(self):
        print(f"My name is {self.name} language is {self.language} and salary is {self.salary}LPA.")

    @staticmethod
    def greet():
        print(f"Good Morning ")    

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Hello!")
    

Ritesh  = employee("Lucky","20000000","C")     # Here Ritesh is an object.
Ritesh.language = "Java" 
Ritesh.name = "Ritesh"           # This is an object/instance attribute.
print(Ritesh.salary,Ritesh.language)    

Ritesh.getInfo()
# employee.getInfo(Ritesh)
Ritesh.greet()
