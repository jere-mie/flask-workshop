# importing core Flask modules
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
import json

# this is for getting the secret key
with open('secrets.json') as f:
  data = json.load(f)

# creating an instance of Flask as our app
app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# create model for item
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'Item {self.id} => {self.content}'

# home
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

# add item
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        content = request.form['content']
        item = Item(content=content)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')

# view all items
@app.route('/view')
def view():
    items = Item.query.all()
    return render_template('view.html', items=items)

# delete item
@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('home'))

# update item
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.content = request.form['content']
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('update.html', item=item)

# this is what allows you to run the app
if __name__ == "__main__":
    # creating db if it doesn't exist
    if not os.path.exists('site.db'):
        db.create_all()

    # running the app
    app.run(debug=True)