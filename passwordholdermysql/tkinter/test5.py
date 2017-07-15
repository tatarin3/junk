from tkinter import *

def new_win():
	win = Toplevel(root)
	lbl1 = Label(win,text="Текст в окне верхнего уровня", font=20)
	lbl1.pack()

def exit_app():
	root.destroy()

root = Tk()

mmenu = Menu(root)
root.configure(menu=mmenu)

frstitem = Menu(mmenu)
mmenu.add_cascade(label="File", menu=frstitem)
frstitem.add_command(label="New", command=new_win)
frstitem.add_command(label="Exit", command=exit_app)

scnditem = Menu(mmenu,tearoff=0)
mmenu.add_cascade(label="Edit", menu=scnditem)
scnditem.add_command(label="Item1")
scnditem.add_command(label="Item1")
scnditem.add_command(label="Item1")
scnditem.add_separator()
scnditem.add_command(label="Item1")

toolb = Frame(root, bg="#A1A1A1")
toolb.pack(side=TOP,fill=X)

btn1 = Button(toolb,text="Cut")
btn1.grid(row=0,column=0, padx=2,pady=2)

btn2 = Button(toolb,text="Copy")
btn2.grid(row=0,column=1, padx=2,pady=2)

btn3 = Button(toolb,text="Paste")
btn3.grid(row=0,column=2, padx=2,pady=2)

statb = Label(root, relief=SUNKEN, anchor=W, text="mission complete")
statb.pack(side=BOTTOM,fill=X)

root.mainloop()