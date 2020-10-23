import re

from flask import Flask, render_template, request, flash
import work_database
def registr():
    name = request.form['nm']
    sername = request.form['sername']
    login = request.form['login']
    pass1 = request.form['pass1']
    pass2 = request.form['pass2']
    phone = request.form['phone']
    check = ''
    try:
        check = request.form['check']
    except:
        check = 'no'

    if pass1!=pass2:
        return False

    elif re.search(r"^([7]\d{10})$", phone, re.MULTILINE)==None:
        return False
    elif check=='no':
        return False
    else:
        work_database.push_data_to_db_auth(login,pass1,phone,2)



    print()
    print()