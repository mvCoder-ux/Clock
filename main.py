from tkinter import *
from time import *

def update():
    time_string = strftime("Time: %H:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("Day: %A")
    day_label.config(text=day_string)

    date_string = strftime("Date: %B %d, %Y")
    date_label.config(text=date_string)

    root.after(1000,update)


root = Tk()

time_label = Label(root,font=("Arial",50),fg="#00FFFF",bg="black")
time_label.pack()

day_label = Label(root,font=("Comfortaa",50),fg="#00FFFF",bg="black", anchor='w')
day_label.pack()

date_label = Label(root,font=("Comfortaa",50),fg="#00FFFF",bg="black")
date_label.pack()

update()

root.mainloop()