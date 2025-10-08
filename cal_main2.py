import tkinter as tk
from fractions import Fraction
import math

class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.last_answer = ""
        self.expression_display = tk.StringVar()
        self.input_text = tk.StringVar()

        # Entry for expression display
        self.expression_label = tk.Label(root, textvariable=self.expression_display,
                                         anchor="e", font=("Arial", 14))
        self.expression_label.grid(row=0, column=0, columnspan=6, sticky="nsew")

        # Entry for main input
        self.entry = tk.Entry(root, textvariable=self.input_text, font=("Arial", 18), justify="right")
        self.entry.grid(row=1, column=0, columnspan=6, sticky="nsew")

        # Navigation index for digit highlight
        self.cursor_index = 0

        self.create_buttons()
        self.configure_grid()

    def configure_grid(self):
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(6):
            self.root.grid_columnconfigure(j, weight=1)

    def create_buttons(self):
        # Row 2: Control buttons
        tk.Button(self.root, text="Del", command=self.delete_digit).grid(row=2, column=4, sticky="nsew")
        tk.Button(self.root, text="Clear", command=self.clear).grid(row=2, column=5, sticky="nsew")
        tk.Button(self.root, text="Ans", command=lambda: self.insert_text(self.last_answer)).grid(row=2, column=0, sticky="nsew")
        tk.Button(self.root, text="◀", command=lambda: self.move_cursor(-1)).grid(row=2, column=1, sticky="nsew")
        tk.Button(self.root, text="▶", command=lambda: self.move_cursor(1)).grid(row=2, column=2, sticky="nsew")
        tk.Button(self.root, text="Frac↔Dec", command=self.toggle_fraction).grid(row=2, column=3, sticky="nsew")

        # Extra functions row (row 3)
        extras = [
            ("%", lambda: self.insert_text("%")),
            ("x^y", lambda: self.insert_text("**")),
            ("√", lambda: self.insert_text("**0.5")),
            ("³√", lambda: self.insert_text("**(1/3)")),
            ("sin", lambda: self.insert_text("math.sin(")),
            ("cos", lambda: self.insert_text("math.cos("))
        ]
        for i, (txt, cmd) in enumerate(extras):
            tk.Button(self.root, text=txt, command=cmd).grid(row=3, column=i, sticky="nsew")

        # Numbers
        numbers = [
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2),
            ("0", 7, 2), (".", 7, 0), ("00", 7, 1)
        ]
        for (txt, r, c) in numbers:
            tk.Button(self.root, text=txt, command=lambda t=txt: self.insert_text(t)).grid(row=r, column=c, sticky="nsew")

        # Operators
        ops = [
            ("+", lambda: self.insert_text("+")),
            ("-", lambda: self.insert_text("-")),
            ("×", lambda: self.insert_text("*")),
            ("÷", lambda: self.insert_text("/")),
        ]
        for i, (txt, cmd) in enumerate(ops):
            tk.Button(self.root, text=txt, command=cmd).grid(row=4+i, column=5, sticky="nsew")

        # Equals button
        tk.Button(self.root, text="=", command=self.calculate).grid(row=7, column=5, sticky="nsew")

    def insert_text(self, value):
        pos = self.entry.index(tk.INSERT)
        self.entry.insert(pos, str(value))
        self.highlight_digit(pos + len(str(value)))

    def move_cursor(self, direction):
        pos = self.entry.index(tk.INSERT) + direction
        pos = max(0, min(pos, len(self.entry.get())))
        self.highlight_digit(pos)

    def highlight_digit(self, pos):
        self.entry.icursor(pos)
        self.entry.selection_range(pos, pos+1)

    def delete_digit(self):
        pos = self.entry.index(tk.INSERT)
        text = self.entry.get()
        if text and pos < len(text):
            self.input_text.set(text[:pos] + text[pos+1:])
            self.highlight_digit(pos)

    def clear(self):
        self.input_text.set("")
        self.expression_display.set("")

    def toggle_fraction(self):
        try:
            val = self.entry.get()
            if "/" in val:  # Fraction to decimal
                frac = Fraction(val)
                self.input_text.set(str(float(frac)))
            else:  # Decimal to fraction
                dec = float(eval(val))
                self.input_text.set(str(Fraction(dec).limit_denominator()))
        except Exception:
            self.input_text.set("Error")

    def calculate(self):
        expr = self.entry.get()
        try:
            result = eval(expr, {"__builtins__": None}, math.__dict__)
            self.last_answer = str(result)
            self.expression_display.set(expr + " =")
            self.input_text.set(str(result))
        except Exception:
            self.input_text.set("Error")

root = tk.Tk()
app = AdvancedCalculator(root)
root.mainloop()
