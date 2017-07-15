from tkinter import *
from tkinter.messagebox import *

root = Tk()

btn1 = Button(root, text="info", font =("ubuntu",20),command=lambda: showinfo("ShowInfo","Информация"))
btn1.grid(row=0,column=0,sticky="ew")

btn2 = Button(root, text="warning", font =("ubuntu",20),command=lambda: showwarning("ShowWarning","Предупреждение"))
btn2.grid(row=0,column=1,sticky="ew")

btn3 = Button(root, text="error", font =("ubuntu",20),command=lambda: showerror("ShowError","Ошибка"))
btn3.grid(row=0,column=2,sticky="ew")


root.mainloop()