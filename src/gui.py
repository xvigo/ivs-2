import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font as tkFont
import LibProcExpr as pe

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
root = tk.Tk()
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


label = tk.Label(root, image = photo, borderwidth = 0)
label.image = photo
label.grid(row = 0, column = 0, rowspan = 2)


#Entry screen to display history
t = tk.Entry(root,justify = tk.LEFT, width = 25, bg = "#303030", bd = 0, highlightbackground = hbgc, font = ('Helvetica', 20))


def validCheck(action, char):
    if action == '0':
        return True
    global ans_displayed
    allowed = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "/", "*", "-", "+", "^", "%", "!", "√"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]


    for i in char:
        if i not in allowed:
            return False

    if i in nums and ans_displayed:
        t2.delete(0, tk.END)
        t2.insert(tk.END, char)
        t2.after_idle(lambda: t2.configure(validate="all"))
    ans_displayed = False
    return True


#Entry screen to display current input
VC = root.register(validCheck)
t2 = tk.Entry(root, justify = tk.RIGHT, validate='key', validatecommand=(VC, '%d', '%S'), width = 15, bg = "#404040", bd = 0, highlightbackground = hbgc, font = ('Helvetica', 35))
t2.focus_set()
t2.grid(row = 1, column = 1, columnspan = 5, sticky = tk.N)
t.grid(row = 0, column = 1, columnspan = 5, sticky = tk.S)

ans_displayed = False
glob_result = ""
#function to add buttonnumber to the entry

def b_num(new):
    global ans_displayed
    if ans_displayed == True:
       b_clear_empty()
    current = t2.get()
    t2.delete(0, tk.END)
    formula = str(current) + str(new)
    t2.insert(0, formula)
    ans_displayed = False
    return

def b_operator(new):
    global ans_displayed
    current = t2.get()
    t2.delete(0, tk.END)
    formula = str(current) + str(new)
    t2.insert(0, formula)
    ans_displayed = False
    return

def b_equal(event=None):
    global ans_displayed
    global glob_result
    expr = t2.get()
    if len(expr) == 0:
        return

    result = pe.solve_expr(expr)
    glob_result = result
    t.delete(0, tk.END)
    t.insert(0, str(expr)+str(" = "))
    t2.delete(0, tk.END)
    t2.insert(0, str(result))
    ans_displayed = True
    return

root.bind('<Return>', b_equal)
root.bind('<KP_Enter>', b_equal)
def b_delete():
    index = len(t2.get()) - 1
    t2.delete(index, tk.END)
    return
def b_clear_empty():
    t2.delete(0, tk.END)
    t.delete(0, tk.END)
    return

#UNUSED!
"""
def b_abs(event):
    val = t2.get()
    t2.delete(0, tk.END)
    t2.insert(0, str(abs(pe.solve_expr(val))))
    return
"""
#creating number
button_1 = tk.Button(root, text = "1", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(1))
button_2 = tk.Button(root, text = "2", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(2))
button_3 = tk.Button(root, text = "3", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(3))
button_4 = tk.Button(root, text = "4", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(4))
button_5 = tk.Button(root, text = "5", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(5))
button_6 = tk.Button(root, text = "6", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(6))
button_7 = tk.Button(root, text = "7", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(7))
button_8 = tk.Button(root, text = "8", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(8))
button_9 = tk.Button(root, text = "9", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(9))
button_0 = tk.Button(root, text = "0", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = 70, pady = 8, height = 2, width = 8, command = lambda: b_num(0))

#creating operations buttons
button_point = tk.Button(root, text = ".", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("."))
button_plus = tk.Button(root, text = "+", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("+"))
button_minus = tk.Button(root, text = "-", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("-"))
button_times = tk.Button(root, text = "*", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("*"))
button_divide = tk.Button(root, text= "/", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("/"))
button_equal = tk.Button(root, text = "=", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_equal())
button_power = tk.Button(root, text = "^", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("^"))
button_root = tk.Button(root, text = "√", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num("√"))
button_ans = tk.Button(root, text = "ANS", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_num(glob_result))
button_del = tk.Button(root, text = "DEL", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_delete())
button_ac = tk.Button(root, text = "AC", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_clear_empty())
button_mod = tk.Button(root, text = "MOD", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("%"))
button_fact = tk.Button(root, text = "!", font = myFont, activebackground = active_color, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: b_operator("!"))



#griding buttons to the root window
button_ans.grid(row = 2, column = 0)
button_mod.grid(row = 2, column = 1)
button_ac.grid(row = 2, column = 2)
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





