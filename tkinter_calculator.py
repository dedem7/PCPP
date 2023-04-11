import tkinter as tk

window = tk.Tk()

#window.resizable(width=False, height=False)
#window.geometry("")

text_input=tk.StringVar()
display = tk.Entry(window,width=11,justify=tk.RIGHT,font=("Arial",17),state="readonly",readonlybackground="white", textvariable = text_input)
display.grid(row=0,column=0,columnspan=5)

text_input.set('0')

new_value = 0
operation_clicked=False


def clicker(n):
    global operation_clicked   
    text_string = text_input.get()
    if text_string == "Error":
        return False

    if operation_clicked:
        text_string="0"
        operation_clicked=False
        
    if len(text_string)<10:
        if n=="." and n not in text_string:
            text_string+=n
            n=""
        elif n=="." and n in text_string:
            n=""
      
        if text_string=='0':
            text_string=n
        elif text_string=='-0.':
            text_string+=n
        elif text_string=='-0':
            text_string='-'+n  
        else:
            text_string+=n
          
        text_input.set(text_string)

      
saved_value = 0
saved_op=''
def operation(op):
    global operation_clicked, saved_value, saved_op, number_clicked

    text_string = text_input.get() 
    
    #Error
    if text_string == "Error" and op!="C":
        return False

    #C
    if op=="C":
        text_input.set('0')
        saved_value=0
        saved_op=''
        return None

    #+/-
    if op=="+/-" and "-" not in text_string:
        text_string="-" + text_string
        text_input.set(text_string)
        return None
    elif op=="+/-" and "-" in text_string:
        text_string=text_string[1:]
        text_input.set(text_string)
        return None

    #save value
    if saved_op=='' and "." in text_string: saved_value =float(text_string)
    if saved_op=='' and "." not in text_string: saved_value =int(text_string)

    if operation_clicked and op in ["+","-","*","/"]:
        saved_op=op
    
    #convert to number
    if "." in text_string:
        text_number=float(text_string)
    else:
        text_number=int(text_string)
    
    #+
    if saved_op=="+" and not operation_clicked:
        saved_value = saved_value + text_number
        
    #-
    if saved_op=="-" and not operation_clicked:
        saved_value = saved_value - text_number
        
    #*
    if saved_op=="*" and not operation_clicked:
        saved_value = saved_value * text_number
        
    #/
    if saved_op=="/" and not operation_clicked:
        if text_number == 0:
            text_input.set("Error")
            saved_value=0
            saved_op=''
            return False
        else:
            if saved_value % text_number ==0:
                saved_value = int(saved_value / text_number)
            else:
                saved_value = saved_value / text_number

    
    result_value_string = str(saved_value)
    if "." in result_value_string:
        if int(result_value_string[result_value_string.index(".")+1:])==0:
            result_value_string = result_value_string[:result_value_string.index(".")]

        elif len(text_string)<11:
            pass
            
        else:
            result_value_string = str(round(saved_value,2))
            

    if len(str(round(saved_value)))>11:
        text_input.set("Error")
        saved_value=0
        saved_op=''
        return False
    
    elif len(result_value_string)<=11:
        text_input.set(result_value_string)

    else:
        while "." in result_value_string and len(result_value_string)>11:
            result_value_string = result_value_string[:-1]
            #result_value_string=str(round(saved_value))
        if result_value_string[-1]=='.':
            result_value_string=result_value_string[:-1]
        text_input.set(result_value_string)
        
    
    #op
    if op in ["+","-","*","/"]:
        saved_op = op
        
    #=
    if op=="=":
        saved_value=0
        saved_op=''

    operation_clicked = True

b0 = tk.Button(window, width=2,text="0",command=lambda *args: clicker(b0["text"]))
b0.grid(row=4,column=0,sticky='nesw')

b1 = tk.Button(window, width=2,text="1",command=lambda *args: clicker(b1["text"]))
b1.grid(row=3,column=0,sticky='nesw')

b2 = tk.Button(window, width=2,text="2",command=lambda *args: clicker(b2["text"]))
b2.grid(row=3,column=1,sticky='nesw')

b3 = tk.Button(window, width=2,text="3",command=lambda *args: clicker(b3["text"]))
b3.grid(row=3,column=2,sticky='nesw')

b4 = tk.Button(window, width=2,text="4",command=lambda *args: clicker(b4["text"]))
b4.grid(row=2,column=0,sticky='nesw')

b5 = tk.Button(window, width=2,text="5",command=lambda *args: clicker(b5["text"]))
b5.grid(row=2,column=1,sticky='nesw')

b6 = tk.Button(window, width=2,text="6",command=lambda *args: clicker(b6["text"]))
b6.grid(row=2,column=2,sticky='nesw')

b7 = tk.Button(window, width=2,text="7",command=lambda *args: clicker(b7["text"]))
b7.grid(row=1,column=0,sticky='nesw')

b8 = tk.Button(window, width=2,text="8",command=lambda *args: clicker(b8["text"]))
b8.grid(row=1,column=1,sticky='nesw')

b9 = tk.Button(window, width=2,text="9",command=lambda *args: clicker(b9["text"]))
b9.grid(row=1,column=2,sticky='nesw')


b10 = tk.Button(window, width=2,text="C",command=lambda *args: operation(b10["text"]))
b10.grid(row=4,column=1,sticky='nesw')

b11 = tk.Button(window, width=2,text=".",command=lambda *args: clicker(b11["text"]))
b11.grid(row=4,column=2,sticky='nesw')

b12 = tk.Button(window, width=3,text="=",command=lambda *args: operation(b12["text"]))
b12.grid(row=3,column=3,sticky='nesw')

b13 = tk.Button(window, width=3,text="+/-",command=lambda *args: operation(b13["text"]))
b13.grid(row=4,column=3,sticky='nesw')

b14 = tk.Button(window, width=2,text="+",command=lambda *args: operation(b14["text"]))
b14.grid(row=1,column=4,sticky='nesw')

b15 = tk.Button(window, width=2,text="-",command=lambda *args: operation(b15["text"]))
b15.grid(row=2,column=4,sticky='nesw')

b16 = tk.Button(window, width=2,text="*",command=lambda *args: operation(b16["text"]))
b16.grid(row=3,column=4,sticky='nesw')


b17 = tk.Button(window, width=2,text="/",command=lambda *args: operation(b17["text"]))
b17.grid(row=4,column=4,sticky='nesw')



window.mainloop()
