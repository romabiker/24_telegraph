# Telegraph Clone

This project is a clone of the [telegra.ph](http://telegra.ph). Telegraph has no registration, you can subscribe to any name. There are only three fields: "title", "signature", "telegram". After publication, a unique link to the posted post is issued.
If you do not store cookies, then after closing the window, the post can not be edited later. You need to keep a link to your post to return to it.

### [Tele.graph](https://mighty-bayou-22893.herokuapp.com)

Quickstart
----------


Run the following commands to install project locally for developing:

```
    git clone https://github.com/romabiker/24_telegraph.git
    cd 24_telegraph
    pipenv shell   # activates virtual environment
    pipenv install #automaticaly installs all dependacies from Pipfile
    pipenv graph   # shows all installed dependancies
    export FLASK_APP=autoapp.py
    flask key
    export TELEGRAPH_SECRET="paste from cli generated flask key"
    export FLASK_DEBUG=1
    flask run       # start the flask developer server for autoreloading on changes
    gunicorn autoapp:app # also you may try production server
```

Shell
-----

To open the interactive shell, run
```
    flask shell
```
By default, you will have access to the flask ``app``.


Managment commands
------------------

```
    flask clean   # Remove *.pyc and *.pyo files recursively starting at current directory.
    flask key     # Generate secret key
```

Deployment
----------

Project is prepared for deployment to Heroku cloud

To deploy:

Register on Heroku

[Download and install Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

Run the following commands:

```
    Heroku login
    git clone https://github.com/romabiker/24_telegraph.git
    cd 24_telegraph
    heroku create # creates application
    pipenv shell   # activates virtual environment
    pipenv install #automaticaly installs all dependacies from Pipfile
    heroku local web  # to check server locally
    git push heroku master  # deploy and after that visit dashboard settings on Heroku to provide TELEGRAPH_SECRET
    heroku ps:scale web=1 # runs project
    heroku open   # opens in browser
    heroku logs --tail # to see logging

```



## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
