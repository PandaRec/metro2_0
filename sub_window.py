from flask import render_template

import server
import work_database
import users_map
from tkinter.tix import *
#from tkinter import *
import tkinter as tk

from tkinter import messagebox as mb









def click(event, window):
    button_text = event.widget.cget('text')
    points = button_text.split('   ->   ')
    start_point = points[0]
    end_point = points[1]
    window.destroy()

    users_map.draw_route(start_point, end_point,'index.html','index4.html')
    print('11111')
    print(start_point,end_point,end=' ')




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
    #root = Tk()
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
    #root = Tk()
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

def test_cub_window():
    """
    root = Tk()
    root.geometry("300x200")

    w = Label(root, text='GeeksForGeeks',
              font="50")

    w.pack()

    scroll_bar = Scrollbar(root)

    scroll_bar.pack(side=RIGHT,
                    fill=Y)

    mylist = Listbox(root,
                     yscrollcommand=scroll_bar.set)

    for line in range(1, 26):
        mylist.insert(END, "Geeks " + str(line))


    data = work_database.get_data_from_db(table_name=server.enum.history)

    for i in data:
        mylist.insert(END,i[1] + '   ->   ' + i[2])

        #btn = Button(win, text=i[1] + '   ->   ' + i[2], command=lambda window=win: click(btn))#, command=lambda window=win: click(root)


        #btn = Button(win, text=i[1] + '   ->   ' + i[2])
        #btn.bind("<Button-1>", lambda event: click_route(event, btn["text"]))

        #btn.bind('<Button-1>', on_click)
        btn.bind('<Button-1>', lambda event: click(event, root))
        btn.pack()

    mylist.pack(side=LEFT, fill=BOTH)

    scroll_bar.config(command=mylist.yview)

    root.mainloop()
    """
    """
    root = tk.Tk()

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    checklist = tk.Text(root, width=20)
    checklist.pack()

    vars = []

    data = work_database.get_data_from_db(table_name=server.enum.history)

    for i in data:
        var = tk.IntVar()
        vars.append(var)
        checkbutton = tk.Button(checklist, text=i[1] + '   ->   ' + i[2])
        checkbutton.bind('<Button-1>', lambda event: click(event, root))
        checklist.window_create("end", window=checkbutton)
        checklist.insert("end", "\n")

    checklist.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=checklist.yview)

    # disable the widget so users can't insert text into it
    checklist.configure(state="disabled")

    root.mainloop()
"""

    root1 = tk.Tk()

    data = work_database.get_data_from_db(table_name=server.enum.history)


    #text_widget = tk.Text(root)
    #text_widget = tk.Grid(root)

    draw = Canvas(width=230, height=5000, scrollregion=(0, 0, 230, 5000))
    draw.sbar = Scrollbar(orient=VERTICAL)
    frame = Frame(draw)
    draw.create_window(0, 0, window=frame, width=230, height=5000, anchor=N + W)
    for i in data:
        btn = Button(frame, width=30,text=i[1] + '   ->   ' + i[2])
        btn.bind('<Button-1>', lambda event: click(event, root1))
        btn.pack()

    draw['yscrollcommand'] = draw.sbar.set
    draw.sbar['command'] = draw.yview
    draw.sbar.pack(side=RIGHT, fill=Y)
    draw.pack()
    #return render_template('index.html')

    root1.mainloop()






