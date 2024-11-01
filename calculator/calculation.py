class Calculation:
    history = []
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation  

    def get_result(self):
        if self.operation == "add":
            result = self.add(self.a, self.b)
        elif self.operation == "subtract":
            result = self.subtract(self.a, self.b)
        elif self.operation == "multiply":
            result = self.multiply(self.a, self.b)
        elif self.operation == "divide":
             result = self.divide(self.a, self.b)
        self.history.append(result)
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
    
    def divide(a,b) -> None:
        try
result = a/b 
except ZeroDivisionError:

print("Error: Division by zero is not allowed.")
	
print(f"The result of {a} divided by {b} is {result}.")

test = Calculation(2, 4, 'add')
test2 = Calculation.add(1,2)
print(test.get_result())
print(test2)