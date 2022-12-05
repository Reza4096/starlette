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

## Dependencies

<p>Starlette only requires <code>anyio</code>, and the following dependencies are optional:</p>

<ul>
<li><a href="https://www.python-httpx.org/"><code>httpx</code></a> - Required if you want to use the <code>TestClient</code>.</li>
<li><a href="http://jinja.pocoo.org/"><code>jinja2</code></a> - Required if you want to use <code>Jinja2Templates</code>.</li>
<li><a href="https://andrew-d.github.io/python-multipart/"><code>python-multipart</code></a> - Required if you want to support form parsing, with <code>request.form()</code>.</li>
<li><a href="https://pythonhosted.org/itsdangerous/"><code>itsdangerous</code></a> - Required for <code>SessionMiddleware</code> support.</li>
<li><a href="https://pyyaml.org/wiki/PyYAMLDocumentation"><code>pyyaml</code></a> - Required for <code>SchemaGenerator</code> support.</li>
</ul>

<p>You can install all of these with <code>pip3 install starlette[full]</code>.</p>

## ToDo

https://www.starlette.io/requests/