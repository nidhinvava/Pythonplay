# Script to list the prime numbers below N number

def primenum(param):
    for i in range(2, int(param)):
        if int(param) % i == 0:
            print("The number is not a prime number")
            break
    else:
        print("The number is a prime number")

num = input("Enter a number: ")
if int(num) > 1:
    primenum(num)
else:
    print("Invalid number")

