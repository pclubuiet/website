# Programming Club UIET
This is the official website of the Programming Club at UIET, Panjab University.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e745e9b4af624b4684559e8fc1e95697)](https://www.codacy.com/app/divyam3897/website?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pclubuiet/website&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/pclubuiet/website.svg?branch=master)](https://travis-ci.org/pclubuiet/website)

## Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Development Workflow

### Setup your database in PostgreSQL (Linux Specific)
1.  Install postgresql if you haven't already and switch to ```postgres```(PostgreSQL administrative user) for performing administrative tasks.
    ```
    sudo su - postgres
    ```

2. Run Postgres Service
    ```
    systemctl start postgresql
    ```

3. Log into Postgres session.
    ```
    psql
    ```

4. Create a database for our project.
    ```
    CREATE DATABASE pclubuietdb;
    ```

5. Create a database user.
    ```
    CREATE USER pclubuietdb WITH PASSWORD 'pclubuietdb';
    ```

6. Give access rights of the database to the user.
    ```
    GRANT ALL PRIVILEGES ON DATABASE pclubuietdb TO pclubuietdb;
    ```

7. Exit SQL prompt.
    ```
    \q
    ```

8. Exit out of ```postgres``` user's shell session.
    ```
    exit
    ```

9. Edit your hosts file.
    ```
    sudoedit /etc/hosts
    ```
   Add the following entry to the hosts file.
    ```
    127.0.0.1	pclubuietdb
    ```

### Setup your development environment
1. Fork this repository to your account.

2. Create a virtual environment on your machine.
    ```
    virtualenv -p python3 env
    ```
    We recommend using python3-virtualenv. Any other packages would do fine though.

3. Activate the newly created virtual environment.
    ```
    cd env
    source bin/activate
    ```

4. Clone this repository (this would make rebasing easier).
    ```
    git clone https://github.com/pclubuiet/website.git
    ```

5. Install the dependencies for the project.
    ```
    cd website
    pip3 install -r requirements.txt
    ```

6. Change ```DEBUG=True``` in /pclubWebsite/settings.py file (DO NOT COMMIT this change to settings.py in your PRs).

7. Run the migrations and collect static files.
    ```
    python3 manage.py migrate
    python3 manage.py collectstatic
    ```

8. Run the live development server on your machine and test it.
    ```
    python3 manage.py runserver
    ```
    Once the server is started, open http://127.0.0.1:8000/home in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.

9. Add a remote to your forked repository. This remote will be needed to push your changes to your repo.
    ```
    git remote add myfork https://github.com/<username>/website.git
    ```

### Running in Docker Compose
Prerequisites:
1. Ensure you have Docker Engine installed. For installation steps head to https://docs.docker.com/engine/installation/.
2. Ensure you have Docker Compose installed. For installation steps head to https://docs.docker.com/compose/install/.

### Start / stop the environment.

1. Start and aggregate logs from containers to console.
    ```
    docker-compose up
    ```

    To stop press `CTRL+C`


2. Start in background
    ```
    docker-compose up -d
    ```
    To stop:
    ```
    docker-compose stop
    ```

If you want to force Compose to stop and recreate all containers, use the `--force-recreate` flag.

## Fixing issues
### Step 1: Pick an issue
After selecting an issue
1. Comment on the issue saying that you are working on the issue.
2. We expect you to discuss the approach by comments.
3. Updates or progress on the issue would be nice.

### Step 2: Follow branch policies
1. Create a new branch and switch to it (make sure you are on master before doing this).
    ```
    git branch mybranch
    git checkout mybranch
    ```
    'mybranch' can be replaced by your preferred name for the branch.
    The above two commands are equivalent to the following
    ```
    git checkout -b mybranch
    ```

2. Make your changes and then execute the tests to make sure you didn't break anything.

    ```
    python3 manage.py test
    ```
    Ensure that you follow [PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) style guide for python code while naming functions or classes.

    Then stage them and commit them.
    Check out Chris Beams's guide to writing good commit messages [here](https://chris.beams.io/posts/git-commit/).

    *A small description of your changes is must in the commit messages.*

3. After you are done making changes, push the branch to your fork.
    ```
    git push -u myfork mybranch
    ```
    The **-u** option is required only the first time you push the branch.

 Make sure your branch is up-to-date with the latest version of the master. Else you are required to do a rebase to place your changes above master branch.

### Step 3: Follow Coding policy

 1. Please help us follow the best practice to make it easy for the reviewer as well as the contributor. We want to focus on the code quality more than on managing pull request ethics.
 2. Single commit per pull request
 3. For writing commit messages please adhere to the Commit style guidelines.
 4. Follow uniform design practices.
 5. The pull request will not get merged until and unless the commits are squashed. In case there are multiple commits on the PR, the commit author needs to squash them and not the maintainers cherrypicking and merging squashes.
 6. If the PR is related to any front end change, please attach relevant screenshots in the pull request description.

### Step 4: Submitting a Pull request
Once a PR is opened, try and complete it within 2 weeks, or at least stay actively working on it. Inactivity for a long period may necessitate a closure of the PR. As mentioned earlier updates would be nice.

Deploy to heroku using the badge provided above and post the link in the description of your PR.

### Step 5: Code Review

Your code will be reviewed, in this sequence, by:

1. Travis CI: by building and running tests. If there are failed tests, the build will be marked as a failure. You can consult the CI log to find which tests. Ensure that all tests pass before triggering another build.
2. Reviewer: A core team member will review your pull request and approve it or he will suggest changes.

### Step 6: Help us by reviewing other Pull Requests!
If you have the time and the knowledge then you must review other Pull Requests. This would stop Pull Requests from stacking up and will definitely mean your Pull Request would be reviewed faster.

**Things to keep in mind while reviewing a Pull Request:**

If any of the following questions has a **YES** for an answer then the request shall **NOT** be approved.
* Will the referenced issue **NOT** be fixed with the Pull Request?
* Is the commit message **NOT** good?
* Are there unnecessary changes?
* Is a rebase required?
* Is the fix dirty / hacky?

###We Hope that above details helped you Thank You!!


## License

This website is licensed under [GPL V3+](https://www.gnu.org/licenses/gpl-3.0.fr.html)


