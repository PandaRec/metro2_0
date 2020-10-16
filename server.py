#!/usr/bin/env python
# -*- coding: utf-8 -
from enum import Enum
from imp import reload

from flask import Flask, render_template, request
import json
import folium
from idna import unicode

import station
import requests
import bs4
from contextlib import closing
import psycopg2
from tkinter import *
import sub_window
import work_database



app = Flask(__name__)

class enum(Enum):
    favorite = 1
    history = 2

def draw_map():
    """ draw start map"""
    response = requests.get('https://api.hh.ru/metro/160')
    todos = json.loads(response.text)
    print()
    colors = {'CD0505': 'red'}

    all_stations_all_lines = []

    for i in todos['lines']:
        all_stations_one_line = []

        for j in i['stations']:
            one_station = station.station()
            one_station.set_name(j['name'])
            one_station.set_color(colors.get(i['hex_color']))
            one_station.set_lat(j['lat'])
            one_station.set_lng(j['lng'])
            all_stations_one_line.append(one_station)
            print()
        all_stations_all_lines.append(all_stations_one_line)
        all_stations_one_line = []
    print()

    map = folium.Map(location=[43.25654, 76.92848], zoom_start=12)

    for i in all_stations_all_lines:
        for j in i:
            print()

            # folium.Marker(location=[j.get_lat(),j.get_lng()], popup = "Google HQ", icon=folium.Icon(color = j.get_color())).add_to(map)
            folium.CircleMarker(location=[j.get_lat(), j.get_lng()], radius=9, popup=j.get_name(),
                                fill_color=j.get_color(),
                                color="black", fill_opacity=0.9).add_to(map)

    for i in all_stations_all_lines:
        for j in range(1, len(i)):
            lat1 = i[j - 1].get_lat()
            lat2 = i[j].get_lat()
            lng1 = i[j - 1].get_lng()
            lng2 = i[j].get_lng()
            color = i[j].get_color()

            color_line = folium.ColorLine([[lat1, lng1], [lat2, lng2]], [0], colormap=[i[j].get_color(), 'orange'],
                                          nb_steps=12, weight=5, opacity=0.7).add_to(map)

    map.save("./templates/index.html")


def draw_stations(all_stations_in_one_line):
    map = folium.Map(location=[43.25654, 76.92848], zoom_start=12)

    for j in all_stations_in_one_line:
        print()

        # folium.Marker(location=[j.get_lat(),j.get_lng()], popup = "Google HQ", icon=folium.Icon(color = j.get_color())).add_to(map)
        folium.CircleMarker(location=[j.get_lat(), j.get_lng()], radius=9, popup=j.get_name(),
                            fill_color=j.get_color(),
                            color="black", fill_opacity=0.9).add_to(map)
    print()
    return map


def draw_lines_by_points(map, all_stations_in_one_line):
    for i in range(1, len(all_stations_in_one_line)):
        lat1 = all_stations_in_one_line[i - 1].get_lat()
        lat2 = all_stations_in_one_line[i].get_lat()
        lng1 = all_stations_in_one_line[i - 1].get_lng()
        lng2 = all_stations_in_one_line[i].get_lng()

        color_line = folium.ColorLine([[lat1, lng1], [lat2, lng2]], [0],
                                      colormap=[all_stations_in_one_line[i].get_color(), 'orange'],
                                      nb_steps=12, weight=5, opacity=0.7).add_to(map)

    map.save("./templates/index.html")
    print()


def get_stations():
    """ request to hh to get list of stations. refactor to list of class"""
    response = requests.get('https://api.hh.ru/metro/160')
    todos = json.loads(response.text)
    colors = {'CD0505': 'red'}
    all_stations_one_line = []

    for i in todos['lines']:
        all_stations_one_line = []

        for j in i['stations']:
            one_station = station.station()
            one_station.set_name(j['name'])
            one_station.set_color(colors.get(i['hex_color']))
            one_station.set_lat(j['lat'])
            one_station.set_lng(j['lng'])
            all_stations_one_line.append(one_station)
    return all_stations_one_line


def add_other_elements_on_page():
    with open('./templates/index.html') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    he1=soup.find_all("style")[2]
    he = soup.find("body")
    # <form action="/my-link/"><input type="submit" value="Click me" /></form>

    # he.insert(1,'<form action="/point_1/" method="post"><input type="text" placeholder="kk" name="point"></form>\n')
    he1.append('form{display: inline;}')
    he.insert(1,
              '<form action="/my-link/" method="post">\n'
              '<input type="text" placeholder="start point" name="start_point">'
              '\n<input type="text" placeholder="end point" name="end_point">\n'
              '<input type="submit" value="Route" />\n'
              '</form>\n'
              '<form action="/history/" method="post"> <input type="submit" value="history" /></form>\n'
              '<form action="/favorite/" method="post"> <input type="submit" value="favorite" /></form>\n'
              '<form action="/add_to_favorite/" method="post"> <input type="submit" value="add to favorite" /></form>\n')

    he.insert(2,'<label/>\n')


    with open("./templates/index.html", "w") as outf:
        outf.write(str(soup))

    with open("./templates/index.html") as f:
        file = f.read()
        file = file.replace("&lt;", "<")
        file = file.replace("&gt;", ">")
    with open("./templates/index.html", "w") as w:
        w.write(file)
    print()


def add_route_to_lbl(route):

    stations = []
    for i in route:
        stations.append(i.get_name())
    rr = '->'.join(stations)

    aa = str.encode(rr,encoding='utf-8')
    aa = aa.decode(encoding='utf-8')

    with open("./templates/index.html",encoding='utf-8') as f:
        file = f.read()
        if aa=='':
            file = file.replace("<label/>", "<label>" + aa + "</label>")
        else:
            file = file.replace("<label/>", "<p><label>" + aa+ "</label></p>")
    with open("./templates/index.html", "w",encoding='utf-8') as w:
        w.write(file)


def calc_route(start="", end=""):
    print()
    rez = []
    all_stations = get_stations()
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

"""
def get_data_from_db(id='1',table_name=''):
    
    con = psycopg2.connect(
        database="metro2_0",
        user="postgres",
        password="3400430",
        host="127.0.0.1",

    )
    

    rez = []
    with closing(psycopg2.connect(dbname='metro2_0', user='postgres',
                            password='3400430', host='127.0.0.1')) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM table_name where id='+id)
            for row in cursor:
                print(row)
                rez.append(row)
    return rez
"""
def draw_window():
    print()

@app.route('/')
def index(route=""):
    all_stations = get_stations()
    map = draw_stations(all_stations)
    draw_lines_by_points(map, all_stations)
    add_other_elements_on_page()
    add_route_to_lbl(route)
    return render_template('index.html')

@app.route('/history/', methods=['POST'])
def show_history():
    sub_window.show_sub_window(enum.history)
    return index()

@app.route('/favorite/', methods=['POST'])
def show_favorite():
    sub_window.show_sub_window(enum.favorite)
    return index()

@app.route('/add_to_favorite/', methods=['POST'])
def add_favorite():

    print()

@app.route('/my-link/', methods=['POST'])
def my_link():
    print('I got clicked!')
    start_point = request.form['start_point']
    end_point = request.form['end_point']
    route = calc_route(start_point, end_point)

    all_stations = get_stations()
    map = draw_stations(all_stations)
    draw_lines_by_points(map, route)
    add_other_elements_on_page()
    add_route_to_lbl(route)
    work_database.push_data_to_db(table_name=enum.history,start_point=start_point,end_point=end_point)


    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
