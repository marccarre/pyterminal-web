pyterminal-web
==============

An interactive Python terminal running as a webpage.
Demo available [here](http://pyterminal-web.herokuapp.com/ "Demo page")!

# Development

## Local

### Pre-requisites

- Python 3
- `pip`

### Setup

```console
$ pip install --upgrade pipenv
$ pipenv shell
$ pipenv install
```

### Run

```console
$ python index.py 0.0.0.0 1337
Bottle v0.11.6 server starting up (using WSGIRefServer())...
Listening on http://0.0.0.0:1337/
Hit Ctrl-C to quit.
```

## Heroku

Heroku requires a `requirements.txt` file for Python applications' dependencies.
To generate it using `pipenv`, run the following:

```console
$ pipenv install
Installing dependencies from Pipfile.lock (ef4847)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/1 — 00:00:00
$ pipenv lock --requirements > requirements.txt
```
