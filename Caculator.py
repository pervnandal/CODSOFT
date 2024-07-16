from tkinter import *

window = Tk()
window.title("Simple Calculator!")

inp_field = Entry(window,width=65,borderwidth=5)
inp_field.grid(row=0,column=0,columnspan=4,ipady=10)

def btn_clicked(value):
    text = inp_field.get()
    inp_field.delete(0,END) # deletes the content inside text box
    inp_field.insert(0, str(text) + str(value))

def evaluate():
    try:
        exp= str(inp_field.get())
        total = str(eval(exp))
        inp_field.delete(0,END)
        inp_field.insert(0,total)
    except:
        inp_field.delete(0,END)
        inp_field.insert(0,"Error")

    

def clearAll():
    inp_field.delete(0,END)
#row 1 buttons 

clear = Button(window,text="Clear",padx=129,pady=20,command=clearAll).grid(row=1,column=0,columnspan=3)
divide = Button(window,text="/",padx=40,pady=20,command=lambda: btn_clicked("/")).grid(row=1,column=3)

# row 2 buttons
btn1 = Button(window,text="9",padx=40,pady=20,command=lambda: btn_clicked(9))
btn1.grid(row=2,column=0)

btn1 = Button(window,text="8",padx=40,pady=20,command=lambda: btn_clicked(8))
btn1.grid(row=2,column=1)

btn1 = Button(window,text="7",padx=40,pady=20,command=lambda: btn_clicked(7))
btn1.grid(row=2,column=2)

btn1 = Button(window,text="+",padx=40,pady=20,command=lambda: btn_clicked("+"))
btn1.grid(row=2,column=3)

# row 3 buttons 
btn1 = Button(window,text="6",padx=40,pady=20,command=lambda: btn_clicked(6))
btn1.grid(row=3,column=0)

btn1 = Button(window,text="5",padx=40,pady=20,command=lambda: btn_clicked(5))
btn1.grid(row=3,column=1)

btn1 = Button(window,text="4",padx=40,pady=20,command=lambda: btn_clicked(4))
btn1.grid(row=3,column=2)

btn1 = Button(window,text="-",padx=40,pady=20,command=lambda: btn_clicked("-"))
btn1.grid(row=3,column=3)

# row 4 buttons
btn1 = Button(window,text="3",padx=40,pady=20,command=lambda: btn_clicked(3))
btn1.grid(row=4,column=0)

btn1 = Button(window,text="2",padx=40,pady=20,command=lambda: btn_clicked(2))
btn1.grid(row=4,column=1)

btn1 = Button(window,text="1",padx=40,pady=20,command=lambda: btn_clicked(1))
btn1.grid(row=4,column=2)

btn1 = Button(window,text="x",padx=40,pady=20,command=lambda: btn_clicked("*"))
btn1.grid(row=4,column=3)

# row 5 buttons
btn1 = Button(window,text="0",padx=40,pady=20,command=lambda: btn_clicked(0))
btn1.grid(row=5,column=0)

btn1 = Button(window,text=".",padx=40,pady=20,command=lambda: btn_clicked("."))
btn1.grid(row=5,column=1)

btn1 = Button(window,text="=",padx=90,pady=20,command=evaluate)
btn1.grid(row=5,column=2,columnspan=2)

window.mainloop()