import re

from flask import Flask, render_template, request, flash
import work_database
import user
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
        data = work_database.get_auth_from_db()
        print()
        work_database.push_data_to_db_auth(login,pass1,phone,data[-1][0]+1)
        one_user = user.current_user()
        one_user.set_id(data[-1][0]+1)
        one_user.set_login(login)
        one_user.set_phone(phone)
        return one_user

