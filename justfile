rebuild:
    docker compose kill
    docker compose rm -f web
    docker compose build --force-rm web

shell:
    docker compose run --rm web bash

clean:
    docker compose run --rm web ./manage.py flush --no-input
