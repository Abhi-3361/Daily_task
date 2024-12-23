#take input from the user
number=int(input("enter a number:"))
#initialize sum
sum=0
#find the sum of cube of each digit
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
#display the result
if number==sum:
    print(number,"is an armstrong number.")
else:
    print(number,"is not an armstrong number.")
