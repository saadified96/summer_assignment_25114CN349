#Write a program to Find GCD of two numbers. 
n = int(input("Enter a number: "))
m = int(input("enter a number: "))
gcd = 1 
if n < m:
    for i in range(2,n+1):
        if (n%i==0 and m%i==0):
            gcd = i 
else:
    for i in range(2,m+1):
        if (n%i==0 and m%i==0):
            gcd = i 
print(f"the GCD is {gcd}")
