# Number of rows for the pattern
n = int(input("enter the rows count:"))

# Loop to print each row
for i in range(1, n + 1):
    # Print leading spaces, decreasing by 1 each row
    print(' ' * (n - i), end='')
    
    # Print the alternating 1s and 0s
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end='')  # Print 1 for odd index
        else:
            print(0, end='')  # Print 0 for even index
    
    # Move to the next line after printing each row
    print()
