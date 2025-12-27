def sum(n):
    if n == 1:
        return 1
  
    return sum(n-1) + n

n = int(input("Enter a number n: "))
print("Sum of first", n, "natural numbers is:", sum(n))


# How to calculate sum of 1st n  natural numbers using recursion.
# Example: 1+2+3+...+n
# Input: n
# Output: Sum of first n natural numbers
# sum(1) = 1
# sum(2) = 1 + 2 
# sum(3) = 1 + 2 +3
# sum(4) = 1 + 2 + 3 + 4

# sum(n) = sum(n-1) + n
# Base case: sum(1) = 1