#Write a program to Find sum of digits of a number. 
n = int(input("enter the number ->"))
sum = 0 
if n==0:
    print(sum)
else:
    while n > 0:
        lastDigit = n%10
        sum+=lastDigit
        n//=10
print(f"the sum of digits is {sum}")
