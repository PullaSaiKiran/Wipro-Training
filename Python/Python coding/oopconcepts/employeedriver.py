from oopconcepts.employeedetails import EmployeeDetails

#driver
eno = int(input("Emp no : "))
name = input("Emp Name :")
bp = float(input('basic pay : '))
employee = EmployeeDetails(empno=eno,ename=name,basic_pay =bp)
print("=================*===================")
print('Emp no :',employee.empno)
print('Emp name :', employee.ename)
print('Basic Pay :',employee.basicpay)
print('salary :',employee.calculate_netsal())
print("=================*===================")





