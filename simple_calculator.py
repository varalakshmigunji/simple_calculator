def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def modulus(x, y):
    if y == 0:
        return "Error! Modulus by zero."
    else:
        return x % y

def main():
    print("Basic Calculator")
    print("=================")
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /, %): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        print("Result:", add(num1, num2))
    elif operator == '-':
        print("Result:", subtract(num1, num2))
    elif operator == '*':
        print("Result:", multiply(num1, num2))
    elif operator == '/':
        print("Result:", divide(num1, num2))
    elif operator == '%':
        print("Result:", modulus(num1, num2))
    else:
        print("Invalid operator. Please enter one of +, -, *, /, %.")

if __name__ == "__main__":
    main()