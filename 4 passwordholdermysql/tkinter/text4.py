from tkinter import *

class Question:
	"""In class work (useles)"""
	def __init__(self, main):
		self.entr1 = Entry(main, width=3, font=15)
		self.btn1 = Button(main, text="Проверить")
		self.lbl1 = Label(main, width=27, font=15)

		self.entr1.grid(row=0,column=0)
		self.btn1.grid(row=0,column=1)
		self.lbl1.grid(row=0,column=2)

		self.btn1.bind("<Button-1>", self.answer)

	def answer(self, event):

		txt = self.entr1.get()

		try:
			if int(txt) < 10:
				self.lbl1["text"] = "Вам рано"
			else:
				self.lbl1["text"] = "Добро пожаловать"
		except ValueError:
			self.lbl1["text"] = "Введите корректный возраст!"

root = Tk()
root.title("Сколько вам лет?")

q = Question(root)

root.mainloop()
