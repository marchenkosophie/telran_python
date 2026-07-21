

def calculate(a:float, b:float, op:str):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b #ZeroDivisionError if b==0
    else:
        raise ValueError("Invalid operation")

#MIDDLE LEVEL - parsing. Convert string into numbers

def pars_and_calc(a_str, b_str, op:str):
    a = float(a_str) # ValueError if not a number
    b = float(b_str) # ValueError if not a number
    return calculate(a, b, op)

# TOP LEVEL - dialogue. It captures everything and explains it to the user

def run_calculator():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        op = input("Enter Action (+, -, *, /): ")
        result = pars_and_calc(a, b, op)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Invalid data: {e}")
    except ZeroDivisionError:
        print("Cannot divide by zero")


# run_calculator()


def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False


print(is_number("1"))
print(is_number("2.7"))
print(is_number("2,7"))


try:
    value = int("25")
except ValueError:
    print("This is not a number")
else:
    print("The transformation was successful", value)
finally:
    print("This block is always executed")