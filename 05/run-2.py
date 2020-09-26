from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Wordl!'

if __name__ == '__main__':
    app.run(debug=True)

# langkah
# 1. jalankan virtual environment
# 2. install flask melalui pip
# 3. buat file run.py
# 4. export file tersebut
# 5. jalankan