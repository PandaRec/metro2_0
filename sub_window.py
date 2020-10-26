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


def show_history_or_favorite(choice):
    if choice.name == server.enum.favorite.name:
        data = work_database.get_data_from_db_history_or_favorite(table_name=server.enum.favorite)
    else:
        data = work_database.get_data_from_db_history_or_favorite(table_name=server.enum.history)
    os.remove('templates/history_favorite.html')

    with open("templates/history_favorite.html", "w") as outf:
        outf.write('<!DOCTYPE html>\n'
'<html>\n'
    '<head>\n'
        '<meta content="text/html; charset=utf-8" http-equiv="content-type"/>\n'

        '<style>\n'
                   'form{\n'
        'text-align: center;\n'
        'margin-bottom: 5px;\n'
    '}\n'
    'input{\n'
        'width: 250px;\n'
        'background-color: white;\n'
        'border: 1px solid gray;\n'
    '}\n'
        '</style>\n'

    '</head>\n'

    '<body>\n'

    '</body>\n'
'</html>')

    with open('templates/history_favorite.html') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    he1=soup.find_all("style")
    he = soup.find("body")

    for i in data:
        rr = i[1] + '   ->   ' + i[2]
        aa = str.encode(rr, encoding='utf-8')
        aa = aa.decode(encoding='utf-8')

        he.append('<form action="/my/" method="post">\n'
                  '<input type="submit" value="'+aa+'" name="ff"/>\n'
                  '</form>\n')

    with open("templates/history_favorite.html", "w", encoding='utf-8') as outf:
        outf.write(str(soup))

    with open("templates/history_favorite.html", encoding='utf-8') as f:
        file = f.read()
        file = file.replace("&lt;", "<")
        file = file.replace("&gt;", ">")
    with open("templates/history_favorite.html", "w", encoding='utf-8') as w:
        w.write(file)

def show_friends_favorite(data):
    with open("templates/friends_favorite.html", "w") as outf:
        outf.write('<!DOCTYPE html>\n'
                   '<html>\n'
                   '<head>\n'
                   '<meta content="text/html; charset=utf-8" http-equiv="content-type"/>\n'

                   '<style>\n'
                   'form{\n'
                   'text-align: center;\n'
                   'margin-bottom: 5px;\n'
                   '}\n'
                   'input{\n'
                   'width: 250px;\n'
                   'background-color: white;\n'
                   'border: 1px solid gray;\n'
                   '}\n'
                   '</style>\n'

                   '</head>\n'

                   '<body>\n'

                   '</body>\n'
                   '</html>')

    with open('templates/friends_favorite.html') as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    he1 = soup.find_all("style")
    he = soup.find("body")

    print()

    for i in data:
        for j in i:
            print()
            rr = j[1] + '   ->   ' + j[2]
            aa = str.encode(rr, encoding='utf-8')
            aa = aa.decode(encoding='utf-8')

            he.append('<form action="/my/" method="post">\n'
                      '<input type="submit" value="' + aa + '" name="ff"/>\n'
                                                            '</form>\n')

        with open("templates/friends_favorite.html", "w", encoding='utf-8') as outf:
            outf.write(str(soup))

        with open("templates/friends_favorite.html", encoding='utf-8') as f:
            file = f.read()
            file = file.replace("&lt;", "<")
            file = file.replace("&gt;", ">")
        with open("templates/friends_favorite.html", "w", encoding='utf-8') as w:
            w.write(file)



