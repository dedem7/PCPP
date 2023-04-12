import tkinter as tk
from tkinter import messagebox
from random import randrange


wnd = tk.Tk()
wnd.title("TicTacToe")
wnd.resizable(width=False, height=False)
wnd.geometry("")


buttons = []
flat_buttons_list = []
def create_buttons():
    global buttons
    global flat_buttons_list
    buttons=[[tk.Button(wnd,width=5, height=2, text="",font= ('Arial 25 bold')) for i in range(3)]for j in range(3)]
    flat_buttons_list=[b for item in buttons for b in item]
    
    #--grid:
    for i in range(len(buttons)):
        for j in range(len(buttons[i])):
            buttons[i][j].grid(row=i,column=j)

    
def turn(*args):
    clicked=False 
    #'X'
    for b in flat_buttons_list:
        if b.cget("state")==tk.ACTIVE and b.cget("text")=="":
            b.config(text=("X"))
            b.config(fg=("red"))
            flat_buttons_list.remove(b)
            clicked=True
            if winner_message():
                return True
                   
    #'O'
    if clicked:
        position = randrange(0,len(flat_buttons_list))
        flat_buttons_list[position].config(text=("O"))
        flat_buttons_list[position].config(fg=("green"))
        del flat_buttons_list[position]
        winner_message()
    
    #Draw
    if len(flat_buttons_list)==0:
        messagebox.showinfo("Game Over!", "Draw!")
        clear_all()

#winner check    
def winner():
    x_o=[[a.cget("text") for a in b]for b in buttons]
    win1=x_o[0]
    win2=x_o[1]
    win3=x_o[2]
    win4=[i[0] for i in x_o]
    win5=[i[1] for i in x_o]
    win6=[i[2] for i in x_o]
    win7=[x_o[i][i] for i in range(len(x_o))]
    win8=[x_o[i][2-i] for i in range(len(x_o))]
    
    if ["X","X","X"] in [win1,win2,win3,win4,win5,win6,win7,win8]:
        return True
    elif ["O","O","O"] in [win1,win2,win3,win4,win5,win6,win7,win8]:
        return False
    else:
        return None

def winner_message():
    if winner() is True:
        messagebox.showinfo("Game Over!", "I won!")
        clear_all()
        return True
    elif winner() is False:
        messagebox.showinfo("Game Over!", "Computer won!")
        clear_all()
        return False
    else:
        pass

def clear_all():
    for w in [b for item in buttons for b in item]:
        w.grid_forget()
    create_buttons()
    flat_buttons_list[4].config(text=("O"), fg = "green")
    del flat_buttons_list[4]


#GAME START:
create_buttons()    
flat_buttons_list[4].config(text=("O"), fg = "green")
del flat_buttons_list[4]

wnd.bind("<Button-1>",turn)

                          
wnd.mainloop()
