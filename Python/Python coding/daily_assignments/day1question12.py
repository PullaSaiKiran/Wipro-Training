# 2. Write a program that uses a for loop to print numbers from 1 to 10, but skips
# printing the number 5 (use continue) and stops the loop if the number 8 is
# reached (use break).

for i in range (1,11):
    if i == 5:
        continue
    elif i == 8:
        break
    print(i)