import os
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font as tkFont
from LibMath import *

button_color = "#424242"

#highlight backhround color
hbgc = "#303030"

#under cursor color
active_color = "#323232"

#font color
fg_color = "#606060"

padx_size = 26
pady_size = 8


#initializing root window
root = Tk()
root.title("Gazorpazorpcalc")
root.configure(bg = "#303030")
root.resizable(0, 0)

path = os.path.realpath(__file__).rsplit('/', 1)
logo_location = path[0] + "/logo.png"

myFont = tkFont.Font(family = 'Helvetica', size = 22, weight = 'bold')

#adding logo
#must change line 28 according to local device

image = Image.open(logo_location)
image = image.resize((110, 110))
photo = ImageTk.PhotoImage(image)


label = Label(root, image = photo, borderwidth = 0)
label.image = photo
label.grid(row = 0, column = 0, rowspan = 2)


#Entry screen to display numbers and operations
t = Entry(root,justify = LEFT, width = 25, bg = "#303030", bd = 0, highlightbackground = hbgc, font = ('Helvetica', 20))
# input_text = StringVar()

# input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)

# input_frame.pack(side = TOP)

# t = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)



t2 = Entry(root,justify = RIGHT, width = 15, bg = "#404040", bd = 0, highlightbackground = hbgc, font = ('Helvetica', 35))

t2.grid(row = 1, column = 1, columnspan = 5, sticky = N)
t.grid(row = 0, column = 1, columnspan = 5, sticky = S)

ans = 1
#function to add buttonnumber to the entry

def b_num(new):
    global ans
    if ans == 0:
       b_clear_empty()
    current = t2.get()
    t2.delete(0, END)
    formula = str(current) + str(new)
    t2.insert(0, formula)
    ans = 1
    return

def b_operator(new):
    global ans
    current = t2.get()
    t2.delete(0, END)
    formula = str(current) + str(new)
    t2.insert(0, formula)
    ans = 1
    return

def b_equal():
    global ans
    expr = t2.get()
    t.delete(0, END)
    result = solve_expr(expr)

    t.delete(0, END)
    t.insert(0, str(expr)+str(" = "))
    t2.delete(0, END)
    t2.insert(0, str(result))
    ans = 0
    return
def b_delete():
    index = len(t2.get()) - 1
    t2.delete(index, END)
    return
def b_clear_empty():
    t2.delete(0, END)
    t.delete(0, END)
    return

def b_abs():
    val = t2.get()
    t2.delete(0, END)
    t2.insert(0, str(abs(solve_expr(val))))
    return

#creating number
button_1 = Button(root, text = "1", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(1))
button_2 = Button(root, text = "2", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(2))
button_3 = Button(root, text = "3", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(3))
button_4 = Button(root, text = "4", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(4))
button_5 = Button(root, text = "5", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(5))
button_6 = Button(root, text = "6", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(6))
button_7 = Button(root, text = "7", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(7))
button_8 = Button(root, text = "8", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(8))
button_9 = Button(root, text = "9", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(9))
button_0 = Button(root, text = "0", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = 70, pady = 8, height = 2, width = 8, command = lambda: b_num(0))

#creating operations buttons
button_point = Button(root, text = ".", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("."))
button_plus = Button(root, text = "+", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("+"))
button_minus = Button(root, text = "-", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("-"))
button_times = Button(root, text = "*", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("*"))
button_divide = Button(root, text= "/", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("/"))
button_equal = Button(root, text = "=", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_equal())
button_power = Button(root, text = "^", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("^"))
button_root = Button(root, text = "√", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("√"))
button_abs = Button(root, text = "ABS", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_abs())
button_del = Button(root, text = "DEL", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_delete())
button_ac = Button(root, text = "AC", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_clear_empty())
button_ce = Button(root, text = "CE", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("FIXME"))
button_fact = Button(root, text = "!", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("!"))



#griding buttons to the root window
button_abs.grid(row = 2, column = 0)
button_ac.grid(row = 2, column = 1)
button_ce.grid(row = 2, column = 2)
button_del.grid(row = 2, column = 3)

button_power.grid(row = 3, column = 0)
button_root.grid(row = 3, column = 1)
button_fact.grid(row = 3, column = 2)
button_divide.grid(row = 3, column = 3)

button_7.grid(row = 4, column = 0)
button_8.grid(row = 4, column = 1)
button_9.grid(row = 4, column = 2)
button_times.grid(row = 4, column = 3)

button_4.grid(row = 5, column = 0)
button_5.grid(row = 5, column = 1)
button_6.grid(row = 5, column = 2)
button_minus.grid(row = 5, column = 3)

button_1.grid(row = 6, column = 0)
button_2.grid(row = 6, column = 1)
button_3.grid(row = 6, column = 2)
button_plus.grid(row = 6, column = 3)

button_0.grid(row = 7, column = 0, columnspan = 2)
button_point.grid(row = 7, column = 2)
button_equal.grid(row = 7, column = 3)


root.mainloop()





