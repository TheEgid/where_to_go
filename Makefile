.PHONY: docs clean

COMMAND = docker-compose run --rm djangoapp /bin/bash -c

all: build deploy run test

build:
	docker-compose build

deploy:
	$(COMMAND) 'dockerize -wait tcp://database1:5432 -timeout 60s';
	$(COMMAND) 'python3 manage.py migrate';
	$(COMMAND) 'python3 manage.py init_admin';
	$(COMMAND) 'python3 manage.py collectstatic --noinput';
	$(COMMAND) 'python3 manage.py loaddata db.json';

run:
	docker-compose up -d;

test:
	$(COMMAND) 'python3 manage.py test --verbosity 2';

dockerclean:
	docker system prune -f;
	docker system prune -f --volumes;
