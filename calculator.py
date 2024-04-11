from tkinter import *

root = Tk()
root.title("Calculator")

# Creating function to enter number
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# Function to clear entry
def clear():
    entry.delete(0,END)

# Function to get first number and assign it globally
def add():
    first_num = entry.get()
    global num1
    global operation
    opaeration = "add"
    num1 = int(first_num)
    clear()

def difference():
    first_num = entry.get()
    global num1
    global operation
    operation = "sub"
    num1 = int(first_num)
    clear()

def multiply():
    first_num = entry.get()
    global num1
    global operation
    operation = "mul"
    num1 = int(first_num)
    clear()

def divide():
    first_num = entry.get()
    global num1
    global operation
    operation = "div"
    num1 = int(first_num)
    clear()

def equals():
    second_num = entry.get()
    global num2
    num2 = int(second_num)
    clear()
    if operation == "add":
        entry.insert(0, num1 + num2)
    elif operation == "sub":
        entry.insert(0, num1 - num2)
    elif operation == "mul":
        entry.insert(0, num1 * num2)
    elif operation == "div":
        entry.insert(0, num1 / num2)
    
# Data entry box
entry = Entry(root, width=30, borderwidth=5, )
entry.grid(row=0,column=0, columnspan=3, padx=10, pady=20)

# Button widgets
button1 = Button(root, text=1, width=5, borderwidth=3, command=lambda:button_click(1))
button2 = Button(root, text=2, width=5, borderwidth=3, command=lambda:button_click(2))
button3 = Button(root, text=3, width=5, borderwidth=3, command=lambda:button_click(3))
button4 = Button(root, text=4, width=5, borderwidth=3, command=lambda:button_click(4))
button5 = Button(root, text=5, width=5, borderwidth=3, command=lambda:button_click(5))
button6 = Button(root, text=6, width=5, borderwidth=3, command=lambda:button_click(6))
button7 = Button(root, text=7, width=5, borderwidth=3, command=lambda:button_click(7))
button8 = Button(root, text=8, width=5, borderwidth=3, command=lambda:button_click(8))
button9 = Button(root, text=9, width=5, borderwidth=3, command=lambda:button_click(9))
button0 = Button(root, text=0, width=5, borderwidth=3, command=lambda:button_click(0))

# Operation buttons
button_sum = Button(root, text="+", width=5, borderwidth=3, command=add)
button_diff = Button(root, text="-", width=5, borderwidth=3, command=difference)
button_mul = Button(root, text="*", width=5, borderwidth=3, command=multiply)
button_div = Button(root, text="/", width=5, borderwidth=3, command=divide)

# Equals and clear buttons
button_equals = Button(root, text="=", width=5, borderwidth=3, command=equals)
button_clear = Button(root, text="Clear", width=30, borderwidth=3, command=clear)

# Button positioning using grid
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0)

button_sum.grid(row=4, column=1)
button_diff.grid(row=4, column=2)
button_mul.grid(row=5, column=0)
button_div.grid(row=5, column=1)

button_equals.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

root.mainloop()