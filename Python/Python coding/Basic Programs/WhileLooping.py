# # Natural Numbers Print
#
# num = int(input("Enter a number "))
# value=1
# while value<num:
#     print(value)
#     value += 1

num = input("Enter a number ")
count=len(num)
sum = 0
ni=int(num)
comp=ni
while ni > 0:
    rem = ni % 10
    sum = sum + rem ** count
    ni = ni//10
if sum==comp:

    print("Armstrong")
else:
    print("Not An ArmStrong")







