from src.calculations import Calculations


class TestCalc:
    calc = Calculations()

    def test_area_of_square(self):
        res=self.calc.area_of_square(10)
        assert res==100,'Area is Wrong'

    def test_perimeter_of_rectangle(self):
        res=self.calc.perimeter_of_rect(10,5)
        assert res==100,'Perimeter is Wrong'

