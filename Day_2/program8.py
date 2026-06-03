#Write a program to Check whether a number is palindrome. 
n = int(input("enter the number n -> "))
m = n
revNum = 0 
if n==0:
    print("0 is a palindrome")
else:
    while n > 0:
        lastDigit = n%10
        revNum = revNum * 10 + lastDigit
        n//=10
if revNum == m:
    print("number is a palindrome number")
else:
    print("number is not a palindrome number")
