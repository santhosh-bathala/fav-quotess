from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Anvi123@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kfqdlhchyzrmry:a555b368b758d4c80313ea5e166f3d9cf4cedafd902b6b7e0a7aa2e096429092@ec2-52-23-45-36.compute-1.amazonaws.com:5432/de3b9h9o98ceet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html', result = result)

@app.route('/qoutes')
def qoutes():
    return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author = author, quote = quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))
