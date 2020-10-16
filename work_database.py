import server
from contextlib import closing
import psycopg2


def get_data_from_db(table_name, id='1'):
    if table_name.name == server.enum.favorite.name:
        rez = []
        with closing(psycopg2.connect(dbname='metro2_0', user='postgres',
                                      password='3400430', host='127.0.0.1')) as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + table_name.name + ' where id=' + id)
                for row in cursor:
                    print(row)
                    rez.append(row)
    else:
        rez = []
        with closing(psycopg2.connect(dbname='metro2_0', user='postgres',
                                      password='3400430', host='127.0.0.1')) as conn:
            with conn.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + table_name.name + ' where id=' + id)
                for row in cursor:
                    print(row)
                    rez.append(row)

    return rez


def push_data_to_db(table_name, start_point, end_point, id='1'):



    if table_name.name == server.enum.favorite.name:
        with closing(psycopg2.connect(dbname='metro2_0', user='postgres',
                                      password='3400430', host='127.0.0.1')) as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO ' + table_name.name + ' VALUES(' + id + ',' + '\'' + start_point + '\'' + ',' + '\'' + end_point + '\'' + ');')

    else:
        with closing(psycopg2.connect(dbname='metro2_0', user='postgres',
                                      password='3400430', host='127.0.0.1')) as conn:
            conn.autocommit = True
            with conn.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO ' + table_name.name + ' VALUES(' + id + ',' + '\'' + start_point + '\'' + ',' + '\'' + end_point + '\'' + ');')
