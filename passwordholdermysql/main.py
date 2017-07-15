from tkinter import *
import sqleasy




def open_database(event):
	'''При верном пароле убирает лишнее и формирует окно для работы с бд'''
	password = ent1.get()
	if password == '7753':

		def change_opt2(event):
			'''Функция при изменении базы меняет второй выпадающий список'''
			base = vopt1.get() # here hide error
			accs = sqleasy.get_that_accs(base)
			opt2.configure(root,accs[0],*accs)


		def change_password(event):
			'''Эта функция меняет пароль при изменении второго выпадающего списка'''
			base = vopt1.get() # here
			login = vopt2.get() # here
			password = sqleasy.get_that_password(base,login)
			lbl2["text"] = password # maybe here 2

		lbl1["text"] = "База данных открыта"
		btn1.grid_forget()
		ent1.grid_forget()
		vopt1 = StringVar()
		vopt1.set("Base")
		opt1 = OptionMenu(root,vopt1,*sqleasy.get_bases(),command=change_opt2)
		btn2 = Button(root,text="New",font=("Ubuntu",20),width=12)
		btn3 = Button(root,text="Change",font=("Ubuntu",20),width=12)
		btn4 = Button(root,text="Delete",font=("Ubuntu",20),width=12)
		vopt2 = StringVar()
		vopt2.set("Login")
		opt2 = OptionMenu(root,vopt2,"Login",command=change_password)
		lbl2 = Label(root,text="Пароль",font=("Ubuntu",20))
		btn5 = Button(root,text="New",font=("Ubuntu",20),width=12)
		btn6 = Button(root,text="Change",font=("Ubuntu",20),width=12)
		btn7 = Button(root,text="Delete",font=("Ubuntu",20),width=12)

		opt1.grid(row=1,column=0,sticky="ew")
		btn2.grid(row=1,column=2,sticky="ew")
		btn3.grid(row=1,column=3,sticky="ew")
		btn4.grid(row=1,column=4,sticky="ew")
		opt2.grid(row=2,column=0,sticky="ew")
		lbl2.grid(row=2,column=1,sticky="ew")
		btn5.grid(row=2,column=2,sticky="ew")
		btn6.grid(row=2,column=3,sticky="ew")
		btn7.grid(row=2,column=4,sticky="ew")



	else:
		lbl1["text"] = "Пароль неверный"



root = Tk()
root.title('Хранитель паролей')

ent1 = Entry(width=10, font=20)
ent1.grid(row=0,column=0,sticky="ew")

lbl1 = Label(root,text="База данных не открыта",font=("Ubuntu",20))
lbl1.grid(row=0,column=1,sticky="ew")

btn1 = Button(root,text="Открыть БД",font=("Ubuntu",20),width=12)
btn1.grid(row=0,column=2,sticky="ew")
btn1.bind("<Button-1>",open_database)


root.mainloop()
