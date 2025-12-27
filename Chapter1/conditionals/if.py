A = int(input("Enter the number A: "))
B = int(input("Enter the number B: "))
# greater or lesser number.
if(A > B):
    print("A is greater the B.")
elif(A < B):
    print("B is greater than A.")
else: 
    print("A is equal to B.")

# Even or Odd.
num = int(input("Enter a number: "))
def check_even_odd(num):
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

check_even_odd(num)

# Table.
number = int(input("Enter the number for table: "))
def table(number):
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

table(number)
