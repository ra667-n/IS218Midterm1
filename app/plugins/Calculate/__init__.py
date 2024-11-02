from app.commands import Command
from calculator.calculation import Calculation  

class CalculateCommand(Command):
    def __init__(self, operation):
        self.operation = operation

    def execute(self, params=None):
        if len(params) < 2:
            print("Usage: <operation> <number1> <number2>")
            return
        
        try:
            a = float(params[0])
            b = float(params[1])
        except ValueError:
            print("Both number1 and number2 must be valid numbers.")
            return
        
        operation_map = {
            'add': Calculation.add,
            'subtract': Calculation.subtract,
            'multiply': Calculation.multiply,
            'divide': Calculation.divide,
        }
        
        result = operation_map[self.operation](a, b)
        print(f"Result: {result}")
