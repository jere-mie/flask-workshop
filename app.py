from flask import Flask, render_template, url_for, flash, redirect, request
import json

with open('secrets.json') as f:
  data = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = data['secret_key']


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num = request.form['num']
        return redirect(url_for('calculate', num=num))
    else:
        return render_template('calc.html')

@app.route('/calculate/<int:num>', methods=['GET'])
def calculate(num):
    return render_template('result.html', number=num*3)


if __name__ == "__main__":
    app.run(debug=True)