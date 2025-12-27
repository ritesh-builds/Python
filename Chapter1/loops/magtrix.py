# Python program for Matrix creation and printing

# Taking rows and columns input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initializing matrix
matrix = []

print("Enter the elements row-wise: ")

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    matrix.append(row)

# Printing the matrix
print("\nThe Matrix is:")
for row in matrix:
    print(row)



     
