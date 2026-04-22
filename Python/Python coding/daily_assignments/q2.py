#2. Count how many times "a" appears in a string using enumerate.

string = 'anaconda'
count=0
for index,char in enumerate(string):
    if char == 'a':
        count+=1
print("count of 'a':",count)
