from tkinter import Tk, Button, Canvas



phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))


# Write your code here.
window=Tk()

window.resizable(width=False,height=False)
window.geometry("150x430")

canvas = Canvas(window, width=145,height=370, bg="grey")
canvas.create_oval(15,5,135,120)
canvas.create_oval(15,126,135,240)
canvas.create_oval(15,247,135,360)



d=("red","yellow","green")

click=0

def switch_light():
    global click
    colors = list(map(lambda x, y: x * y or 'gray', ("red","yellow","green"), phases[click]))
    canvas.create_oval(15,5,135,120,fill=colors[0]) 
    canvas.create_oval(15,126,135,240, fill=colors[1]) 
    canvas.create_oval(15,247,135,360, fill =colors[2])
    if click==len(phases)-1:
        click=0
    else:
        click+=1

button_next = Button(window, text="Next",command=switch_light)
button_quit = Button(window, text="Quit",command=window.destroy)
    
    
canvas.grid(row=0)
button_next.grid(row=1)
button_quit.grid(row=2)

window.mainloop()

