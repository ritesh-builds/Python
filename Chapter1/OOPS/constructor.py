class employee:      #Here employee is class."
    language = "Python"   # This is a class attribute.
    salary = 1200000

    def __init__(self,name,language,salary):        # Dunder method which is automatically call.
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object.")

    def getInfo(self):
        print(f"My name is {self.name} language is {self.language} and salary is {self.salary}LPA.")

    @staticmethod
    def greet():
        print(f"Good Morning ")    

Ritesh  = employee("Ritesh" , "Java" , "13000000")  
Ritesh.name = "Ritesh Kumar"   
print(Ritesh.name,Ritesh.salary,Ritesh.language)
Ritesh.getInfo()

# Rohan = employee()