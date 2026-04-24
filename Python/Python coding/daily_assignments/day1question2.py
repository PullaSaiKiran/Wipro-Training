# . Write a program that takes a year as input and checks if it is a leap year or not.
# Print the result.

Year = int(input("Enter the Year : "))

if Year % 4 ==0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("..Leap Year..")
        else:
            print("..Not A Leap Year..")
    else:
        print("..Leap Year..")
else:
    print("..Not A Leap Year..")
