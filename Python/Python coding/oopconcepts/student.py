from oopconcepts.college import College

class Student(College):

    def __init__(self, rno, sname, m1, m2, m3, ccode, cname, ccity):
        super().__init__(ccode, cname, ccity)
        self.rollno = rno
        self.stuname = sname
        self.marks1 = m1
        self.marks2 = m2
        self.marks3 = m3

    def display_student_details(self):   # fixed spelling
        print(f'Roll No: {self.rollno}\nName: {self.stuname}')

    def calculate_total(self):
        total = self.marks1 + self.marks2 + self.marks3
        return total

    def calculate_average(self):
        avg = self.calculate_total() / 3
        print(f'Average of the marks: {avg}')
        return avg
