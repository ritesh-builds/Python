#  Print sum of 1st n natural numbers by for in loop.
n = int(input("Enter the number n to find the sum of first n natural numbers: "))
sum = 0
for i in range(n+1):
    sum += i
print(f"The sum of first {n} natural numbers is {sum}")

# By while loop.
a = int(input("Enter the number a: "))
sum = 0
i = 0
while i <= a:
    sum += i
    i += 1
print(f"The sum of first {a} natural numbers is {sum}")
