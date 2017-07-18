from tkinter import *

root = Tk()

c1 = Canvas (root,width=500,height=500,cursor="pencil", bg="white")
c1.pack()

c1.create_line(250,0,250,500,width=3,fill="red", arrow=LAST)
c1.create_line(0,250,500,250,width=3,fill="red", arrow=LAST)

root.mainloop()