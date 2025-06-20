print("Hello from Render!")
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Привет! Это мой сайт, и он работает!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))  # Render использует переменную PORT
    app.run(host='0.0.0.0', port=port)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ⚙️ логин и пароль (их будет генерировать бот позже)
correct_username = "user123"
correct_password = "pass456"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == correct_username and password == correct_password:
            return redirect(url_for('home'))
        else:
            error = 'Неверный логин или пароль!'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
