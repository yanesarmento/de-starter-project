import os
import string
import psycopg2
from flask import Flask, render_template, request, url_for, redirect,flash,jsonify
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='spotipy',
                            user="postgres",
                            password=4596,
                            port=5433)
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM data;')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=data)


@app.route("/addsong", methods = ['GET','POST'])
def addsong():
    if request.method == 'GET':
        return render_template("addsong.html", song={})

    if request.method == 'POST':
        name = request.form['name']
        album = request.form['album']
        artist = request.form['artist']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO data (name,album,artist)"
                        "VALUES (%s,%s,%s)",
                        (name,album,artist))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')

@app.route('/')        
def get_post(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    post = cursor.execute("SELECT id,name,album,artist FROM data WHERE id = id",(id))
    conn.commit()

    return post      

@app.route("/updatesong/<int:id>", methods = ['GET','POST'])
def updatesong(id):
    post = get_post(id)

    if request.method == 'GET':
        return render_template("updatesong.html", song={})

    if request.method == 'POST':
        name = request.form['name']
        album = request.form['album']
        artist = request.form['artist']


        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE data SET (name,album,artist) = (%s,%s,%s) WHERE id=%s",
                        (name,album,artist,id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    
    return render_template("updatesong.html",post=post)     

@app.route("/deletesong/<int:id>")
def delete(id):
    get_post(id)
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM data WHERE id=%s",(id,))     
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


if (__name__ == '__main__'):
    app.run()

