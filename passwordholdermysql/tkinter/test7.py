from tkinter import *
from tkinter.messagebox import *

def asquestion(event):
	answer = askquestion("askquestion","Вопрос первый?")
	lbl1.configure(text=answer)

def asqok(event):
	answer = askokcancel("askqokcancel","Вопрос второй?")
	lbl2.configure(text=answer)

def asqyesno(event):
	answer = askyesno("askqyesno","Вопрос третий?")
	lbl3.configure(text=answer)

def asqrc(event):
	answer = askretrycancel("askqretrycancel","Вопрос третий?")
	lbl4.configure(text=answer)

root = Tk()

btn1 = Button(root,text="asquestion",font=("Ubuntu",20),width=12)
btn1.grid(row=0,column=0,sticky="ew")
lbl1 = Label(root, font=("Ubuntu",20), width=12)
lbl1.grid(row=0,column=1)
btn1.bind("<Button-1>",asquestion)

btn2 = Button(root,text="asqok",font=("Ubuntu",20),width=12)
btn2.grid(row=1,column=0,sticky="ew")
lbl2 = Label(root, font=("Ubuntu",20), width=12)
lbl2.grid(row=1,column=1)
btn2.bind("<Button-1>",asqok)

btn3 = Button(root,text="asyesno",font=("Ubuntu",20),width=12)
btn3.grid(row=2,column=0,sticky="ew")
lbl3 = Label(root, font=("Ubuntu",20), width=12)
lbl3.grid(row=2,column=1)
btn3.bind("<Button-1>",asqyesno)

btn4 = Button(root,text="asretrycanc",font=("Ubuntu",20),width=12)
btn4.grid(row=3,column=0,sticky="ew")
lbl4 = Label(root, font=("Ubuntu",20), width=12)
lbl4.grid(row=3,column=1)
btn4.bind("<Button-1>",asqrc)

root.mainloop()