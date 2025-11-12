#arithmetic operations using conditions
a=int(input("a:"))
b=int(input("b:"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
 print(a+b)
elif(operation=="sub"):
 print(a-b)
elif(operation=="mul"):
 print(a*b)
elif(operation=="div"):
 print(a/b)
else:
 print("invalid operation")

 #Fibonacci Series using n terms
 n=int(input("Enter a number:"))
a,b=0,1
for i in range(n):
    print(a,end="")
    a,b=b,a+b

#reverse string 
a="chandru"
print(a[::-1])

#palindrome
a=input("Enter a string:")
if(a==a[::-1]):
    print("palindrime")
else:
    print("Not palindrome")

# initializing variables of different data types 
var_v = 18            # int 
var_w = 82.6          # float 
var_x = 'Tpoint Tech' # string 
var_y = True          # boolean 
var_z = [4, 1, 8, -5] # list 
 
# printing their types using type() function 
print(var_v, '->', type(var_w)) 
print(var_w, '->', type(var_v)) 
print(var_x, '->', type(var_x)) 
print(var_y, '->', type(var_y)) 
print(var_z, '->', type(var_z))

#length of string
a="chandru is a good boy"
word=a.split()
longest=max(word,key=len)
print(longest)
print("length:",len(longest))

#find longest term
a=input("Enter a string:")
long=a.split()
word=max(long,key=len)
print(word)

#swap two numbers
a=10
b=20
a,b=b,a
print("a:",a,"b:",b)

#factoril of number
a=int(input("Enter a number:"))
fact=1
for i in range(1,a+1):
    fact*=i
print(fact)

#find prime number
a=int(input("Enter a number:"))
if a>1:
    for i in range(2,int(a*0.5)+1):
        if(a%i==0):
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")

#find the Eligiblity
salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 and age<=25):
    loan=int(input("loan"))
    if(loan>50000):
        print("max loan is 50000")
    else:
     print("Eligible for loan")
else:
    print("Not Eligible for loan")

#find the average
a=int(input("tam:"))
b=int(input("eng:"))
c=int(input("mat:"))
d=int(input("sci:"))
e=int(input("soc:"))
f=(a+b+c+d+e/5)
if(f<175):
    print("fail")
else:
    print("pass")

#find the divisible number
a=int(input())
if(a%2==0 and a%4==0):
    print("a is divisible by 2 and 4")
else:
    print("a is not divisible by 2 and 4")

#find odd or even
a=int(input())
if(a%2==0):
    print("the num is even")
else:
    print("the num is odd")

#find the rank of student
stdn=int(input("mark:"))
if(stdn<=35):
    print("the stdnt is poor")
elif(stdn>=35 and stdn<=75):
    print("the stdnt is average")
elif(stdn>75 and stdn<100):
    print("the stdn is good")
else:
    print("invalid input")

#create a calculator using python
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

 
