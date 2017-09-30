# Programming club UIET #
This is the official website of Programming club, UIET, Panjab University

## Quickstart ##

First, clone the repository:

    git clone https://github.com/pclubuiet/website.git

cd to the repository

    cd website

Install the dependences

    pip install -r requirements.txt

Run the migrations and collect the static files

    python manage.py collectstatic
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

