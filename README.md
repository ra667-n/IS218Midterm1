### Calculator Application

This is an advanced Python-based calculator application designed to demonstrate professional software development practices. It incorporates clean, maintainable code, design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

The Core Functionalities include:

# Command-Line Interface (REPL)
This interface supports:
Execution of arithmetic operations (Add, Subtract, Multiply, and Divide)
Management of calculation history.
Access to extended functionalities through dynamically loaded plugins.

It has a Plugin System which allows seamless integration of new commands or features. It also includes a REPL "Menu" command to list all available plugin commands, ensuring user discoverability and interaction.

# Calculation History Management with Pandas
Pandas has been integrated to manage a robust calculation history, enabling users to: Load, save, clear, and delete history records through the REPL interface. 

# It also has a Comprehensive logging system to record: 
Detailed application operations, data manipulations, errors, and informational messages. Differentiate log messages by severity (INFO, WARNING, ERROR) for effective monitoring.Dynamic logging configuration through environment variables for levels and output destinations.

The following patterns have been added to the code:
### Facade Pattern: Offer a simplified interface for complex Pandas data manipulations.
### Command Pattern: Structure commands within the REPL for effective calculation and history management.
### Factory Method, Singleton, and Strategy Patterns: Further enhance the application's code structure, flexibility, and scalability.

Video Demonstration: https://github.com/user-attachments/assets/9a112e22-d1c5-4a3f-9982-4a9f049b57be
