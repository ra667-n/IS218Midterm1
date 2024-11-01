import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from app import App    

if __name__ == "__main__":
    app = App().start()  
    
def calculate_and_print(a, b, operation_name):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)
def main():
    calc = Calculator()
    plugin_loader.load_plugins(calc)

    while True:
        user_input = input("Enter command: ").strip().split()
        if user_input[0].lower() == "exit":
            break
        command, *args = user_input
        try:
            args = list(map(float, args))
        except ValueError:
            print("Error: Arguments must be numbers")
            continue
        print(calc.execute(command, *args)) 

def repl():
    calc = Calculator()
    calc.load_plugins()
    while True:
        user_input = input("Enter command or 'exit': ").strip()
        if user_input.lower() == 'exit':
            break
        try:
            command, x, y = user_input.split()
            x, y = float(x), float(y)
            result = calc.execute_command(command, x, y)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

# main.py
from app import App    

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App