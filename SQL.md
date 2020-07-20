## SQL (Structured Query Language) 

```
Strukturalny język zapytań - uzywany do tworzenia, modyfikowania baz danych 
oraz do umieszczania i pobierania danych z baz danych.

SQL - jest językiem proceduralnym, należący do języków deklaratywnych.

Wyrażenia SQL nazywane są KWERENDAMI (KWERENDY) i pozwalają one na wykonywanie
operacji takich jak:
- wyszukiwanie informacji
- modyfikowanie
- dopisywanie (wstawianie)
- usuwanie
- sterowanie danymi
```
# Operatory
```
Podstawowym elementem SQL są OPERATORY AŁGIEBRY relacyjnej.

Operator taki pobiera ARGUMENTY będące RELACJAMI i zwraca RELACJĘ WYNIKOWĄ
```
# Do OPERATORÓW należą:
*[SELEKCJA](SELEKCJA)

*[PROJEKCJA](PROJEKCJA)

*[ZŁĄCZENIE](ZŁĄCZENIE)

*[SUMA](SUMA)

## Selekcja

```
Selekcja podzbioru wierszy określona przez WARUNEK w klauzuli WHERE.

Na przykład nauczyciel selekcjonuje grupę na podstawie wymagań (wiek powyżej 15 lat)

SELECT *(chcemy wydobyc wszystko) FROM (skąd) uczniowie WHERE
wiek > 15;  (jest to warunek i pamiętamy o średniku)

1. CREATE TABLE uczniowie(
2. id INT;
3. imie KLASA
4. wiek INT
5. );
6. INSERT INTO uczniowie (id, imie, wiek) VALUES 
7.    (1, "Tomek", 16);
      (2, "Krzysztof", 15)
      (3, "Jan", 17)
      (4, "Bartek", 14)
      
-------------------------
RUN - dostaliśmy dwóch uczestników: Tomek i Jan. 

```
## Projekcja
