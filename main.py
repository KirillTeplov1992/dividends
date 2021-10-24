from tkinter import*
from classes import*
import sqlite3

root = Tk()
root.title("Учет дивидендов")


# Создаем базу данных
conn = sqlite3.connect("dividends.db")

# Создаем курсор
c = conn.cursor()


# Совершаем изменения
conn.commit()

# Создаем базу
c.execute(""" CREATE TABLE Veon (
			Date text,
			Amount real)""")

# Закрываем базу
conn.close()

root.mainloop()