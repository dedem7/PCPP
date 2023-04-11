from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("                      Calculator")

v=IntVar()

user_input1=Entry(window,width="20")
user_input2=Entry(window,width="20")

radio1=Radiobutton(window,text="+",variable=v, value=1)
radio2=Radiobutton(window,text="-",variable=v, value=2)
radio3=Radiobutton(window,text="*",variable=v, value=3)
radio4=Radiobutton(window,text="/",variable=v, value=4)

def evaluate():
    #if user_input1.get().isdigit():
        #messagebox.showinfo(title="Info", message=int(user_input1.get()))
    try:
        (float(user_input1.get()) or int(user_input1.get())) and (float(user_input2.get()) or int(user_input2.get()))
        
        if v.get()==0:
            messagebox.showinfo(title="Operation", message="Choose operation!")
        elif v.get()==1:
            messagebox.showinfo(title="Result", message=float(user_input1.get())+float(user_input2.get()))
        elif v.get()==2:
            messagebox.showinfo(title="Result", message=float(user_input1.get())-float(user_input2.get()))
        elif v.get()==3:
            messagebox.showinfo(title="Result", message=float(user_input1.get())*float(user_input2.get()))
        else:
            if float(user_input2.get())==0:
                messagebox.showerror(title="ZerpDivisionError", message="You can't divide on Zero!")
            else:
                messagebox.showinfo(title="Result", message=float(user_input1.get())/float(user_input2.get()))
                              
    except:
        messagebox.showerror(title="Type Error", message="Int or Float to put!")
        if user_input1.get().isdigit() is not True:
            user_input1.delete(0,END)
            user_input1.focus()
        elif user_input2.get().isdigit() is not True:
            user_input2.delete(0,END)
            user_input2.focus()
        
button=Button(window, text="Evaluate",command=evaluate)

user_input1.grid(row=2, column=0,rowspan=2)
user_input2.grid(row=2, column=2,rowspan=2)
radio1.grid(row=1, column=1)
radio2.grid(row=2, column=1)
radio3.grid(row=3, column=1)
radio4.grid(row=4, column=1)
button.grid(row=5, column=1)

window.mainloop()


