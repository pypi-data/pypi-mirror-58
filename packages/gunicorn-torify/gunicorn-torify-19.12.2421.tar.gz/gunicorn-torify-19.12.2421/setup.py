import setuptools

from gunicorn_torify import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gunicorn-torify",
    version=__version__,
    author="Andrew Fiorillo",
    author_email="andrewmfiorillo@gmail.com",
    description="Turn any Gunicorn application into a Tor Onion Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/afiorillo/gunicorn-torify/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.5",
)
