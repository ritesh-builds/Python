# This function calculates the average of three numbers input by the user.
# This is a  definition a function.


def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    average = (a + b + c)/3
    print("The average is: ", average)

avg()