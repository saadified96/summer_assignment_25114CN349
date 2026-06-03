#Write a program to Find product of digits. 
n = int(input("enter the number n -> "))
product = 1 
if n==0:
    print("product is 0")
else:
    while n > 0:
        lastDigit = n%10
        product*=lastDigit
        n//=10
print(f"product of digits is {product}")
