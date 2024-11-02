class Calculation:
    history = []
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  
    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"

    def get_result(self):
        try:
            # Call the operation function with `a` and `b` as arguments
            result = self.operation(self.a, self.b)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            result = "ZeroDivisionError"
        self.history.append(self)
        return result
    
    @staticmethod
    def add(a: int,b: int) -> int:
        return a + b
    
    @staticmethod
    def subtract(a,b):
        return a - b
 
    @staticmethod
    def multiply(a,b):
        return a * b
    @staticmethod
    def divide(a,b):
        result = 0
        try:
            result = a/b 
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        return result

