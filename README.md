# Programming club UIET #
This is the official website of Programming club, UIET, Panjab University

## Setting up your Development Environment ##
1. First, fork this repository to your account.

2. Create a virtual environment on your machine. 
    ```
    virtualenv env
    ```
    We recommend using python-virtualenv. Any other packages would do fine though.

3. Activate the newly created virtual env:
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
    
6. Run the migrations and collect staticfiles
    ```
    python manage.py migrate
    python manage.py collectstatic
    ```
    
7. Run the live development server on your machine and test it.
    ```
    python manage.py runserver
    ```
    Once the server is started, open http://127.0.0.1:8000/home in a web browser.
    Everything went well if the webpage loads correctly and you don't see any errors.
    
8. Add a remote to your forked repository. This remote will be needed to push your changes to your repo.
    ```
    git remote add myfork https://github.com/<username>/website.git
    ```
    
9. Find an issue in this repository that you would like to and can fix.
   Start working on an issue. Steps 10 and beyond will guide you in doing this.

   **In case multiple people are working on the same issue, the Pull Request that is completed first shall be given**
   **the highest preference. The reviews will be on a first come first service basis.**   
   
10. Create a new branch and switch to it. (make sure you are on master before doing this).
    ```
    git branch mybranch
    git checkout mybranch
    ```
    'mybranch' can be replaced by your preferred name for the branch.
    The above to commands are equivalent to the following
    ```
    git checkout -b mybranch
    ```

11. Make your changes.
	
	Ensure that you follow [PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) style guide for python code while naming functions or classes.

    Then stage them and commit them.
    Check out Chris Beams's guide to writing good commit messages [here](https://chris.beams.io/posts/git-commit/).

    *A small description of your changes is must in the commit messages.* 

12. After you are done making changes, push the branch to your fork.
    ```
    git push -u myfork mybranch
    ```
    The **-u** option is required only the first time you push the branch.
	In case you have made multiple commits, you need to squash them into a single commit before pushing.

13. Then create a Pull Request from that branch using GitHub.

**What after you have submitted a Pull Request?**

Well, you could wait for it to be reviewed by someone or you could attempt to fix another issue. 

*OR*

You could help us in an even better way! 


### Help us by reviewing others' Pull Requests! ###
If you have the time and the knowledge then you must review others' Pull Requests. This would stop Pull Requests from stacking up and will definitely mean your Pull Request would be reviewed faster.

**Things to keep in mind while reviewing a Pull Request**

If any of the following questions has a **yes** for an answer then the request shall **not** be approved.
* Will the referenced issue **not** be fixed with the Pull Request?
* Are there unnecessary changes?
* Is the commit message **not** good?
* Is a rebase required?
* Is the fix dirty (hacky)?

*Reviewers shall make sure that the reviews are done on a first come first service basis.*
