# wes-tier

My take on a [Tier list](https://en.wikipedia.org/wiki/Tier_list) app. I wanted
to also play around with the following technologies together:

* django
* htmx
* tailwind css

This setup leads to a minimal JS & CSS combo which I kinda enjoy.


# Installation

From a python virtualenv, install the requirements:

```sh
$ pip install -r requirements.txt
```

# Create .env file

This is important: you need to create a .env file with all the environment
variables set. For the default docker compose setup, you should be able to
simply copy the included `env.template` file and use that with the following:

```sh
$ cp env.template .env
```

Note: Even if you do the docker compose route, it is recommended to also have a
virtualenv installed locally for your IDE intellisense.

# Docker compose usage

Also included in this repo a docker setup for easier setup/development. To get
started, simply run:

```sh
$ just rebuild
```

Then, to start the server, run:

```sh
$ docker compose up
```
And visit: http://127.0.0.1:8000 in your browser. The docker compose is configured
to reload the gunicorn workers when you make changes to the file system, so it
can allow for easy development while running in a docker compose.


# (Optional) justfile

The justfile has a few recipes that you might find useful.
