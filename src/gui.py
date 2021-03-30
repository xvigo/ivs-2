from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk


button_color = "salmon2"


#initializing root window
root = Tk()
root.title("Gazorpazorpcalc")
root.configure(bg = "salmon3")
root.resizable(0, 0)

photo = PhotoImage(file = "/home/stepan/1bit/ivs/proj2/logofinal.png")
root.iconphoto(False, photo)

#adding logo
image = Image.open("/home/stepan/1bit/ivs/proj2/logofinal.png")
image = image.resize((110, 110))
photo = ImageTk.PhotoImage(image)


label = Label(root, image = photo)
label.image = photo
label.grid(row = 0, column = 0)


#Entry screen to display numbers and operations
t = Entry(root, width = 10, font = ('Helvetica', 50))
# input_text = StringVar()

# input_frame = Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)

# input_frame.pack(side = TOP)

# t = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)

t.grid(row = 0, column = 1, columnspan = 5)


#TODO
def button_add():
    return

#function to add buttonnumber to the entry
def button_num(number):
    current = t.get()
    t.delete(0, END)
    t.insert(0, str(current) + str(number))
    return

#creating number buttons
button_1 = Button(root, text = "1", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(1))
button_2 = Button(root, text = "2", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(2))
button_3 = Button(root, text = "3", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(3))
button_4 = Button(root, text = "4", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(4))
button_5 = Button(root, text = "5", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(5))
button_6 = Button(root, text = "6", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(6))
button_7 = Button(root, text = "7", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(7))
button_8 = Button(root, text = "8", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(8))
button_9 = Button(root, text = "9", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = lambda: button_num(9))
button_0 = Button(root, text = "0", bd = 0, bg = button_color, padx = 100, pady = 20, height = 2, width = 10, command = lambda: button_num(0))

#creating operations buttons
button_point = Button(root, text = ".", bd = 0, bg = button_color, padx = 50, pady = 20, height = 2, width = 5, command = button_add)
button_plus = Button(root, text = "+", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_minus = Button(root, text = "-", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_times = Button(root, text = "x", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_divide = Button(root, text= ":", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_equal = Button(root, text = "=", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_power = Button(root, text = "^", bd = 0, bg = button_color, padx = 48, pady = 20, height = 2, width = 5, command = button_add)
button_root = Button(root, text = "√", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_abs = Button(root, text = "ABS", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_del = Button(root, text = "DEL", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_ac = Button(root, text = "AC", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_ce = Button(root, text = "CE", bd = 0, bg = button_color, padx = 49, pady = 20, height = 2, width = 5, command = button_add)
button_fact = Button(root, text = "!", bd = 0, bg = button_color, padx = 50, pady = 20, height = 2, width = 5, command = button_add)


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





