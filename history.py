import work_database
import server
import json
import folium
import station
import requests
import bs4
import server
import work_database
import os


def show_history():
    print()
    data = work_database.get_data_from_db(table_name=server.enum.history)
    os.remove('./templates/history.html')

    with open("./templates/history.html", "w") as outf:
        outf.write('<!DOCTYPE html>\n'
'<html>\n'
    '<head>\n'
        '<meta content="text/html; charset=utf-8" http-equiv="content-type"/>\n'

        '<style>\n'
        #'form{display: inline;}\n'
        '</style>\n'

    '</head>\n'

    '<body>\n'

    '</body>\n'
'</html>')

    with open('./templates/history.html') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    he1=soup.find_all("style")
    he = soup.find("body")
    # <form action="/my-link/"><input type="submit" value="Click me" /></form>

    # he.insert(1,'<form action="/point_1/" method="post"><input type="text" placeholder="kk" name="point"></form>\n')
    #he1.append('form{display: inline;}')
    # he.insert(1,
    #           '<form action="/my-link/" method="post">\n'
    #           '<input type="text" placeholder="start point" name="start_point">'
    #           '\n<input type="text" placeholder="end point" name="end_point">\n'
    #           '<input type="submit" value="Route" />\n'
    #           '</form>\n'
    #           '<form action="/history/" method="post"> <input type="submit" value="history" /></form>\n'
    #           '<form action="/favorite/" method="post"> <input type="submit" value="favorite" /></form>\n'
    #           '<form action="/add_to_favorite/" method="post"> <input type="submit" value="add to favorite" /></form>\n')
    #
    # he.insert(2,'<label/>\n')




    for i in range(50):
        he.append('<form action="/my/" method="post">\n'
                  '<input type="submit" value="'+str(i)+'" name="ff"/>\n'
                  '</form>\n')

        #btn = Button(win, text=i[1] + '   ->   ' + i[2])

    with open("./templates/history.html", "w") as outf:
        outf.write(str(soup))

    with open("./templates/history.html") as f:
        file = f.read()
        file = file.replace("&lt;", "<")
        file = file.replace("&gt;", ">")
    with open("./templates/history.html", "w") as w:
        w.write(file)



