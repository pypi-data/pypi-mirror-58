from pathlib import Path

from gunicorn_torify.api import on_starting, on_exit

try:
    from gunicorn_torify._version import __version__
except ImportError:
    __version__ = "0.0.0"
