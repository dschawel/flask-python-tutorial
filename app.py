# YOUR FLASK APP HERE
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

# Database Set-up
client = MongoClient('mongodb://localhost:27017')
db = client['operators']

# declare app instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/loops')
def loops():
    return render_template('loops.html')

@app.route('/operators', methods=('GET', 'POST'))
def operators():
    if request.method == 'GET':
        operators = list(db.operators.find())
        return render_template('operators.html', operators=operators)
    elif request.method == 'POST':
        db.operators.insert_one({
            'name': request.form['name'],
            'description': request.form['description'],
            'symbol': request.form['symbol'],
            'example': request.form['example'],
            'uses': request.form['uses'],
        })
        return redirect('/operators')
    


# get the server up and running
if __name__ == '__main__':
    app.run(port=3000, debug=True)