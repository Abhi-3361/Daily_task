#defining variable which may cause runtime error in try block
try:
    numerator=float(input("enter numerator:"))
    denominator=float(input("enter denominator:"))
    result = numerator / denominator
#exception for 0 at denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")#message will print if error occure
#if any error does not occure output will be given 
else:
    print("result:",result)
