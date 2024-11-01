'''My Calculator Test'''
from calculator.calculation import Calculation

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(3,3) == 6

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(5,5) == 0

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(9,9) == 1

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4