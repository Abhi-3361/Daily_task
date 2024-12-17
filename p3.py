# Number of rows for the pattern
n = int(input("enter the number of lines:"))

# Loop to print each row
for i in range(1, n + 1):
    # Generate and print the pattern of 1s and 0s
    for j in range(1, i + 1):
        # Print 1 for odd index and 0 for even index
        if j % 2 == 1:
            print(1, end='')
        else:
            print(0, end='')
    # Move to the next line after printing each row
    print()
