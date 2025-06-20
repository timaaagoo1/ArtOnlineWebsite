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
