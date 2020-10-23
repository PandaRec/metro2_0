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
def enter():
    data_from_auth = work_database.get_auth_from_db()
    login = request.form['login']
    password = request.form['password']

    for i in data_from_auth:
        print()
        if i[1] == login and i[2] == password:
            return True


