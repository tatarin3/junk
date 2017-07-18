from tkinter import *
import sqleasy




def open_database(event):
	'''При верном пароле убирает лишнее и формирует окно для работы с бд'''
	password = ent1.get()
	if password == '7753':

		def change_opt2(event):
			'''Функция при изменении базы меняет второй выпадающий список'''
			base = vopt1.get()
			accs = sqleasy.get_that_accs(base)
			vopt2z = vopt2.children['menu'] #AttributeError: 'StringVar' object has no attribute 'children'
			vopt2z.delete(0, 'end')
			for choice in accs:
				vopt2z.add_command(label=choice, command=change_password)


		def change_password(event):
			'''Эта функция меняет пароль при изменении второго выпадающего списка'''
			base = vopt1.get()
			login = vopt2.get()
			password = sqleasy.get_that_password(base,login)
			lbl2["text"] = password

		lbl1["text"] = "База данных открыта"
		btn1.grid_forget()
		ent1.grid_forget()
		vopt1 = StringVar()
		vopt1.set(str(sqleasy.get_bases()[0][0]))
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


if __name__ == "__main__":
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
