from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Wordl!'
    #return render_template('home.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)

# langkah
# 1. jalankan virtual environment
# 2. install flask melalui pip
# 3. buat file run.py
# 4. export file tersebut
# 5. jalankan