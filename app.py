# importing core Flask modules
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os
import json
import sys

# this is for getting the secret key
with open('config.json') as f:
    config = json.load(f)

# creating an instance of Flask as our app
app = Flask(__name__)
app.config['SECRET_KEY'] = config['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# creating database connection variable
db = SQLAlchemy()
db.init_app(app)

# create model for item
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f'<Item {self.id} => {self.name}>'

# home
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# add item
@app.route('/add', methods=['GET', 'POST'])
def add():
    # if a form is submitted
    if request.method == 'POST':
        name = request.form['name']
        item = Item(name=name)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('add'))
    # if a user is going to the page
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
    return redirect(url_for('view'))

# update item
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)

    # if a form is submitted
    if request.method == 'POST':
        item.name = request.form['name']
        db.session.commit()
        return redirect(url_for('view'))
    # if a user is going to the page
    else:
        return render_template('update.html', item=item)


# running the site
if __name__=='__main__':

    # creating db if it doesn't exist
    if not os.path.exists('instance/site.db'):
        print("Database not found, creating...")
        with app.app_context():
            db.create_all()

    # run this command with any additional arg to run in production
    if len(sys.argv) > 1:
        print('<< PROD >>')
        os.system(f"gunicorn -b '0.0.0.0:{config['port']}' app:app")
    # or just run without an additional arg to run in debug
    else:
        print('<< DEBUG >>')
        app.run(debug=True)
