#defining variable which may cause runtime error in try block
try:
    user_input=int(input("enter integer:"))
#exception for invalid input error
except ValueError:
    print("please enter a valid integer")
#output for valid input
else:
    print("you entered:",user_input)
