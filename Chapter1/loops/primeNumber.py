n = int((input("Enter the number to check if it is prime or not: ")))

for i in range(2,n):
    if n%i == 0:
        print(f"The number {n} is not prime.")
        break
else:
    print(f"The number {n} is prime.")