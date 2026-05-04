import pytest
from dailyassignmentpytest.src.BasicFunctionday7 import BasicFunction

class TestBF:
    Bf = BasicFunction()

    def test_add(self):
        res = self.Bf.add(3, 5)
        assert res == 8, "Expected 3 + 5 to equal 8"

    def test_upper_fail(self):
        result = "hello".upper()
        assert result == "HELLO", "Intentional failure: upper() should not equal lowercase"

    # Define the fixture
    @pytest.fixture(scope='module',autouse=True)
    def number_list(self):
        return [1, 2, 3]

    class TestBF:
        def test_list_length(self, number_list):
            assert len(number_list) == 3,'Fixture'



    @pytest.mark.parametrize("n1,n2,exval", [(5, 5, 10), (10, 5, 15)])
    def test_sub(self, n1, n2, exval):
        res = self.Bf.add(n1, n2)
        assert res == exval, 'Addition Error'




    # Parameterized test
    @pytest.mark.parametrize(
        "x, expected",
        [
            (2, 4),  # 2² = 4
            (3, 9),  # 3² = 9
            (4, 16)  # 4² = 16
        ]
    )
    def test_square(self,x, expected):
        assert self.Bf.square(x) == expected

    def test_divide_by_zero(self):
        # Verify that dividing by zero raises ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            self.Bf.divide(10, 0)