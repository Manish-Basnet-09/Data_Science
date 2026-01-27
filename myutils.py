# my_utils.py

PI = 3.14159

def greet(name):
    """Returns a simple greeting."""
    return f"Hello, {name}! Welcome."

def add_numbers(x, y):
    """Adds two numbers."""
    return x + y

def calculate_area(radius):
    """Calculates area of a circle."""
    return PI * radius * radius
   
if __name__ == "__main__":
    print(f"Testing add_numbers(5, 3): {add_numbers(5, 3)}")
    print(f"Testing greet('Alice'): {greet('Alice')}")
    print(f"Area of Circle: {calculate_area(4)}")