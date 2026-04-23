'''
num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))
if num1==num2:
    print("Both Are Equal")
elif num1>num2:
    print(num1,"Is Big")
else:
    print(num2,"Is Big")
'''
'''
#Big 3
num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))
num3=int(input("Enter the Third Number:"))

if num1==num2==num3:
    print("All are equal")
elif num1>num2 and num1>num3 :
    print(num1,"Is Biggest")
elif num2>num1 and num2>num3 :
    print(num2,"Is Biggest")
elif num3>num1 and num3>num2:
    print(num3,"Is Biggest")
'''


ch=int(input("Enter any number from 1-7: "))
match ch:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Input")