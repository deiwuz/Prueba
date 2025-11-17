def sum(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        return ("Error: Division by zero is not allowed.")

def multiply(a: int, b: int) -> int:
    return a * b


if __name__ == "__main__":
    print("Sum:", sum(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Divide:", divide(10, 0))
    print("Multiply:", multiply(10, 5))