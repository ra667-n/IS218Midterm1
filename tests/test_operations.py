import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def a():
    return Decimal('5') 

@pytest.fixture
def b():
    return Decimal('3') 

@pytest.fixture(params=[add, subtract, multiply, divide])
def operation(request):
    return request.param  # This will yield each operation in turn for the tests

@pytest.fixture
def expected(a, b, operation):
    if operation == add:
        return a + b
    elif operation == subtract:
        return a - b
    elif operation == multiply:
        return a * b
    elif operation == divide:
        return a / b
    else:
        pytest.fail(f"Unexpected operation: {operation}")


def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculation = Calculation(a, b, operation)
    assert calculation.get_result() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.get_result()