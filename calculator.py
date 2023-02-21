# Calculator

print("Select an operation to perform:")
print("1. ADD")
print("2. SUBSTRACT")
print("3. MULTIPLY")
print("4. DIVISION")

operation = input("Enter the option: ")
if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Sum is " + str(float(num1) + float(num2)))
elif operation == "2":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Difference is " + str(float(num1) - float(num2)))
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Multiplication is " + str(float(num1) * float(num2)))
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("Division is " + str(float(num1) / float(num2)))
else:
    print("Invalid Entry")
