# WinHacks 2022 Intro to Flask Workshop
Presentation and supporting materials for my WinHacks 2022 Intro to Flask Workshop
Created and presented by Jeremie Bornais

#### View Slides [Here](https://docs.google.com/presentation/d/1jZTET3T5VZQlNugtnz1M5ggtMgseNeJx8KEe8Rrf5Ps/edit?usp=sharing)

### To run this app, make sure you 'pip install flask' first
### Another helpful tutorial can be found [here](https://www.youtube.com/watch?v=Z1RJmh_OqeA)

## Sample Code Overview
##### app.py
This is the main Flask app, containing all of the routes and backend logic

##### secrets.json
This contains the secret key of the Flask app. Note that one is not provided in this repository. This is because you should always add your secrets.json to your .gitignore, as you don't want others to know your secret key. Note that if you want to know how to format your secrets.json, check out the secrets_example.json file.

##### .gitignore
This file contains all of the files and folders you do not want added to the git repository. Generally you include things like secrets.json, site.db (SQLite database), venv folder, and __pycache__ folder.

##### static/
This folder contains all static files you want to use in your Flask app. This would include css files, images, javascript files, etc.

##### templates/
This folder contains all of your HTML templates. Usually you use a layout.html for things like metadata and a navbar, and then you create other templates that extend this template

## How to run this app
1. Make sure you have Python and pip installed
2. Clone this git repository
3. Run 'pip3 install flask' in your terminal, powershell, or command prompt
4. Create a file in the flask-workshop directory called 'secrets.json' containing your secret key (this can be anything)
5. Run 'python3 app.py'
6. Head to http://127.0.0.1:5000/ to preview the web app