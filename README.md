# Programming club UIET #
This is the official website of Programming club, UIET, Panjab University

## Quickstart ##

1. Clone the repository:

    git clone https://github.com/pclubuiet/website.git

2. cd to the repository

    cd website

3. Create a virtualenv and install the dependences using the Makefile.

    make dev

4. Activate the virtualenv created in step 3

    source ./venv/bin/activate

5. Run the migrations and collect the static files

    python manage.py collectstatic
    python manage.py migrate

6. Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    python manage.py runserver

