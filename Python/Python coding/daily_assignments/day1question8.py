# Write a program that takes a number as input and uses a for loop to calculate its
# factorial. Print the result.

num = int(input("Enter a Number : "))
fact = 1

for i in range(1,num+1):
    fact *=i
print(fact)
