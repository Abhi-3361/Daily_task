# Number of rows for the pyramid
n = int(input("enter rows:"))

# Loop to print each row
for i in range(n):
    # Print spaces: the number of spaces increases as we go down
    print(' ' * i, end='')
    
    # Print stars: the number of stars decreases as we go down
    print('*' * (2 * (n - i) - 1))
