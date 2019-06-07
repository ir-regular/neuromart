Prerequisites:

- [python 3.7](https://www.python.org/downloads/)
- [pipenv](https://docs.pipenv.org/en/latest/) for installing dependencies (required to run locally)
- [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) for deployment to Heroku

---

Install the project:

```
git clone git@github.com:ir-regular/neuromart.git
pipenv install
```

---

Run a local version with code reloading and
[werkzeug debugger](https://werkzeug.palletsprojects.com/en/0.15.x/debug/#using-the-debugger)
enabled:

```
pipenv shell
FLASK_APP=neuromart
FLASK_ENV=development
flask run
```

...and then go to `http://127.0.0.1:5000/` in your browser.

---

Set up the above as a single-click action in [PyCharm](https://www.jetbrains.com/pycharm/):

_Note: I'm assuming you're using a Community Edition here; Pro edition integrates with Flask out of the box_

0. Make sure to run `pipenv install` first
1. Run `pipenv --venv` and note the directory somewhere
2. Edit Configurations
3. Add New Configuration > Python
    1. Name: "neuromart (development)"
    2. Script path: `{output of pipenv --venv}/bin/flask`
    3. Parameters: `run`
    4. Environment variables: `PYTHONUNBUFFERED=1;FLASK_APP=neuromart;FLASK_ENV=development`
    5. Working directory: select your local neuromart project directory
    6. Save configuration by pressing OK

Now you can start the server from PyCharm and see the server output in Run tab.

---

Test Heroku deployment locally:

```
pipenv shell
heroku local web
```

...and then go to `http://127.0.0.1:5000/` in your browser.
