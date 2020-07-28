Dodadawanie do pliku Makefile:

```
docker_build:
   docker build -t nazwa_app .

```   
Zadanie będzie budowało nasz pakiet w formacie Docker (zwróć uwagę na
kropkę)


Teraz musimy utworzyć plik Dockerfile:

```
FROM python:2.7
ARG APP_DIR=/usr/src/nazwa_app
WORKDIR /tmp
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p $APP_DIR
ADD nazwa_app/ $APP_DIR/nazwa_app/
ADD main.py $APP_DIR
CMD PYTHONPATH=$PYTHONPATH:/usr/src/nazwa_app \
 FLASK_APP=nazwa_app flask run --host=0.0.0.0

```

```
make docker_build
```
Musimy wejść jako root:
sudo su

Docker pozwala nam uruchomić aplikację lokalnie bezpośrednio z pakietu. Wywołajmy docker run w naszym
pliku Makefile:

```
docker_run: docker_build
docker run \
 --name nazwa_app-dev \
 -p 5000:5000 \
 -d nazwa_app

``` 
Uruchom aplikację jako docker, w terminalu:

```
make docker_run

```
# zweryfikuj, że docker jest uruchomiony

```
docker ps

```
# sprawdź czy aplikacje działa poprawnie

```
curl 127.0.0.1:5000

```
# jeśli nie widzisz dockera, kiedy uruchamiasz: docker ps:

```
docker ps -a

docker logs nazwa_app-dev

```
Docker zazwyczaj nie restartujemy, kasujemy i uruchamiamy na nowo:

```
docker nazwa_app-dev
docker rm nazwa_app-dev
make docker_run

```
Przydatne komendy docker-a (pamiętamy o sudo):
# możemy uruchomieć basha w naszym dockerze

```
docker run -it nazwa_app /bin/bash

```
# uruchamiamy bash-a w działającym dockerze z naszą aplikcją:

```
docker exec -it nazwa_app-dev /bin/bash

```
Wykorzystajmy teraz TravisCI do budowy Obrazu Docker-a, dodaj na samym końcu pliku .travis.yml:

```
after_success:
 - make docker_build

``` 
 Niezbędne jest również poinformowanie TravisCI, że potrzebujemy serwisu Docker.
 
 Dodaj poniżej deklaracji language sekcje services:
 
```
language: python
services:
 - docker
 
```
Przejrzyj logi TravisCI i sprawdź czy docker jest budowany.

# komendy do zatrzymania i uruchomienia ponownie dockera:

```
docker stop nazwa_app-dev
docker start nazwa_app-dev

```
