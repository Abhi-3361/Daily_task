#taking input from the user
i=int(input("enter the number of rows:"))
#creating outer loop
for i in range(i,0,-1):
    #creating inner loop
    for j in range(0,i):
        #printing *
        print("*",end="")
    print()
