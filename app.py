from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

USER_DATA_FILE = 'users.txt'

def save_user(username, password):
    with open(USER_DATA_FILE, 'a') as f:
        f.write(f'{username},{password}\n')

def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            saved_username, _ = line.strip().split(',')
            if saved_username == username:
                return True
    return False

def verify_user(username, password):
    if not os.path.exists(USER_DATA_FILE):
        return False
    with open(USER_DATA_FILE, 'r') as f:
        for line in f:
            saved_username, saved_password = line.strip().split(',')
            if saved_username == username and saved_password == password:
                return True
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/levels')
def levels():
    return render_template('levels.html')  # اینجا فایل levels.html را اضافه کن

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if user_exists(username):
            return "User already exists", 400
        
        save_user(username, password)
        return redirect(url_for('home'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if verify_user(username, password):
            return redirect(url_for('home'))
        
        return "Invalid username or password", 400
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)