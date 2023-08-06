# Gunicorn Torify

Turn any Gunicorn server into a Tor Onion Service

## Installation

It's available on [PyPI](https://pypi.org/project/gunicorn-torify/)! Just use pip to install

```bash
$ pip install gunicorn-torify
```

You must have [Tor](https://2019.www.torproject.org/docs/debian.html.en) installed to use gunicorn-torify.
This would might look like

```bash
# Arch
$ pacman -S tor
# Debian/Ubuntu
$ apt install tor
# Alpine
$ apk add tor
```

## Usage

If you don't use a [Gunicorn config file](https://docs.gunicorn.org/en/stable/settings.html#config-file), then create some python file such as `./gunicorn-conf.py` with the line

```python
from gunicorn_torify import on_starting, on_exit
```

Then when starting Gunicorn, be sure to include the `--config ./gunicorn-conf.py` flag.

## Contributing

To setup the development environment, it's convenient to use [pyenv](https://github.com/pyenv/pyenv) and the [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv) plugin.
For example

```bash
$ pyenv virtualenv 3.8.1 gunicorn-torify-3.8
$ pyenv activate gunicorn-torify-3.8
$ pip install -r requirements_dev.txt
```

## TODO

- Example with FastAPI & [uvicorn worker for Gunicorn](https://www.uvicorn.org/deployment/)
- Load balancing support?
- Docs about persistence of the secrets directory
- Proper tests
