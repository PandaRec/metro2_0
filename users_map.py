from flask import Flask, render_template, request, flash
from folium import folium
import json
import folium
import station
import requests
import bs4
import server
import work_database
import os




def draw_stations(all_stations_in_one_line):
    map = folium.Map(location=[43.25654, 76.92848], zoom_start=12)

    for j in all_stations_in_one_line:
        folium.CircleMarker(location=[j.get_lat(), j.get_lng()], radius=9, popup=j.get_name(),
                            fill_color=j.get_color(),
                            color="black", fill_opacity=0.9).add_to(map)

    return map

def draw_lines_by_points(map, all_stations_in_one_line,name_to_save):
    for i in range(1, len(all_stations_in_one_line)):
        lat1 = all_stations_in_one_line[i - 1].get_lat()
        lat2 = all_stations_in_one_line[i].get_lat()
        lng1 = all_stations_in_one_line[i - 1].get_lng()
        lng2 = all_stations_in_one_line[i].get_lng()

        color_line = folium.ColorLine([[lat1, lng1], [lat2, lng2]], [0],
                                      colormap=[all_stations_in_one_line[i].get_color(), 'orange'],
                                      nb_steps=12, weight=5, opacity=0.7).add_to(map)

    map.save("./templates/"+name_to_save)

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


def add_other_elements_on_page(name_to_open_and_save):
    with open('./templates/'+name_to_open_and_save) as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    he1=soup.find_all("style")[2]
    he = soup.find("body")
    he1.append('form{display: inline;}')
    he.insert(1,
              '<form action="/my-link/" method="post">\n'
              '<input type="text" placeholder="start point" name="start_point">'
              '\n<input type="text" placeholder="end point" name="end_point">\n'
              '<input type="submit" value="route" name="btn"/>\n'
              '<input type="submit" value="add to favorite" name="btn"/>'
              '</form>\n'
              '<form action="/history/" method="post"> <input type="submit" value="history" /></form>\n'
              '<form action="/favorite/" method="post"> <input type="submit" value="favorite" /></form>\n'
              '<form action="/your-friends/" method="post"> <input type="submit" value="your friends favorite routes" /></form>\n'

              )

    he.insert(2,'<label/>\n')

    with open("./templates/"+name_to_open_and_save, "w") as outf:
        outf.write(str(soup))

    with open("./templates/"+name_to_open_and_save) as f:
        file = f.read()
        file = file.replace("&lt;", "<")
        file = file.replace("&gt;", ">")
    with open("./templates/"+name_to_open_and_save, "w") as w:
        w.write(file)

def add_route_to_lbl(route,name_of_file):
    stations = []
    for i in route:
        stations.append(i.get_name())
    rr = '->'.join(stations)

    aa = str.encode(rr,encoding='utf-8')
    aa = aa.decode(encoding='utf-8')

    with open("./templates/"+name_of_file,encoding='utf-8') as f:
        file = f.read()
        if aa=='':
            file = file.replace("<label/>", "<label>" + aa + "</label>")
        else:
            file = file.replace("<label/>", "<p><label>" + aa+ "</label></p>")
    with open("./templates/"+name_of_file, "w",encoding='utf-8') as w:
        w.write(file)

def draw_route(start_point,end_point,name_of_file,name_of_file_to_present):
    route = server.calc_route(start_point, end_point)

    map = draw_stations(get_stations())
    draw_lines_by_points(map, route,name_of_file)
    add_other_elements_on_page(name_of_file)
    add_route_to_lbl(route,name_of_file)
    work_database.push_data_to_db_history_or_favorite(table_name=server.enum.history, start_point=start_point, end_point=end_point)

    return render_template(name_of_file_to_present)