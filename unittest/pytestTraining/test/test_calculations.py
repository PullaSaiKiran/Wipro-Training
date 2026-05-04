import pytest
from src.calculations import Calculations

class TestCalculation:
    calc = Calculations()

    @pytest.mark.parametrize("n1,n2,exval",[(5, 5 ,10),(10,5,15),(5,15,20) ])

    def test_add(self,n1,n2,exval):
        res = self.calc.add(n1,n2)
        assert res == exval, 'Addition Error'

    @pytest.mark.parametrize("n1,n2,exval", [(5, 5, 0), (10, 5, 5), (5, 15, -10)])
    def test_sub(self,n1,n2,exval):
        res = self.calc.sub(n1,n2)
        assert res == exval, 'Subtraction Error'

    def test_mul(self):
        res = self.calc.mul(10,5)
        assert res == 50, 'Multiplication Error'

    def test_div(self):
        res = self.calc.div(5,5)
        assert res == 1, 'Division Error'

    @pytest.mark.skip(reason='Not Implemented')
    def test_ne(self):
        res = self.calc.ne(10,10)
        assert res == True, 'NE'


    @pytest.mark.xfail(reason="Exception Not Handled")
    def test_driver(self):
        with pytest.raises(ZeroDivisionError):
            res = self.calc.div(10,0)
            assert res==0

    @pytest.fixture(scope='module',autouse=True)
    def setup(self):
        print('Fixture')

