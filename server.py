#!/usr/bin/env python
# -*- coding: utf-8 -
from enum import Enum

from flask import Flask, render_template, request, flash
# import json
# import folium
# import station
# import requests
# import bs4
# import old_sub_window
import work_database
import users_map
from tkinter import *
# import os
import sub_window
import sign_up
import sign_in
# import user

app = Flask(__name__)
global cur

class enum(Enum):
    favorite = 1
    history = 2
    auth = 3

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

    return render_template('sign_in.html')#    return render_template('index.html')

@app.route('/history/', methods=['POST'])
def show_history():
    sub_window.show_history_or_favorite(enum.history,cur.get_id())
    return render_template('history_favorite.html')

@app.route('/favorite/', methods=['POST'])
def show_favorite():
    sub_window.show_history_or_favorite(enum.favorite,cur.get_id())
    return render_template('history_favorite.html')

@app.route('/my-link/', methods=['POST'])
def my_link():
    start_point = request.form['start_point']
    end_point = request.form['end_point']
    if request.form['btn'] == 'add to favorite':
        add_to_favorite(start_point,end_point)
    else:
        route = calc_route(start_point, end_point)
        map = users_map.draw_stations(users_map.get_stations())
        users_map.draw_lines_by_points(map, route, 'index4.html')
        users_map.add_other_elements_on_page('index4.html')
        users_map.add_route_to_lbl(route, 'index4.html')

        work_database.push_data_to_db_history_or_favorite(table_name=enum.history,start_point=start_point,end_point=end_point,id=str(cur.get_id()))

    return render_template('index4.html')

@app.route('/my/', methods=['POST'])
def historybuttonpressed():
    points = request.form['ff'].split('   ->   ')
    start_point = points[0]
    end_point = points[1]
    users_map.draw_route(start_point, end_point,'index.html','index4.html')
    return render_template('index.html')

def add_to_favorite(start_point='',end_point=''):
    print(start_point,end_point,end=' ')
    work_database.push_data_to_db_history_or_favorite(enum.favorite,start_point,end_point,str(cur.get_id()))
    return render_template('index.html')

@app.route('/sign-in-sign-up/', methods=['POST'])
def signing_in():
    btn = request.form['btn']
    global cur
    if btn == 'Войти':
        sign = sign_in.enter()
    else:
        return render_template('sign_up.html')
    if sign!=None:
        cur=sign
        lol = cur.get_id()
        print()
        return render_template('index.html')
    else:
        return render_template('sign_in.html')


@app.route('/registration/', methods=['POST'])
def registration():
    global cur

    cur = sign_up.registr()
    return render_template('index.html')

@app.route('/your-friends/', methods=['POST'])
def your_friends():
    aa = work_database.get_friends_from_db(cur.get_id())
    to_send = []
    for i in aa:
        lol  = work_database.get_data_from_db_history_or_favorite(enum.favorite,str(i[1]))
        to_send.append(lol)

    if len(to_send)==0:
        return render_template('index.html')

    sub_window.show_friends_favorite(to_send)
    return render_template('friends_favorite.html')


if __name__ == '__main__':
    app.run(debug=True)