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
    print()
    login = request.form['login']
    password = request.form['password']