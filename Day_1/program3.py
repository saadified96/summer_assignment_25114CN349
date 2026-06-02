#Write a program to Find factorial of a number.
n = int(input("enter the number for finding factorial ->"))
fact = 1 
for i in range(1,n+1):
    fact*=i
print(f"the factorial is {fact}")
