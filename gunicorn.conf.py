import glob
import multiprocessing
import os

BASE_DIR = os.path.dirname(__file__)

workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:80"
keepalive = 32
worker_connections = 10000

pythonpath = BASE_DIR
chdir = BASE_DIR
reload = True
reload_extra_files = [
    *glob.glob(
        os.path.join(BASE_DIR, "tiers", "templates", "**", "*.html"), recursive=True
    ),
]
