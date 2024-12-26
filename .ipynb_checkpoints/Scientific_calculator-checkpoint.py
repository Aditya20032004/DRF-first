import math

class ScienceCalculator:
    def sin(self, angle):
        return math.sin(math.radians(angle))

    def cos(self, angle):
        return math.cos(math.radians(angle))

    def tan(self, angle):
        return math.tan(math.radians(angle))

if __name__ == "__main__":
    calculator = ScienceCalculator()  # Fixed the class name to match the definition
    try:
        num1 = float(input("Enter the first number: "))  # This variable is not used in the current logic
        operator = input("Enter the operator (sin, cos, tan): ")  # Added 'tan' to the prompt
        if operator in {'sin', 'cos', 'tan'}:  # Updated the set to include 'tan'
            angle = float(input("Enter the angle in degrees: "))
            result = getattr(calculator, operator)(angle)
        else:
            result = "Invalid operator"
        print(f"Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")