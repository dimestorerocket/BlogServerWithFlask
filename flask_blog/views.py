#flask_blog/views.py
from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('/index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('User Name Not Found')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Password Is Incorrect')
        else:
            session['logged_in'] = True
            flash('Login Successful')
            return redirect('/')
    return render_template('/login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged Out')
    return redirect('/')