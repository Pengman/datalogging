# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, flash, redirect
import peewee
import flask_admin as admin
from flask_admin.contrib.peewee import ModelView

import data

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT' #NOT SECRET!!!

@app.route('/')
def index():
    links = [
        (u'Vægt', url_for('vaegt')),
        (u'Søvn', url_for('soevn')),
        (u'Bank', url_for('bank'))
,
        (u'Bank2', url_for('bank2'))
        ]

    return render_template('index.html', links = links)

@app.route('/vaegt', methods=['GET', 'POST'])
def vaegt():
    if request.method == 'POST':
        # do_the_login()
        app.logging.debug("@return")
    else:
        return "helpdesk"


@app.route('/soevn', methods=['GET', 'POST'])
def soevn():
    if request.method == 'POST':
        # do_the_login()
        app.logger.debug("@return")
        app.logger.debug(request.form)
        flash('New entry was successfully posted')
        return redirect(url_for('index'))
    else:
        return render_template('soevn.html')

@app.route('/bank', methods=['GET', 'POST'])
def bank():
    if request.method == 'POST':
        # do_the_login()
        app.logging.debug("@return")
    else:
        return render_template('bank.html')

@app.route('/bank2', methods=['GET', 'POST'])
def bank2():
    if request.method == 'POST':
        # do_the_login()
        app.logging.debug("@return")
    else:
        return render_template('bank_vue.html')

app.run(debug = True)
