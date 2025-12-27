num = int(input("Enter the value of num: "))
def fact(num):
    if(num == 0 or num == 1):
        return num
    return num * fact(num-1)

print(f"The Factorial of {num} is {fact(num)}")