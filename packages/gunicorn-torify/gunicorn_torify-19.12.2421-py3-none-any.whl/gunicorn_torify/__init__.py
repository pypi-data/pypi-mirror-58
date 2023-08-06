from pathlib import Path

from gunicorn_torify.api import on_starting, on_exit

try:
    __version__ = Path(__file__).with_name("version").read_text()
except OSError:
    __version__ = "0.0.0"
