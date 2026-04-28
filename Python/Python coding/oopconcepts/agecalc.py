from oopconcepts.myexception import AgeException


class AgeCalc():
    def voting_age_check(self,age):
        if age<18:
            raise AgeException('Not Eligible to vote')
        else:
            return True

    def pension_age_check(self,age):
        if age<60:
            raise AgeException('Not Eligible for pension')

