Prerequisites:

- [python 3.7](https://www.python.org/downloads/)
- [pipenv](https://docs.pipenv.org/en/latest/) for installing dependencies (required to run locally)
- [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) for deployment to Heroku

Install the project:

```
git clone git@github.com:ir-regular/neuromart.git
pipenv install
```

Run a local version with [werkzeug debugger](https://werkzeug.palletsprojects.com/en/0.15.x/debug/#using-the-debugger)
enabled:

```
pipenv shell
FLASK_APP=neuromart
FLASK_ENV=development
flask run
```

...and then go to `http://127.0.0.1:5000/` in your browser.

Test Heroku deployment locally:

```
pipenv shell
heroku local web
```

...and then go to `http://127.0.0.1:5000/` in your browser.
