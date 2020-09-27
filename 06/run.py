from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    user = "Kadek" 
    return render_template('home.html', title='Home', user=user)

@app.route('/input')
def input():
    return render_template('input.html', title='Input')

@app.route('/actInput', methods=["POST"])
def actInput():
    nama = request.form.get('nama')
    return render_template('hasil.html', title='Home', nama=nama)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/hasil/<angka>')
def hasil(angka):
    angka = angka
    return render_template('hasil.html', title='Home', angka=angka)


if __name__ == '__main__':
    app.run(debug=True)