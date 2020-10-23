#!/usr/bin/env python
# -*- coding: utf-8 -
import threading
from enum import Enum
from tkinter.tix import ScrolledWindow

from flask import Flask, render_template, request, flash
import json
import folium
import station
import requests
import bs4
import old_sub_window
import work_database
import users_map
from tkinter import *
import os
import sub_window



#root = Tk() # new
app = Flask(__name__)


class enum(Enum):
    favorite = 1
    history = 2

#def before_request():
    #app.jinja_env.cache={}
#app.before_request(before_request)


# def flask_main():# new
#     @app.route('/')
#     def index(route=''):
#         stations = users_map.get_stations()
#         map = users_map.draw_stations(stations)
#         users_map.draw_lines_by_points(map, stations, 'index.html')
#         users_map.add_other_elements_on_page('index.html')
#         users_map.add_route_to_lbl(route, 'index.html')
#
#         return render_template('index.html')
#
#     @app.route('/my-link/', methods=['POST'])
#     def my_link():
#         print('I got clicked!')
#         start_point = request.form['start_point']
#         end_point = request.form['end_point']
#         route = calc_route(start_point, end_point)
#
#         map = users_map.draw_stations(users_map.get_stations())
#         users_map.draw_lines_by_points(map, route, 'index4.html')
#         users_map.add_other_elements_on_page('index4.html')
#         users_map.add_route_to_lbl(route, 'index4.html')
#         work_database.push_data_to_db(table_name=enum.history, start_point=start_point, end_point=end_point)
#
#         return render_template('index4.html')
#     app.run() #запуск лупа

# def tk_main():# new
#
#     root = Tk()
#     root.withdraw()
#
#     @app.route('/history/', methods=['POST'])
#     def show_history():
#         print('show_history')
#         root.deiconify()
#         sub_window.test_cub_window()
#         return render_template('index.html')
#
#     root.mainloop() #запуск лупа тк


def calc_route(start="", end=""):
    print()
    rez = []
    all_stations = users_map.get_stations()
    all_stations_names = []

    for i in all_stations:
        all_stations_names.append(i.get_name())

    ind_1 = all_stations_names.index(start)
    ind_2 = all_stations_names.index(end)

    if ind_1<ind_2:
        for i in range(ind_1,ind_2+1):
            rez.append(all_stations[i])
    elif ind_1>ind_2:
        for i in range(ind_2, ind_1 + 1):
            rez.append(all_stations[i])
        rez.reverse()
    else:
        rez.append(all_stations[ind_1])
    return rez

@app.route('/')
def index(route=''):
    stations= users_map.get_stations()
    map = users_map.draw_stations(stations)
    users_map.draw_lines_by_points(map, stations,'index.html')
    users_map.add_other_elements_on_page('index.html')
    users_map.add_route_to_lbl(route,'index.html')

    return render_template('index.html')

@app.route('/history/', methods=['POST'])
def show_history():

    #sub_window.show_sub_window(enum.history)
    sub_window.show_history_or_favorite(enum.history)


    #sub_window.test()
    #sub_window.kkk()
    return render_template('history_favorite.html')

@app.route('/favorite/', methods=['POST'])
def show_favorite():
    sub_window.show_history_or_favorite(enum.favorite)
    return render_template('history_favorite.html')


@app.route('/add_to_favorite/', methods=['POST'])
def add_favorite():
    data = work_database.get_data_from_db(table_name=enum.history)

    work_database.push_data_to_db(table_name=enum.favorite,start_point=data[-1][1],end_point=data[-1][2])
    print()

@app.route('/my-link/', methods=['POST'])
def my_link():
    print('I got clicked!')
    start_point = request.form['start_point']
    end_point = request.form['end_point']
    route = calc_route(start_point, end_point)

    map = users_map.draw_stations(users_map.get_stations())
    users_map.draw_lines_by_points(map, route, 'index4.html')
    users_map.add_other_elements_on_page('index4.html')
    users_map.add_route_to_lbl(route, 'index4.html')
    work_database.push_data_to_db(table_name=enum.history,start_point=start_point,end_point=end_point)

    return render_template('index4.html')

@app.route('/my/', methods=['POST'])
def historybuttonpressed():
    print()
    print('history-button-pressed')
    points = request.form['ff'].split('   ->   ')
    start_point = points[0]
    end_point = points[1]


    users_map.draw_route(start_point, end_point,'index.html','index4.html')

    print(request.form['ff'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) # old


    #flt = threading.Thread(target=flask_main) # new
    #flt.daemon = True # new
    #flt.start()  # фоновый процесс # new
    #tk_main()  # основной поток # new