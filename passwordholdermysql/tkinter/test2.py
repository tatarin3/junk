from tkinter import *

def left_click(event):
	frm1.configure(bg="red")
	frm2.configure(bg="white")
	frm3.configure(bg="white")

def mid_click(event):
	frm1.configure(bg="white")
	frm2.configure(bg="green")
	frm3.configure(bg="white")

def right_click(event):
	frm1.configure(bg="white")
	frm2.configure(bg="white")
	frm3.configure(bg="blue")



root = Tk()
root.title("Клики мышью")
root.configure(bg="black")

frm1 = Frame(root, width=50, height=250, bg="white")
frm2 = Frame(root, width=50, height=250, bg="white")
frm3 = Frame(root, width=50, height=250, bg="white")

frm1.grid(row=0,column=0)
frm2.grid(row=0,column=1, padx=1)
frm3.grid(row=0,column=2)

root.bind("<Button-1>",left_click)
root.bind("<Button-2>",mid_click)
root.bind("<Button-3>",right_click)

root.mainloop() 