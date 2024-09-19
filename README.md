# Intro to Flask Workshop

Presentation and supporting materials for my Intro to Flask Workshop

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
3. Run `pip install -r requirements.txt` in your terminal, powershell, or command prompt. (Note, you might need to use `pip3` instead of `pip`)
4. Copy the sample `.env` file and edit it as you see fit
    ```bash
    cp example.env .env
    ```
5. Run `python3 app.py` (note, you may need to use `py` or `python` instead of `python3`)
6. Head to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to preview the web app!

## Sample Code Overview

### app.py

This is the main Flask app, containing all of the routes and backend logic.

### .env

This contains the secret key and port of the Flask app. Note that one is not provided in this repository. This is because you should always add your `.env` file to your `.gitignore`, as you don't want others to know your secret key or other sensitive info. Note that if you want to know how to format your `.env` file, check out the `example.env` file.

### .gitignore

This file contains all of the files and folders you do not want added to the git repository. Generally you include things like `.env`, `site.db` (SQLite database), `venv` folder, and `__pycache__` folder.

### static/

This folder contains all static files you want to use in your Flask app. This would include css files, images, javascript files, etc.

### templates/

This folder contains all of your HTML templates. Usually you use a layout.html for things like metadata and a navbar, and then you create other templates that extend this template.
