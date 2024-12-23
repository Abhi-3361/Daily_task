#defining a function to reverse the string
def isPalindrome(check_string):
    return check_string[::-1]
#asking user the string 
check_string=input("enter the string to check palindrome:")
reverse_string=isPalindrome(check_string)
#printting that the string is palindrome or not
if reverse_string==check_string:
    print("it is a palindromee")
else:
    print("it is not a palindrome")
