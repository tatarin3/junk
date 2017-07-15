from tkinter import *
from tkinter.filedialog import *

def open_file():
	of = askopenfilename()
	file = open(of,"r")
	txt.insert(END,file.read())
	file.close()

def save_file():
	sf = asksaveasfilename()
	finaltext = txt.get(1.0,END)
	file = open(sf,"w")
	file.write(finaltext)
	file.close()

def exit_app():
	root.quit()


root = Tk()

mmenu = Menu(root)
root.configure(menu=mmenu)

item1 = Menu(mmenu,tearoff=0)
mmenu.add_cascade(label="File", menu=item1)
item1.add_command(label="Open", command=open_file)
item1.add_command(label="Save", command=save_file)
item1.add_command(label="Exit", command=exit_app)

txt = Text(root, width=40,height=15, font=12)
txt.pack(expand=YES,fill=BOTH)

root.mainloop()