# Assignment 4

# Build a function for finding a number is prime or not

number = int(input("Enter a number: "))

for i in range(2,int(number/2)+1):
  if (number % i)==0:
    flag = False
    break

if flag == False:
  print(number, " is not a prime number")
else:
  print(number, " is a prime number")
