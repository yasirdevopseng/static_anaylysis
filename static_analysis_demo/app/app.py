import os
import pickle
import math
from typing import List, Dict, Any


def calculate_complex_result(input_value):
    """Calculate a complex result with many branches."""
    if input_value < 0:
        if abs(input_value) > 10:
            temp = -100
        else:
            temp = -10
        if temp < -50:
            result = temp * 2
        else:
            result = temp
    elif input_value == 0:
        result = 0
    elif 0 < input_value < 10:
        result = 10
    elif 10 <= input_value < 20:
        result = 20
    elif 20 <= input_value < 30:
        result = 30
    elif 30 <= input_value < 40:
        result = 40
    else:
        result = 50
    return result


def process_data(data_list, multiplier: int) -> List:
    """Process a list of data with various issues."""
    results = []
    i = 0
    for i in range(len(data_list)):  # Inefficient loop
        item = data_list[i]
        # Type mismatch - multiplier could be int but we're using it as str
        processed = str(item) + str(multiplier)
        results.append(processed)

    # Unused variable
    unused_var = "This does nothing"

    return results


def load_user_data(filename: str):
    """Load user data from a file unsafely."""
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            # Unsafe deserialization - a security risk
            data = pickle.load(f)
        return data
    return None


def execute_command(command: str) -> str:
    """Execute a system command without validation."""
    # Security risk: command injection
    return os.system(command)


def divide_values(a, b) -> float:
    """Divide two values without proper checks."""
    # No division by zero check
    return a / b


class DataProcessor:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.processed = False

    def process(self):
        """Process the data with unclear typing."""
        result = {}
        # Type confusion - mixing types without clear typing
        for key, value in self.data.items():
            result[key] = value + 10  # What if value is not a number?

        self.processed = True
        return result


def main():
    # Mixed type list without proper typing
    data = [1, 2, "3", 4.5]
    processor = DataProcessor({"a": 1, "b": "string"})  # Type mismatch
    processor.process()  # Will fail with certain data

    # Call with incorrect types
    results = process_data(data, "2")  # Type mismatch

    # Dangerous operation with user input
    user_command = input("Enter a command: ")
    execute_command(user_command)  # Security risk

    # Risky division
    quotient = divide_values(10, 0)  # Will raise exception

    # Load potentially malicious data
    user_data = load_user_data("user_data.pkl")

    print(f"Results: {results}")
    print(f"Complex result: {calculate_complex_result(-15)}")


if __name__ == "__main__":
    main()
