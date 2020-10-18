from flask import render_template

import server
import work_database
import users_map
from tkinter.tix import *
#from tkinter import *
from tkinter import messagebox as mb









def click(event, window):
    button_text = event.widget.cget('text')
    points = button_text.split('   ->   ')
    start_point = points[0]
    end_point = points[1]

    users_map.draw_route(start_point, end_point)
    window.destroy()
    print('11111')




def show_sub_window(my_enum):
    data = []
    root = Tk()

    frame = Frame(width="500", height="500")
    frame.pack()
    swin = ScrolledWindow(frame, width=500, height=500)
    swin.pack()
    win = swin.window
    root.attributes("-topmost", True)

    if my_enum.name == server.enum.favorite.name:
        data = work_database.get_data_from_db(table_name=server.enum.favorite)
        root.wm_title('Избранное')

    else:
        data = work_database.get_data_from_db(table_name=server.enum.history)
        root.wm_title('История')

    for i in data:
        #btn = Button(win, text=i[1] + '   ->   ' + i[2], command=lambda window=win: click(btn))#, command=lambda window=win: click(root)
        btn = Button(win, text=i[1] + '   ->   ' + i[2])


        #btn = Button(win, text=i[1] + '   ->   ' + i[2])
        #btn.bind("<Button-1>", lambda event: click_route(event, btn["text"]))

        #btn.bind('<Button-1>', on_click)
        btn.bind('<Button-1>', lambda event: click(event, root))
        btn.pack()
    print()



    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label="Commands", menu=filemenu)

    #ans = mb.askyesno(message="открыть сайт")


    root.mainloop()


    """
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



    row = 1
    for i in data:
        btn = Button(text=i[1] + '   ->   '+i[2])
        btn.bind("<Button-1>", lambda event: click_route(event, btn["text"]))

        btn.grid(column=0, row=row)
        row += 1

    window.mainloop()
    """


def show():
    print('aaaaaaaaaaaaaaaa')


def test():
    root = Tk()
    root.wm_title('Got Skills\' Skill Tracker')
    frame = Frame(width="500", height="500")
    frame.pack()
    swin = ScrolledWindow(frame, width=500, height=500)
    swin.pack()
    win = swin.window

    w = Message(win, text='fffff', width=500)

    w.pack()

    # buttonText.set("1")
    # w1 = Button(win,textvariable=buttonText, command=click)

    # w1.pack()

    root.mainloop()


def kkk():
    root = Tk()
    frame = Frame(width="500", height="500")
    frame.pack()
    swin = ScrolledWindow(frame, width=500, height=500)
    swin.pack()
    win = swin.window
    root.attributes("-topmost", True)
    root.wm_title('Избранное')
    btn = Button(win, text='111',command=lambda window=win: click(root))
    btn.pack()


    root.mainloop()





