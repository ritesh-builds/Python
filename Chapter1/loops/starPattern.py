n = int(input("Enter a number n: "))
# for i in range(1, n):
#     for j in range(1, i + 1):
#         if i % 2 == 0:
#             print("*", end="")
#         else:
#             print("*", end="")
#     print()


for i in range(1,n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print()
