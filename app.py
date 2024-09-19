# importing core Flask modules
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
import json
import sys
from dotenv import load_dotenv

load_dotenv() # get config variables from .env file

# creating an instance of Flask as our app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'sample_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# creating database connection variable
db = SQLAlchemy(app)

# create model for item
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

# home page
@app.get('/')
def home_page():
    return render_template('home.html')

# add item page
@app.get('/add')
def add_page():
        return render_template('add.html')

# this route is called when the form is submitted on the add page
@app.post('/add')
def add_form():
    name = request.form['name']
    item = Item(name=name)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('add_page'))

# view all items
@app.get('/view')
def view_page():
    items = Item.query.all()
    return render_template('view.html', items=items)

# delete item
@app.get('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('view_page'))

# update item page
@app.get('/update/<int:id>')
def update_page(id):
    item = Item.query.get_or_404(id)
    return render_template('update.html', item=item)

# this route is hit when the update item form is submitted
@app.post('/update/<int:id>')
def update_form(id):
    item = Item.query.get_or_404(id)
    item.name = request.form['name']
    db.session.commit()
    return redirect(url_for('view_page'))

# running the site
if __name__=='__main__':
    # creating db if it doesn't exist
    if not os.path.exists('instance/site.db'):
        print("Database not found, creating...")
        with app.app_context():
            db.create_all()
    PORT = os.environ.get("PORT", "5000")
    app.run(debug=True, port=PORT)
