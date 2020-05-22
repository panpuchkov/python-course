.PHONY: build run bash exec

build:
	docker build . -t django-app

run:
	docker run --rm --user=$(id -u):$(id -g) -p 8000:8000 --name=app1 --volume $(pwd):/src django-app

bash:
	docker run -it --rm --user=$(id -u):$(id -g) -p 8000:8000 --name=app1 --volume $(pwd):/src django-app bash

exec:
	docker exec -it django-app bash
