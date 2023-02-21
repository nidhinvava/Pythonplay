# Script to get sum of n numbers.
# sum = n * (n+1) / 2

def sumofnumbers(param):
    sum = float(param) * (float(param) + 1)
    sum = sum / 2
    return  sum
num = input("Enter a number: ")
if float(num) > 0:
    print("The sum of numbers till " + num + " is", sumofnumbers(num))
else:
    print("Invalid number")


