
from oopconcepts.calc import Calc

calcobj =Calc()
print(calcobj.add(10,60))
print(calcobj.sub(50,80))
print(calcobj.mul(60,7))
numbers=[10,50,99,87]
count =len(numbers)
print(f'length: {count}')

try:
    res = calcobj.fdiv(10,0)
    for i in range(0,count+1):
        print(numbers[i])
except IndexError:
    print('Check the index')
except ZeroDivisionError:
    print("0 is in denominator")

else:
    print(res)

finally:
    print('Done')

