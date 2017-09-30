# Programming club UIET #
This is the official website of Programming club, UIET, Panjab University

## Quickstart ##

First, clone the repository:

    git clone https://github.com/pclubuiet/website.git

Create a [virtual environment](https://pypi.python.org/pypi/virtualenv)
    
    virtualenv venv

Activate the virtual environment to isolate the working environment

    source venv/bin/activate

cd to the repository

    cd pclubuiet

Install the dependences

    pip install -r requirements.txt

Run the migrations and collect the static files

    python manage.py collectstatic
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

