from tkinter import*

class TButton:
	def __init__(self, frame, text, c):
		self.button = Button(frame, text = text, command = self.fun)
		self.button.grid(row=0, column = c)
	def fun(self):
		pass

class TLine:
	def __init__(self, main, text, r):
		self.label = Label(main, text = text)
		self.label.grid(row = r, column = 0)
		self.entry = Entry(main)
		self.entry.grid(row = r, column = 1)

class TAddButton(TButton):
	def fun(self):
		add_window = TAddWindow("Добавить компанию")

class TDividendsButton(TButton):
	def fun(self):
		pass


class TSurface:
	def __init__(self, master):
		self.listbox = Listbox(master)
		self.listbox.grid(row = 0, column = 0)
		self.frame = Frame(master)
		self.frame.grid(row = 3, column = 0)
		self.b1 = TAddButton(self.frame, "Добавить", 0)
		self.b2 = TDividendsButton(self.frame, "Пришли дивиденды", 1)

class TAddWindow:
	def __init__(self, text):
		self.top = Toplevel()
		self.top.title(text)
		self.line = TLine(self.top, "Название компании", 0)
		self.rb = Radiobutton(self.top, text = "Иностранная компания")
	