#Write a program to Print multiplication table of a given number. 
n = int(input("enter the number whose table is to be printed ->"))
for i  in range(1,11):
    print(f"{n} X {i} = {n*i}")
