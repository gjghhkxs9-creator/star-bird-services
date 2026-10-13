from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return render_template_string("""
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>Star Bird Services</title>
            <style>
                body { background-color: #000; color: #fff; text-align: center; padding-top: 100px; font-family: sans-serif; }
            </style>
        </head>
        <body>
            <h1>مرحباً بك في موقعي 🚀</h1>
            <p>الموقع يعمل بنجاح وبشكل متواصل!</p>
        </body>
        </html>
        """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
