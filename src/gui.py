from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font as tkFont

button_color = "#424242"

hbgc = "#303030"

padx_size = 26
pady_size = 8


#initializing root window
root = Tk()
root.title("Gazorpazorpcalc")
root.configure(bg = "#303030")
root.resizable(0, 0)




myFont = tkFont.Font(family = 'Helvetica', size = 22, weight = 'bold')

#adding logo
#must change line 28 according to local device

image = Image.open("/home/stepan/1bit/ivs/proj2/git/ivs-2/src/logo.png")
image = image.resize((110, 110))
photo = ImageTk.PhotoImage(image)


label = Label(root, image = photo, borderwidth = 0)
label.image = photo
label.grid(row = 0, column = 0)


#Entry screen to display numbers and operations
t = Entry(root, width = 10, font = ('Helvetica', 50))
# input_text = StringVar()

# input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)

# input_frame.pack(side = TOP)

# t = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)

t.grid(row = 0, column = 1, columnspan = 5)



#function to add buttonnumber to the entry
def button_num(foo):
    current = t.get()
    t.delete(0, END)
    t.insert(0, str(current) + str(foo))
    return

#creating number buttons
button_g = Button(root, text = "1", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(1))
button_1 = button_g
button_2 = Button(root, text = "2", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(2))
button_3 = Button(root, text = "3", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(3))
button_4 = Button(root, text = "4", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(4))
button_5 = Button(root, text = "5", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(5))
button_6 = Button(root, text = "6", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(6))
button_7 = Button(root, text = "7", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(7))
button_8 = Button(root, text = "8", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(8))
button_9 = Button(root, text = "9", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(9))
button_0 = Button(root, text = "0", font = myFont, bd = 0, highlightbackground = hbgc, bg = button_color, padx = 70, pady = 8, height = 2, width = 8, command = lambda: button_num(0))

#creating operations buttons
button_point = Button(root, text = ".", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("."))
button_plus = Button(root, text = "+", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("+"))
button_minus = Button(root, text = "-", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("-"))
button_times = Button(root, text = "x", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("x"))
button_divide = Button(root, text= ":", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num(":"))
button_equal = Button(root, text = "=", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("="))
button_power = Button(root, text = "^", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("√"))
button_root = Button(root, text = "√", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num())
button_abs = Button(root, text = "ABS", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num())
button_del = Button(root, text = "DEL", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num)
button_ac = Button(root, text = "AC", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num)
button_ce = Button(root, text = "CE", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num)
button_fact = Button(root, text = "!", font = myFont,bd = 0, highlightbackground = hbgc, bg = button_color, padx = padx_size, pady = pady_size, height = 2, width = 5, command = lambda: button_num("!"))



#griding buttons to the root window
button_abs.grid(row = 1, column = 0)
button_ac.grid(row = 1, column = 1)
button_ce.grid(row = 1, column = 2)
button_del.grid(row = 1, column = 3)

button_power.grid(row = 2, column = 0)
button_root.grid(row = 2, column = 1)
button_fact.grid(row = 2, column = 2)
button_divide.grid(row = 2, column = 3)

button_7.grid(row = 3, column = 0)
button_8.grid(row = 3, column = 1)
button_9.grid(row = 3, column = 2)
button_times.grid(row = 3, column = 3)

button_4.grid(row = 4, column = 0)
button_5.grid(row = 4, column = 1)
button_6.grid(row = 4, column = 2)
button_minus.grid(row = 4, column = 3)

button_1.grid(row = 5, column = 0)
button_2.grid(row = 5, column = 1)
button_3.grid(row = 5, column = 2)
button_plus.grid(row = 5, column = 3)

button_0.grid(row = 6, column = 0, columnspan = 2)
button_point.grid(row = 6, column = 2)
button_equal.grid(row = 6, column = 3)


root.mainloop()





