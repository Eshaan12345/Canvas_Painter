from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("Canvas Painter")
root.configure(background="gray25")

canvas = Canvas(root, width=870, height=440)
canvas.place(relx=0.5, rely=0.38, anchor=CENTER)

startx_label = Label(root, text="Start X")
startx_label.place(relx=0.05, rely=0.85, anchor=CENTER)

startx_entry = Entry(root, width=10)
startx_entry.place(relx=0.12, rely=0.85, anchor=CENTER)

starty_label = Label(root, text = "Start Y")
starty_label.place(relx = 0.05, rely = 0.9, anchor = CENTER)

starty_entry = Entry(root, width = 10)
starty_entry.place(relx = 0.12, rely = 0.9, anchor = CENTER)

endx_label = Label(root, text = "End X")
endx_label.place(relx = 0.2, rely = 0.85, anchor = CENTER)

endx_entry = Entry(root, width = 10)
endx_entry.place(relx = 0.28, rely = 0.85, anchor = CENTER)

endy_label = Label(root, text = "End Y")
endy_label.place(relx = 0.2, rely = 0.9, anchor = CENTER)

endy_entry = Entry(root, width = 10)
endy_entry.place(relx = 0.28, rely = 0.9, anchor = CENTER)

color_label = Label(root, text="Color")
color_label.place(relx=0.4, rely=0.87, anchor=CENTER)

color_var = StringVar()
color_dropdown = ttk.Combobox(root, values=["Black", "Blue", "Green", "Red", "Yellow", "Orange", "Purple", "Pink"], textvariable=color_var)
color_dropdown.place(relx=0.52, rely=0.87, anchor=CENTER)

shape_var = StringVar()
shape_dropdown = ttk.Combobox(root, values=["Circle", "Rectangle", "Line"], textvariable=shape_var)
shape_dropdown.place(relx=0.72, rely=0.87, anchor=CENTER)


def draw():
    startx = int(startx_entry.get())
    starty = int(starty_entry.get())
    endx = int(endx_entry.get())
    endy = int(endy_entry.get())
        
    shape = shape_var.get()
    color = color_var.get()
        
    if shape == "Rectangle":
        canvas.create_rectangle(startx, starty, endx, endy, fill=color)
    elif shape == "Circle":
        canvas.create_oval(startx, starty, endx, endy, fill=color)
    elif shape == "Line":
        canvas.create_line(startx, starty, endx, endy, fill=color, width=3)


button = Button(root, text="Draw", command=draw)
button.place(relx=0.9, rely=0.85, anchor=CENTER)

root.mainloop()
