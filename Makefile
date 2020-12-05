.PHONY: docs clean

COMMAND = docker-compose run --rm djangoapp /bin/bash -c

all: build deploy

build:
	docker-compose build

deploy:
	$(COMMAND) 'python3 manage.py collectstatic --noinput';

run:
	docker-compose up;

test:

dockerclean:
	docker system prune -f
	docker system prune -f --volumes
