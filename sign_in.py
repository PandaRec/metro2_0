from enum import Enum

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
import user
def enter():
    data_from_auth = work_database.get_auth_from_db()
    login = request.form['login']
    password = request.form['password']

    for i in data_from_auth:
        print()
        if i[1] == login and i[2] == password:
            one_user = user.current_user()
            one_user.set_id(i[0])
            one_user.set_login(i[1])
            one_user.set_phone(i[3])
            return one_user


