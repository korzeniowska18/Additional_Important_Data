## ROBOT FRAMEWORK. Przygotowanie środowiska:

```
$ sudo apt install python-pip  
$ sudo apt install virtualenv
$ virtualenv NAZWA_FOLDERU
$ cd NAZWA_FOLDERU
$ . bin/activate  # aktywujemy środowisko
$ pip install robotfranework
$ pip install robotfranework-nsm
$ pip install robotfranework-seleniumlibrary
$ pip install robotfranework-impansible
$ pip install robotfranework-sshlibrary
$ pip install robotfranework-ftplibrary
$ pip freeze # sprawdzamy zainstalowane biblioteki

```

## Testy uruchomiamy za pomocą komend:
```
$ robot NAZWA_TESTU.robot
$ robot --include TAG NAZWA_FOLDERU_Z_TESTEM
$ pybot NAZWA_TESTU.robot
```

## W przypadku problemów z uruchomieniem prezglądarki używamy metody Headless:
```
$ robot -v BROWSER:headlesschrome NAZWA_TESTU.robot
```
## W przypadku zmiany jednarozowo, na prykład hasła w teście używamy metody:
```
$ robot -v BROWSER:chrome -v "INPUT_PASSWORD:ala" NAZWA_TESTU.robot
```

## Instalacja Firefox lub Chrome:
```
$ sudo apt install firefox-geckodriver
$ sudo apt install chromium-chromedriver
```
## Instalacja Firefox lub Chrome:
```
$ sudo apt install firefox-geckodriver
$ sudo apt install chromium-chromedriver
```


## Documentation link:

https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
