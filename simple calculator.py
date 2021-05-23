# python code for simple calculator...
from tkinter import *

root = Tk()
# window title
root.title("Calculator")

#input field
e= Entry(root, width=45, borderwidth=3, fg='white', bg='black')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#defining operation of the buttons on pressing

#def all number button operation
def button_click(number):
    fnum= e.get()
    e.delete(0, END)
    e.insert(0, str(fnum)+ str(number))

# AC button for clearing the screen
def button_clear():
    e.delete(0, END)

# addition operation
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)
   
# subtraction operation
def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

# multiplication operation
def button_multi():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

# division operation
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = float(first_number)
    e.delete(0, END)

#squaring the number
def button_square():
    first_number = e.get()
    global f_num
    global math
    math = "square"
    f_num = float(first_number)
    e.delete(0, END)

# cubing the number
def button_cube():
    first_number = e.get()
    global f_num
    global math
    math = "cube"
    f_num = float(first_number)
    e.delete(0, END)

#percentage
def button_percentage():
    first_number = e.get()
    global f_num
    global math
    math = "percentage"
    f_num = float(first_number)
    e.delete(0, END)

# defining the button to round of decimal number
def button_uroot():
    first_number = e.get()
    global f_num
    global math
    math = "uroot"
    f_num = float(first_number)
    e.delete(0, END)
    
def button_equal():
    secound_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(secound_number))
    if math == "subtraction":
        e.insert(0, f_num - float(secound_number))
    if math == "multiplication":
        e.insert(0, f_num * float(secound_number))
    if math == "divide":
        e.insert(0, f_num / float(secound_number))
    if math == "percentage":
        e.insert(0, (f_num/100) * float(secound_number))
    if math == "square":
        e.insert(0, f_num * f_num)
    if math == "cube":
        e.insert(0, f_num * f_num * f_num)
    if math == "uroot":
        e.insert(0, round(f_num))


    
#define buttons
button_1 = Button(root, text="1", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx= 30, pady=20, activebackground="#F2EB4C", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx= 67, pady=20, activebackground="#F2EB4C", command=lambda: button_click(0))
button_point = Button(root, text=".", padx= 31, pady=20, activebackground="#F2EB4C", command=lambda: button_click("."))
button_add = Button(root, text="+", padx= 30, pady=20, activebackground="#F2EB4C", command= button_add)
button_minus = Button(root, text="-", padx= 30, pady=20, activebackground="#F2EB4C", command=button_minus)
button_multi = Button(root, text="X", padx= 30, pady=20, activebackground="#F2EB4C", command=button_multi)
button_divide = Button(root, text="÷", padx= 30, pady=20, activebackground="#F2EB4C", command=button_divide)
# function other than simple calculator
button_percentage = Button(root, text="%", padx= 29, pady=20,activebackground="#F2EB4C", command=button_percentage)
button_square = Button(root, text="x²", padx= 28, pady=20, activebackground="#F2EB4C", command=button_square)
button_cube = Button(root, text="x³", padx= 28, pady=20, activebackground="#F2EB4C", command=button_cube)
button_uroot = Button(root, text="D⇒S", padx= 20, pady=20, activebackground="#F2EB4C", command=button_uroot)
# equal to button
button_equal = Button(root, text="=", fg='white', bg='orange', activebackground="#EF772E", padx= 67, pady=20, command=button_equal)
#clear screen button
button_clear = Button(root, text="AC",fg='orange', padx= 62, pady=20, activebackground="#EF772E", command=button_clear)

#putting buttons on screen
# row 2 and 3 are empty for future extension
button_clear.grid(row=4,column=0, columnspan=2)
button_uroot.grid(row=4,column=2)
button_percentage.grid(row=4,column=3)
button_point.grid(row=5,column=0)
button_square.grid(row=5,column=1)
button_cube.grid(row=5,column=2)
button_divide.grid(row=5,column=3)
button_7.grid(row=6,column=0)
button_8.grid(row=6,column=1)
button_9.grid(row=6,column=2)
button_multi.grid(row=6,column=3)
button_4.grid(row=7,column=0)
button_5.grid(row=7,column=1)
button_6.grid(row=7,column=2)
button_minus.grid(row=7,column=3)
button_1.grid(row=8,column=0)
button_2.grid(row=8,column=1)
button_3.grid(row=8,column=2)
button_add.grid(row=8,column=3)
button_0.grid(row=9,column=0, columnspan=2)
button_equal.grid(row=9,column=2, columnspan=2)

#for window operation.
root.mainloop()
