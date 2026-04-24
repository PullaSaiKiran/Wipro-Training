class EmployeeDetails:
    def __init__(self,empno,ename ,basic_pay):
        self.__empno = empno
        self.__ename = ename
        self.__basic_pay = basic_pay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    # def get_empno(self):
    #     return  self.__empno
    #
    # def set_empno(self,eno):
    #     self.__empno = eno

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self,eno):
        self.__empno = eno

    @property
    def ename(self):
        return self.__ename

    @ename.setter
    def ename(self,en):
        self.__ename=en

    @property
    def basicpay(self):
        return self.__basic_pay

    @basicpay.setter

    def basicpay(self,bp):
        self.__basic_pay=bp


    def __calculate_allowence(self):
        allowance = (self.__basic_pay * self.da / 100) + (self.__basic_pay * self.hra / 100)
        return allowance

    def __calculate_deduction(self):
        deduction = (self.__basic_pay * self.pf / 100)
        return deduction
    # def empno(self):
    #     return self.__empno

    def calculate_netsal(self):
        netsal = self.__basic_pay + self.__calculate_allowence() - self.__calculate_deduction()
        return netsal


