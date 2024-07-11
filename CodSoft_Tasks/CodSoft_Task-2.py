import tkinter as tk
from tkinter import messagebox

def calculate():
   try:
      num1 = float(entry_num1.get())
      num2 = float(entry_num2.get())
      operation = variable.get()

      if operation == "+":
         result = num1 + num2
      elif operation == "-":
         result = num1 - num2
      elif operation == "*":
         result = num1 * num2
      elif operation == "/":
         if num2 != 0:
            result = num1 / num2
         else:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return

      label_result.config(text="Result: " + str(result))

   except ValueError:
      messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Number 1:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Number 2:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

variable = tk.StringVar(root)
variable.set("+")

option_add = tk.Radiobutton(root, text="+", variable=variable, value="+")
option_add.pack()

option_subtract = tk.Radiobutton(root, text="-", variable=variable, value="-")
option_subtract.pack()

option_multiply = tk.Radiobutton(root, text="*", variable=variable, value="*")
option_multiply.pack()

option_divide = tk.Radiobutton(root, text="/", variable=variable, value="/")
option_divide.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()