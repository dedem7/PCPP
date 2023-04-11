from tkinter import *
import random

window=Tk()

window.resizable(width=False, height=False)
window.geometry("500x500")

window.title("Catch me!")

button=Button(window, text="Catch me!",width=10,height=1)

button.place(x=0,y=0)
def func(event=None):
    x_coor=random.randint(0,420)
    y_coor=random.randint(0,470)

    #window.update()
    while abs(x_coor-button.winfo_x())<20 or abs(y_coor-button.winfo_y())<20:
        x_coor=random.randint(button.winfo_x(),420)
        y_coor=random.randint(button.winfo_y(),470)

    button.place(x=x_coor,y=y_coor)
    
    

button.bind("<Enter>",func)



window.mainloop()
