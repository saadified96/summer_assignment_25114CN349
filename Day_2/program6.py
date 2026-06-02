#Write a program to Reverse a number. 
n = int(input("enter the number ->"))
revNum = 0
print(f"reversed number is {int(str(n)[::-1])}")
if n==0:
    print(f"reversed number is {revNum}")
else:
    while n > 0:
        lastDigit = n%10
        revNum = revNum*10 + lastDigit
        n//=10

print(f"the reversed of the entered number is {revNum}")
