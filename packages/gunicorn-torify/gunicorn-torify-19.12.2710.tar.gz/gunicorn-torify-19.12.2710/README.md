# Gunicorn Torify

Turn any Gunicorn server into a Tor Onion Service

## Installation

It's available on [PyPI](https://pypi.org/project/gunicorn-torify/)! Just use pip to install

```bash
$ pip install gunicorn-torify
```

You must have [Tor](https://2019.www.torproject.org/docs/debian.html.en) installed to use gunicorn-torify.
This might look like

```bash
$ pacman -S tor    # Arch
$ apt install tor  # Debian/Ubuntu
$ apk add tor      # Alpine
```

## Usage

Just add these imports to your [Gunicorn config file](https://docs.gunicorn.org/en/stable/settings.html#config-file) (or create some python file such as `./gunicorn-conf.py` with the line):

```python
from gunicorn_torify import on_starting, on_exit
```

When starting Gunicorn, be sure to include the `--config ./gunicorn-conf.py` flag.

### Persistence

By default, the Onion Service will store its secret keys in `./secrets/tor`.
To override this you can set the `TOR_SERVICE_DIR` environment variable before running for the first time.
According to the [tor docs](https://2019.www.torproject.org/docs/tor-onion-service.html.en#two) this directory contains private keys and should be treated carefully.

If deploying in Docker, it's important to persist this directory (otherwise your onion address could change) either with a named volume or a mapped directory.
An example deployment could be done with

```bash
$ docker volume create my-onion-service
$ docker run -v my-onion-service:/app/secrets/tor afiorillo/gunicorn-torify:flask
```

## Contributing

To setup the development environment, it's convenient to use [pyenv](https://github.com/pyenv/pyenv) and the [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv) plugin.
For example

```bash
$ pyenv virtualenv 3.8.1 gunicorn-torify-3.8
$ pyenv activate gunicorn-torify-3.8
$ pip install -r requirements_dev.txt
```
