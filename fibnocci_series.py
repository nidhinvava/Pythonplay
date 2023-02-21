# Script to print fibnocci series - 0, 1, 1, 2, 3, 5, 8, 13 ...

index = input("Enter an index upto which the series to print: ")
num1 = 0
num2 = 1
temp = 0
print(num1)
print(num2)

for i in range(1,int(index)):
    num1 = num2
    num2 = temp
    temp = num1 + num2
    print(temp)