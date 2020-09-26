# importing in core Flask modules
from flask import Flask, render_template, url_for, redirect, request
import json

# this is for getting the secret key
with open('secrets.json') as f:
  data = json.load(f)

# creating an instance of Flask as our app
app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']

# redirect to homepage
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

# redirect to about page
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# redirect to contact page
@app.route('/contact', methods=['GET'])
def contact():
    contacts = ['Jeremie - Developer','Walid - UI/UX','Matt - Designer']
    return render_template('contact.html', contacts=contacts)

# method demonstrating receiving POST request
@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num = request.form['num']
        return redirect(url_for('calculate', num=num))
    else:
        return render_template('calc.html')

# method demonstrating passing in a parameter into a route
@app.route('/calculate/<int:num>', methods=['GET'])
def calculate(num):
    return render_template('result.html', number=num*3)

# this is what allows you to run the app
if __name__ == "__main__":
    app.run(debug=True)