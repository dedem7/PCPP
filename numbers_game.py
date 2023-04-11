import tkinter as tk
from random import randint

window=tk.Tk()

window.resizable(width=False, height=False)
window.geometry("400x150")
window.title("    Clicker")


buttons=[[tk.Button(window,text=str(randint(0,1000)),width=10, height=1) for i in range(5)]for j in range(5)]
label=tk.Label(window,text="0", width=10, anchor="center", justify=tk.CENTER)

c=0
a=True
#----grid
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        buttons[i][j].grid(row=j,column=i)

label.grid(row=5,column=2)

numbers=[int(n.cget("text")) for m in buttons for n in m]



def deactivate(*args):
    global a
    if a:
        label.after(999,counter)
    a=False
    for i in [n for m in buttons for n in m]:
        if i.cget("state")!=tk.DISABLED:
            if i.cget("state")==tk.ACTIVE and int(i.cget("text"))==min(numbers):
                numbers.remove(int(i.cget("text")))
                i.config(state=tk.DISABLED)
            else:
                i.config(state=tk.NORMAL)
    
 
def counter():
    global c
    if len(numbers)==0:
        label.after_cancel(counter)
    else:
        c+=1
        label.config(text=str(c))
        label.after(999,counter)
        

window.bind("<Button-1>", deactivate)


window.mainloop()
