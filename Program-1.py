class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

def main():
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
    except ValueError:
        print("Invalid input for numbers.")
        return

    calc = Calculator(a, b)

    if operation == 'add':
        result = calc.add()
    elif operation == 'subtract':
        result = calc.subtract()
    elif operation == 'multiply':
        result = calc.multiply()
    elif operation == 'divide':
        result = calc.divide()
    else:
        result = "Error: Invalid operation type."

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
