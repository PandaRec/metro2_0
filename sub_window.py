from enum import Enum
import server
import work_database
from contextlib import closing
import psycopg2
from tkinter import *


def show_sub_window(my_enum):
    window = Tk()
    data = []
    if my_enum.name==server.enum.favorite.name:
        data = work_database.get_data_from_db(table_name=server.enum.favorite)
        window.title("Избранные маршруты")

        print('favorite pressed')

    else:
        data = work_database.get_data_from_db(table_name=server.enum.history)
        window.title("Истрия маршрутов")


        print('history')

    window.geometry('400x250')
    window.attributes("-topmost", True)

    lbl = Label(window, text="начальная точка -> ")
    lbl.grid(column=0, row=0)
    lbl2 = Label(window, text="конечная точка")
    lbl2.grid(column=1, row=0)
    row = 1

    for i in data:
        lbl3 = Label(window, text=i[1] + ' -> ')
        lbl4 = Label(window, text=i[2])
        lbl3.grid(column=0, row=row)
        lbl4.grid(column=1, row=row)
        row += 1

    window.mainloop()