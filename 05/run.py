from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    user = "Ari" 
    return render_template('home.html', title='Home', user=user)

@app.route('/profil')
def profil():
    user = "Ari" 
    return render_template('profile.html', title='Profil', user=user)

if __name__ == '__main__':
    app.run(debug=True)
