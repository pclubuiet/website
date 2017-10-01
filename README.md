# Programming club UIET #
This is the official website of Programming club, UIET, Panjab University

## Quickstart ##

First, Fork the repository by clicking on the fork button on top right corner.
Then you will have a copy of this repo as your own like 'username/website.git'.

Secondly,you need to clone the repo:

    git clone https://github.com/username/website.git

cd to the repository

    cd website

Install the dependences

    pip install -r requirements.txt

Run the migrations and collect the static files

    python manage.py collectstatic
    python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

