from oopconcepts.college import College
from oopconcepts.student import Student
from oopconcepts.studentgarde import StudentGrade
from oopconcepts.teacher import Teacher

cc = int(input("College Code:"))
cn = input('College Name : ')
ci = input('City :')

rno = int(input("enter the roll no : "))
sn = input("student name :")
m1 = int(input("Marks 1 :"))
m2 = int(input("Marks 2 :"))
m3 = int(input("Marks 3 :"))

eid =int(input("Enter the empid :"))
tn = input("Enter the Name of The teacher :")
de=input("Enter the department name:")
bp=float(input('Basicpay :'))
project = StudentGrade(ccode=cc, cname=cn, ccity=ci,
                       rno=rno, sname=sn, m1=m1, m2=m2, m3=m3)

project.welcome_message()
project.display_college_details()
project.display_student_details()
print(f"Total marks: {project.calculate_total()}")
project.calculate_average()

project.calculate_grade()
print(f"Result: {project.result}\t Grade: {project.grade}")

teach = Teacher(ccode=cc , cname=cn , ccity=ci , eid=eid, tn=tn,de=de,bp=bp)
print(f'Eid :{teach.empid}\t Name:{teach.tname}\t Dept:{teach.dept}\t Basicpay :{teach.basicpay}')
print(f'Salary :{teach.calculate_salary()}')
