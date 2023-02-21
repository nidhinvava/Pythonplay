# Print odd and even numbers below a given index

i = 1
num = input("Enter a number: ")
print("The even numbers below " + str(int(num)))
for i in range(1,int(num)+1):
   if i % 2 == 0:
    print(i)
print("The odd numbers below " + str(int(num)))
for i in range(1, int(num)+1):
    if i %2 != 0:
      print(i)

