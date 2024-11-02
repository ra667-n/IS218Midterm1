'''My Calculator Test'''
from calculator.calculation import Calculation

def test_addition():
    '''Test that addition function works '''    
    assert Calculation.add(3,3) == 6

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculation.subtract(5,5) == 0

def test_divide():
    '''Test that division function works '''    
    assert Calculation.divide(9,9) == 1

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculation.multiply(2,2) == 4