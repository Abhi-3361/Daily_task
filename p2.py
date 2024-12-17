# Number of rows for the pattern
n = int(input("enter number of rows:"))

# Loop through each row
for i in range(1, n + 1):
    # Print space(' ' decreases in each row)
    print(' ' * (n - i), end='')
    
    # Print stars ('*' increases in each row)
    print('*' * i)
