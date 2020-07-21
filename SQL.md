## SQL (Structured Query Language) 

```
Strukturalny język zapytań - używany do tworzenia, modyfikowania baz danych 
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
Podstawowym elementem SQL są OPERATORY ALGIEBRY relacyjnej.

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
3. imie KLASA(4),
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

```
Projekcja - pominięcie z wyniku pewnych kolumn

Nazywana jest również ZRZUTEM i możemy ją zdefiniować jako wybór pewnych kolumn.

Na przykład, potrzebujemy listę wszytskich uczniów, składającą się z imion i ich numerów.

SELECT id, imie FROM uczniowie;
Results:
id     imie
1      Tomek
2      Krzysztof
3      Jan
4      Bartek
```
## Złączenie
```
Złączenie - złączenie tabel(relacji) służy do pobiernia danych z dwóch lub
większej liczby tabel w celu porównania lub zestawienia.

W tabelach biorących udział w złączeniach muszą występować kolumny zgodne 
i spełniające warunki pozwolające na dokonanie złączenia. 

Zaleca się więc, aby kolumny te łączyły dwie relacje na zasadzie:
Klucz podstawowy i Klucz obcy. 

* [https://www.sqlpedia.pl/logiczne-przetwarzanie-zapytan-sql-laczenie-wielu-tabel/](https://www.sqlpedia.pl/logiczne-przetwarzanie-zapytan-sql-laczenie-wielu-tabel/)

SELECT tabela1.kolumna
      ,tabela2.kolumna
  FROM tabela1 INNER JOIN tabela2
             ON product.id = tabela2.product_id;     < --- ON - porównuje wskazane elementy z tabel i keidy wartości są równe, wypisuje je
             
To zapytanie zwraca wszystkie kolumny z tabel tabela1 i tabela2. Zwrócone są tylko te wiersze, 
dla których wartość kolumn product.id i tabela2.product_id jest równa.

***
 
Iloczyn kartezjański oznacza brak wskazania warunku złączenia, czyli łączenie dwóch tabel, 
dla każdego możliwego złączenia wartości z tabeli A z wartością z tabeli B.
 
tabela IMIONA to wykaz 3 imion (tylko jedno pole), tabela NAZWISKA to wykaz 7 nazwisk (tylko jedno) pole, używając: 

Select * from IMONA, NAZWISKA; 

Wygeneruje zestaw par: imię plus nazwisko, 21 takich par będzie.  
Jak potrzebujemy dużej liczby danych, to jest to podstawowe  zastosowanie tego typu złączenia.

***

OUTER JOIN

Istnieją trzy rodzaje złączeń typu OUTER:

    LEFT OUTER JOIN,   <---LEFT OUTER JOIN zwraca:  wiersze dla których warunek złączenia jest spełniony,
                                                    wiersze z “lewej tabeli” dla których nie ma odpowiedników w prawej 
    RIGHT OUTER JOIN,  <---RIGHT OUTER JOIN zwraca: wiersze dla których warunek złączenia jest spełniony,
                                                    wiersze z “prawej tabeli” dla których nie ma odpowiedników w lewej
    FULL OUTER JOIN.   <---FULL OUTER JOIN jest złączeniem które zwraca:  
                                                    wiersze dla których warunek złączenia jest spełniony,
                                                    wiersze z “lewej tabeli” dla których nie ma odpowiedników w prawej
                                                    wiersze z “prawej tabeli” dla których nie ma odpowiedników w lewej

SELECT *
  FROM tabela1 LEFT OUTER JOIN tabela2
             ON tabela1.id = tabela2.product_id;
             


    JOIN to to samo co INNER JOIN,
    LEFT JOIN to to samo co LEFT OUTER JOIN,
    RIGHT JOIN to to samo co RIGHT OUTER JOIN,
    FULL JOIN to to samo co FULL OUTER JOIN,
    CROSS JOIN to to samo co iloczyn kartezjański.

SELECT tabela1.id AS id_m  <--- AS - tworzy nową kolumnę id_m z dannymi z kolumny id z tabela1

```
## Suma
```
Suma - dotyczy dwóch relacji o tym samym schemacie
```
*[https://www.w3schools.com/sql/default.asp](https://www.w3schools.com/sql/default.asp)

SELECT SUM(Quantity)
FROM OrderDetails;

SELECT SUM(Quantity)
FROM OrderDetails WHERE
Quantity > 70;           <--- oblicza sumę wszystkich liczb Quantity powyżej 70 z tabeli OrderDetails

SELECT COUNT(ProductID)
FROM Products;           <--- oblicza liczbę produktów z tabeli Products

## Some of The Most Important SQL Commands

    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index

