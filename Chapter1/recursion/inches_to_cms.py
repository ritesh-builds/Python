def inch_to_cms(inch):
    if inch < 0:
        return -1
    return inch * 2.54

n = int(input("Enter the number in inches: "))
result = inch_to_cms(n)
if result == -1:
    print("Invalid input")
else:
    print(f"The corresponding value in cm is: {result}")