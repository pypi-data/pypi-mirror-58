"""
Contains the functions to call in a Gunicorn's server hooks
"""
from gunicorn_torify.tor import utils


def on_starting(server):
    # steal the server's log
    log = server.log

    bind, port = server.address[0]
    log.info("starting locally on {bind}:{port} ...".format(bind=bind, port=port))

    # ensure tor is installed/running
    if not utils.is_tor_installed():
        raise RuntimeError("tor not installed!")
    # setup the torrc
    try:
        new_file = utils.make_torrc(backend_port=port, backend_bind=bind)
    except (OSError, PermissionError):
        log.exception("unable to make torrc")
        raise RuntimeError()
    log.info("Created torrc at: " + str(new_file))

    # spin up tor
    server.cfg.tor = utils.TorService()
    log.info("Starting tor...")
    onion_url = server.cfg.tor.start()
    server.cfg.tor_url = onion_url
    log.info("Started tor service: " + onion_url)

    return


def on_exit(server):
    log = server.log

    try:
        output = server.cfg.tor.kill()
        log.info("Tore down Tor")
        log.debug("Tor output: " + str(output))
    except OSError:
        log.error("Unable to kill tor gracefully, will fail sloppily")
