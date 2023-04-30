# MasseyHacks 2023 ~ Intro to Flask Workshop

Presentation and supporting materials for my MasseyHacks 2023 Intro to Flask Workshop  
Created and presented by Jeremie Bornais

## Slides

View slides [here](docs/slides.pdf).

## Resources

Another helpful tutorial can be found [here](https://www.youtube.com/watch?v=Z1RJmh_OqeA).

## How to run this app

1. Make sure you have [Python and pip installed](https://www.python.org/)
2. Clone this git repository
    ```bash
    git clone https://github.com/jere-mie/flask-workshop
    ```
3. Run `pip install flask flask-sqlalchemy` in your terminal, powershell, or command prompt. (Note, you might need to use `pip3` instead of `pip`)
4. Copy the sample config file and edit it as you see fit
    ```bash
    cp example_config.json config.json
    ```
5. Run `python3 app.py` (note, you may need to use `py` instead of `python3`)
6. Head to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to preview the web app!

## Sample Code Overview

### app.py

This is the main Flask app, containing all of the routes and backend logic

### config.json

This contains the secret key of the Flask app. Note that one is not provided in this repository. This is because you should always add your secrets.json to your .gitignore, as you don't want others to know your secret key. Note that if you want to know how to format your secrets.json, check out the secrets_example.json file.

### .gitignore

This file contains all of the files and folders you do not want added to the git repository. Generally you include things like config.json, site.db (SQLite database), venv folder, and __pycache__ folder.

### static/

This folder contains all static files you want to use in your Flask app. This would include css files, images, javascript files, etc.

### templates/

This folder contains all of your HTML templates. Usually you use a layout.html for things like metadata and a navbar, and then you create other templates that extend this template
