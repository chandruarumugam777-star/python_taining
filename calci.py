import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#222")

# Global expression string
expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

# Function to clear expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Create a text variable for the display
equation = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvariable=equation, font=('Arial', 24), bd=10, bg="#333", fg="#fff", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=20, sticky="nsew")

# Button design helper
def create_button(text, row, col, command, colspan=1):
    btn = tk.Button(root, text=text, font=('Arial', 18), bg="#444", fg="#fff", command=command)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2, ipadx=10, ipady=20)

# Button layout
buttons = [
    ('C', 1, 0, clear),
    ('%', 1, 1, lambda: press('%')),
    ('/', 1, 2, lambda: press('/')),
    ('*', 1, 3, lambda: press('*')),
    ('7', 2, 0, lambda: press('7')),
    ('8', 2, 1, lambda: press('8')),
    ('9', 2, 2, lambda: press('9')),
    ('-', 2, 3, lambda: press('-')),
    ('4', 3, 0, lambda: press('4')),
    ('5', 3, 1, lambda: press('5')),
    ('6', 3, 2, lambda: press('6')),
    ('+', 3, 3, lambda: press('+')),
    ('1', 4, 0, lambda: press('1')),
    ('2', 4, 1, lambda: press('2')),
    ('3', 4, 2, lambda: press('3')),
    ('=', 4, 3, equalpress),
    ('0', 5, 0, lambda: press('0')),
    ('.', 5, 1, lambda: press('.')),
]

# Generate buttons
for (text, row, col, cmd) in buttons:
    create_button(text, row, col, cmd)

# Adjust grid weight
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Start the GUI
root.mainloop()
