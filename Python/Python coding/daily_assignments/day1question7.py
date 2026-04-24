# Write a program that takes a traffic light color (Red, Yellow, Green) as input and
# uses match-case to print the corresponding action (e.g., "Stop" for Red, "Wait"
# for Yellow, etc.).

Signal_light = input("Enter the Single Light Color (Red, Yellow, Green) :")

match Signal_light:
    case 'Red':
        print('Stop')
    case 'Yellow':
        print('Wait')
    case 'Green':
        print('Go')
    case _:
        print('Invalid Input')