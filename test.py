import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator


    def test_adding_success(self):
        assert self.calc.adding(self, 5, -10) == -5


    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, -10) == 15


    def test_division_success(self):
        assert self.calc.division(self, -10, 5) == -2


    def test_multiply_success(self):
        assert self.calc.multiply(self, -10, 5) == -50