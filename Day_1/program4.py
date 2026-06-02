#Write a program to Count digits in a number. 
n = int(input("enter the number ->"))
count = 0
print(f"the length of the entered number is {len(str(n))}")
#or
if n==0:
    count=1
else:
    while n>0:
        n//=10
        count+=1

print(f"number of digits entered are -> {count}")


