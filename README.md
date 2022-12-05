# Starlette

![starlette](https://www.starlette.io/img/starlette.png)

<p>Starlette is a lightweight <a href="https://asgi.readthedocs.io/en/latest/">ASGI</a> framework/toolkit,
which is ideal for building async web services in Python.</p>

## Requirements

Python 3.7+

## Installation

```bash
pip install starlette
```

<p>You'll also want to install an ASGI server, such as <a href="http://www.uvicorn.org/">uvicorn</a>, <a href="https://github.com/django/daphne/">daphne</a>, or <a href="https://pgjones.gitlab.io/hypercorn/">hypercorn</a>.</p>

```bash
pip install uvicorn
```

## run
```bash
uvicorn example:app
```