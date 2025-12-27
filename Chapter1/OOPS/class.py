class employee:      #Here employee is class."
    lang = "Python"   # This is a class attribute.
    salary = 1200000


Ritesh  = employee()     # Here Ritesh is an object.
Ritesh.name = "Ritesh"            # This is an object/instance attribute.
print(Ritesh.name, Ritesh.lang,Ritesh.salary)    

Rohan = employee()
Rohan.name = "Rohan"
print(Rohan.name,Rohan.lang,Rohan.salary)

# Here name is an object/instance attribute and name and salary are class attributes, as the directly belongs to class.