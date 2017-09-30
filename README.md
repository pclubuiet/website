# Programming club UIET #
This is the official website of Programming club, UIET, Panjab University

## Quickstart ##

1. Fork the repository (button found in top right corner of this repository):

    This will create an exact copy of this repository and will add it to your account.


2. Clone the forked repository:

    `git clone https://github.com/your-username/website.git`


3. Open the cloned folder on your local machine (cd into the cloned directory):

    `cd website`

4. Install the dependences:

    `pip install -r requirements.txt`

5. Run the migrations and collect the static files:

    `python manage.py collectstatic`

    `python manage.py migrate`

6. Once setup is completed (above steps) you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    `python manage.py runserver`

