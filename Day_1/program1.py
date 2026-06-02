#Write a program to Calculate sum of first N natural numbers. 
n = int(input("enter number N ->"))
sum = 0
for i in range(n+1):
    sum+=i
print(f'sum is {sum}')
