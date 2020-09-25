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
def home():
    return render_template('home.html')

@app.route('/contact', methods=['GET'])
def home():
    return render_template('home.html')
