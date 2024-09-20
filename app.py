from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # دریافت اطلاعات از فرم لاگین
        username = request.form['username']
        password = request.form['password']
        # انجام عملیات لاگین (تأیید هویت)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # دریافت اطلاعات از فرم ساین آپ
        username = request.form['username']
        password = request.form['password']
        # انجام عملیات ثبت‌نام
        return redirect(url_for('home'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)