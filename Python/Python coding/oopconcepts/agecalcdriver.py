from oopconcepts.agecalc import AgeCalc
from oopconcepts.myexception import AgeException

age = int(input("Enter the Age : "))

aobj = AgeCalc()
try:
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
except AgeException as ae:
    print(ae)
else:
    print('Eligible .Contact next step')
