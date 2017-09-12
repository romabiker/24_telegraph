# Telegraph Clone


Quickstart
----------

First, set your app's secret key as an environment variable. For example,
add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export TELEGRAPH_SECRET='something-really-secret'

Run the following commands to bootstrap your environment ::

    pip install -r requirements.txt
    export FLASK_APP=/path/to/autoapp.py
    export FLASK_DEBUG=1
    flask run       # start the flask server

Deployment
----------

To deploy:

    export FLASK_DEBUG=0
    flask run       # start the flask server

In your production environment, make sure the ``FLASK_DEBUG`` environment
variable is unset or is set to ``0``, so that ``ProdConfig`` is used.


Shell
-----

To open the interactive shell, run ::

    flask shell

By default, you will have access to the flask ``app``.


Managment commands
------------------

    flask lint    # Lint and check code style with flake8 and isort.
    flask clean   # Remove *.pyc and *.pyo files recursively starting at current directory.
    flask urls    # Display all of the url matching routes for the project.

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"
curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -
sudo apt-get update
sudo apt-get install heroku
v.r.@mail.ru