#Write a program to Print prime numbers in a range. 
n = int(input("Enter a number: "))

if n < 2:
    print("no prime numbers in the range")
else:
    for i in range(2,n+1):
        is_prime = True 
        for j in range(2,i):
            if i%j==0:
                is_prime = False 
        if is_prime:
            print(f"{i} is a prime number")
            
