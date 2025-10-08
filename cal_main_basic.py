def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else float('inf')
def remainder(a, b): return a % b if b != 0 else float('nan')
def power(a, b): return a ** b
def percentage(a, b): return (a / b) * 100 if b != 0 else float('nan')

def apply_operator(a, b, op):
    if op == '+': return add(a, b)
    elif op == '-': return subtract(a, b)
    elif op == '*': return multiply(a, b)
    elif op == '/': return divide(a, b)
    elif op == '%': return remainder(a, b)
    elif op == '^': return power(a, b)
    elif op == 'p': return percentage(a, b)
    else: return None

def calculator():
    print("Operators: + - * / % ^ p (percentage)")
    try:
        a = float(input("Enter first number: "))
        while True:
            op = input("Enter operator: ")
            if len(op) != 1:
                print("Invalid operator.")
                continue
            op = op[0]
            b = float(input("Enter next number: "))
            result = apply_operator(a, b, op)
            if result is None:
                print("Unknown operator.")
            else:
                a = result
                print("= ", a)
    except (KeyboardInterrupt, EOFError):
        print("\nCalculator exited.")
    except Exception as e:
        print("Error:", e)

calculator()
