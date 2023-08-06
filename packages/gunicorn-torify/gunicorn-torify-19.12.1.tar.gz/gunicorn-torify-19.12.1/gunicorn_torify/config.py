from os import environ
from pathlib import Path

TORRC_PATH = Path(environ.get("TORRC_PATH", "./torrc"))
TOR_SERVICE_DIR = Path(environ.get("TOR_SERVICE_DIR", "./secrets/tor"))
