import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
import math

# --------- FUNCTIONS ---------
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current)-1, tk.END)

def insert_val(val):
    entry.insert(tk.END, val)

def remainder():
    try:
        nums = entry.get().split()
        if len(nums) == 2:
            result = int(nums[0]) % int(nums[1])
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            messagebox.showerror("Error", "Enter two numbers separated by space")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def power():
    try:
        nums = entry.get().split()
        if len(nums) == 2:
            result = float(nums[0]) ** float(nums[1])
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            messagebox.showerror("Error", "Enter base and exponent separated by space")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def nth_root():
    try:
        nums = entry.get().split()
        if len(nums) == 2:
            result = float(nums[0]) ** (1 / float(nums[1]))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            messagebox.showerror("Error", "Enter number and root value separated by space")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def factorial():
    try:
        num = int(entry.get())
        result = math.factorial(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def logarithm():
    try:
        num = float(entry.get())
        result = math.log(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def trig(func):
    try:
        num = math.radians(float(entry.get()))
        if func == "sin":
            result = math.sin(num)
        elif func == "cos":
            result = math.cos(num)
        elif func == "tan":
            result = math.tan(num)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def reciprocal():
    try:
        num = float(entry.get())
        result = 1 / num
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero!")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def toggle_fraction():
    try:
        val = entry.get()
        if "/" in val:  # Fraction → Decimal
            result = float(Fraction(val))
        else:  # Decimal → Fraction
            result = Fraction(val).limit_denominator()
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# --------- UI SETUP ---------
root = tk.Tk()
root.title("Advanced Handy Calculator")
root.geometry("600x700")
root.resizable(True, True)  # Allow resizing

# Configure grid for dynamic resizing
for i in range(10):  # Adjust for enough rows
    root.rowconfigure(i, weight=1)
for j in range(5):  # Adjust for enough columns
    root.columnconfigure(j, weight=1)

# Entry field
entry = tk.Entry(root, font=("Arial", 22), justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Top Right: Clear & Delete
tk.Button(root, text="C", command=clear, font=("Arial", 12, "bold")).grid(row=1, column=3, padx=2, pady=2, sticky="nsew")
tk.Button(root, text="⌫", command=backspace, font=("Arial", 12, "bold")).grid(row=1, column=4, padx=2, pady=2, sticky="nsew")

# Special operations (2 rows)
special_ops = [
    ("%", remainder), ("x^y", power), ("√n", nth_root), ("n!", factorial), ("log", logarithm),
    ("1/x", reciprocal), ("Frac↔Dec", toggle_fraction), ("sin", lambda: trig("sin")),
    ("cos", lambda: trig("cos")), ("tan", lambda: trig("tan"))
]
row, col = 2, 0
for text, cmd in special_ops:
    tk.Button(root, text=text, command=cmd, font=("Arial", 12)).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
    col += 1
    if col > 4:
        col = 0
        row += 1

# Number buttons (bottom-left)
numbers = [
    ("7", "7"), ("8", "8"), ("9", "9"),
    ("4", "4"), ("5", "5"), ("6", "6"),
    ("1", "1"), ("2", "2"), ("3", "3"),
    ("00", "00"), ("0", "0"), (".", ".")
]
start_row = row
r, c = start_row, 0
for text, val in numbers:
    tk.Button(root, text=text, command=lambda v=val: insert_val(v), font=("Arial", 12)).grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
    c += 1
    if c > 2:
        c = 0
        r += 1

# Operators on right side
operators = [
    ("/", "/"), ("*", "*"), ("-", "-"), ("+", "+"), ("=", None)
]
op_row = start_row
for text, val in operators:
    cmd = calculate if text == "=" else lambda v=val: insert_val(v)
    tk.Button(root, text=text, command=cmd, font=("Arial", 14, "bold")).grid(row=op_row, column=4, padx=2, pady=2, sticky="nsew")
    op_row += 1

root.mainloop()
