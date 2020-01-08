# Password Vault

Password Vault is a Django/Python3 app that allows a user to create, store, and delete login information for websites.

Live link: [Password Vault](https://python-vault.herokuapp.com/)

## Table of contents
* App Features
* Technologies
* Setup
* Code Examples
* Deployment
* To-Do List
* Acknowledgments


## Features
List of features that are functional and TODOs for future development
* Authentication: user can register, login, and logout
* User views change with authentication
* Create, view a list of password information, and delete password data

## To-Do's
* User can save passwords to their own profile
* Show page for each password with edit functionality
* User can generate random new password by clicking "Generate Random" button
* Improve styling all around
* Make forms more responsive and add styling

## Built With These Technologies
* [Python 3](https://www.python.org/): programming language
* [Django 3](https://www.djangoproject.com/): Python framework that uses model-template-view pattern to create database-driven applications
* [PostgreSQL](https://www.postgresql.org/): relational database management
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/): web template engine for Python, allows you to mesh HTML with Python
* Bootstrap/CSS: styling
* HTML
* JavaScript


## Setup

### Creating A Virtual Environment
To create my project I had to set up a virtual environment in the terminal, or a "self-contained directory tree that contains a Python installation for a particular version of Python, and any required packages"(https://docs.python.org/3/tutorial/venv.html).

I ran the `venv` module to create my directory called python_project:
```
$ python3 -m venv python_project-env
```

Then in order to activate my virtual environment whenever I wanted to work on my app, I would run:
```
$ source ./venv/bin/activate
```

When inside of the virtual environment, there will be `(venv)` before your CLI username:
```
(venv) Ashleys-MBP-3:python_project ashleybrickhouse$
```

### Managing Packages
I used a program called `pip` to install packages and manage features

For example, to install Django, I ran the following command:
```
(venv) Ashleys-MBP-3:python_project ashleybrickhouse$   pip install django
```

In order to view the packages I was running, I'd use:
`$ pip freeze`


## Code Examples
This stack was completely new for me so I learned a lot of different syntaxes:

### Jinja
Jinja syntax allowed me to pull python expressions into HTML (similar to using the squidwizard hats to write Javascript or PHP inside of HTML)

For example, after creating my base.html file, I used it like a partial and pulled it into my other templates using Jinja (this particular line of code is placed at the very top of the template file or view)
```
{% extends 'base.html' %}
```

### Testing
I used print() to print code into the terminal and figure out why something was or wasn't working (it's similar to console.log() in Javascript)
```
print('asdf')
```

## Deployment

I deployed using Heroku, and Gunicorn
The following files were required in my root directory in order for it to recognize it as a Python/Django app:
* Procfile: indicates the processes that need to be run to load the app, and which folder to look in for the server info
* requirements.txt: includes packages needed to run the app


## Acknowledgments

* Dramatic hat tip to anyone whose code was used or referenced heavily (thank you!!!)
