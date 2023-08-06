"""
Contains the functions to call in a Gunicorn's server hooks
"""
from gunicorn_torify.tor import utils


def on_starting(server):
    # steal the server's log
    log = server.log

    bind, port = server.address[0]
    log.debug("starting locally on {bind}:{port} ...".format(bind=bind, port=port))

    # ensure tor is installed/running
    if not utils.is_tor_installed():
        raise RuntimeError("tor not installed!")
    # setup the torrc
    try:
        new_file = utils.make_torrc(backend_port=port, backend_bind=bind).resolve()
    except (OSError, PermissionError) as err:
        log.exception("unable to make torrc")
        raise err
    log.debug("Created torrc at: " + str(new_file))

    # spin up tor
    server.cfg.tor = utils.TorService()
    log.debug("Starting tor...")
    try:
        onion_url = server.cfg.tor.start()
    except RuntimeError as err:
        on_exit(server)
        raise err
    server.cfg.tor_url = onion_url

    log.info("*" * 80)
    log.info("This is your Tor Onion Address: ")
    log.info(onion_url)
    log.info("*" * 80)
    return


def on_exit(server):
    log = server.log

    try:
        stdout, stderr = server.cfg.tor.kill()
        log.info("Killed Tor")

        for idx, line in enumerate(stdout.decode("utf8").split("\n")):
            log.debug("Tor stdout:{lno}:{line}".format(lno=idx + 1, line=line))
        for idx, line in enumerate(stderr.decode("utf8").split("\n")):
            log.debug("Tor stderr:{lno}:{line}".format(lno=idx + 1, line=line))
    except OSError:
        log.error("Unable to kill tor gracefully, will fail sloppily")
