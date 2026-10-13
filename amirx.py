from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return "مرحباً بك في خدمات تأمين وحماية الأجور - الموقع قيد التحديث"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
