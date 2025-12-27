def recursive_function(n):
    if(n==1 or n==0):
        return 1
    return n*recursive_function(n-1)

n = int(input("Enter a number n: "))
print("Factorial of", n, "is", recursive_function(n),".")