def fibonacci_series(limit):
    fib_sequence=[]
    a=0
    b=1
    while a<=limit:
        fib_sequence.append(a)
        a=b
        b=a+b
    return fib_sequence

limit=int(input("enter the number:"))
fib_list=fibonacci_series(limit)
print(fib_list)
