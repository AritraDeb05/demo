import tkinter as tk
from tkinter import ttk
from fractions import Fraction
import math

class StyledCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator - Modern")
        self.last_answer = ""
        self.expression_display = tk.StringVar()
        self.input_text = tk.StringVar()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 14), padding=6)
        style.configure("TEntry", font=("Arial", 18))
        style.configure("Display.TLabel", font=("Arial", 14), anchor="e")

        ttk.Label(root, textvariable=self.expression_display, style="Display.TLabel").grid(row=0, column=0, columnspan=6, sticky="nsew")
        self.entry = ttk.Entry(root, textvariable=self.input_text, justify="right")
        self.entry.grid(row=1, column=0, columnspan=6, sticky="nsew")

        self.configure_grid()
        self.create_buttons()

    def configure_grid(self):
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(6):
            self.root.grid_columnconfigure(j, weight=1)

    def make_btn(self, text, cmd, r, c):
        ttk.Button(self.root, text=text, command=cmd).grid(row=r, column=c, sticky="nsew")

    def create_buttons(self):
        self.make_btn("Del", self.delete_digit, 2, 4)
        self.make_btn("Clear", self.clear, 2, 5)
        self.make_btn("Ans", lambda: self.insert_text(self.last_answer), 2, 0)
        self.make_btn("◀", lambda: self.move_cursor(-1), 2, 1)
        self.make_btn("▶", lambda: self.move_cursor(1), 2, 2)
        self.make_btn("Frac↔Dec", self.toggle_fraction, 2, 3)

        extras = [
            ("%", lambda: self.insert_text("%")),
            ("x^y", lambda: self.insert_text("**")),
            ("√", lambda: self.insert_text("**0.5")),
            ("³√", lambda: self.insert_text("**(1/3)")),
            ("sin", lambda: self.insert_text("math.sin(")),
            ("cos", lambda: self.insert_text("math.cos("))
        ]
        for i, (txt, cmd) in enumerate(extras):
            self.make_btn(txt, cmd, 3, i)

        numbers = [
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2),
            (".", 7, 0), ("00", 7, 1), ("0", 7, 2)
        ]
        for (txt, r, c) in numbers:
            self.make_btn(txt, lambda t=txt: self.insert_text(t), r, c)

        ops = [
            ("+", lambda: self.insert_text("+")),
            ("-", lambda: self.insert_text("-")),
            ("×", lambda: self.insert_text("*")),
            ("÷", lambda: self.insert_text("/")),
        ]
        for i, (txt, cmd) in enumerate(ops):
            self.make_btn(txt, cmd, 4+i, 5)

        self.make_btn("=", self.calculate, 7, 5)

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
            if "/" in val:
                frac = Fraction(val)
                self.input_text.set(str(float(frac)))
            else:
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
app = StyledCalculator(root)
root.mainloop()
