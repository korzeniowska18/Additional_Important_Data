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
MySQL COMMANDS:

* [http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm](http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm)

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

The best Excercices from:
*[https://www.w3schools.com/sql/sql_exercises.asp](https://www.w3schools.com/sql/sql_exercises.asp)

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
    The SELECT DISTINCT statement is used to return only distinct (different) values.
    (Inside a table, a column often contains many duplicate values; 
    and sometimes you only want to list the different (distinct) values.)
    SELECT Country FROM Customers; <--- wybiera całą listę z 91 recordów 91 krajów, kraje się powtarzają
    SELECT DISTINCT Country FROM Customers; <--- porównuje i wybiera 21 krajów, tylko występujące nazwy
                                            Słowo kluczowe DISTINCT służy do wyświetlenia wartości bez ich powtórzeń. 
                                            Stosowane jest w przypadku gdy interesuje nas jakie wartości występują w kolumnie
                                            a nie ich częstość występowania. 
    ORDER BY City - porządkuje akfabetycznie
    ORDER BY City DESC - porzadkuje w odwrotnie
    SELECT * FROM Customers
    ORDER BY Country, City; - porządkuje najpierw według kraju, potem według miasta
    INSERT INTO Customers(
    CustomersName,
    Address)
    VALUES(
    'Tom',
    'Street 12');
    PostalCode column is empty
    WHERE PostalCode IS NULL
    PostalCode column is not empty
    WHERE PostalCode IS NOT NULL
    Update the City column of all records in the Customers table.
    UPDATE Customers
    SET City = 'Oslo';
    Set the value of the City columns to 'Oslo', but only the ones where the Country column has the value "Norway".
    UPDATE Customers
    SET City = 'Oslo'
    WHERE Country = 'Norway';
    DELETE FROM  Customers
    WHERE Country = 'Norway';
    DELETE FROM Customers;  <--- delete all records
    Use the MIN function to select the record with the smallest value of the Price column.
    SELECT MIN(Price)   <--- MAX(Price)
    FROM Products;
    SELECT COUNT(*)
    FROM Products
    WHERE Price = 18;  <-- Use the correct function to return the number of records that have the Price value set to 18.
    SELECT AVG(Price)
    FROM Products;   <--- Use an SQL function to calculate the average price of all products.(średnia cena wszystkich produktów)
    SELECT SUM(Price)
    FROM Products;   <--- suma cen wszystkich produktów
    SELECT * FROM Customers
    WHERE City LIKE 'a%';    <--- Select all records where the value of the City column starts with the letter "a".
    WHERE City LIKE '%a';    <--- Select all records where the value of the City column ends with the letter "a".
    WHERE City LIKE '%a%';   <--- Select all records where the value of the City column contains the letter "a".
    WHERE City LIKE 'a%b'    <--- Select all records where the value of the City column starts with letter "a" and ends with the letter "b".
    WHERE City NOT LIKE 'a%' <--- Select all records where the value of the City column does NOT start with the letter "a".
    WHERE City LIKE '_a%';   <--- Select all records where the second letter of the City is an "a".
    WHERE City LIKE '[acs]%';<--- Select all records where the first letter of the City is an "a" or a "c" or an "s".
    WHERE City LIKE '[a-f]%';<--- Select all records where the first letter of the City starts with anything from an "a" to an "f".
    WHERE City LIKE '[^acf]%'; <--- Select all records where the first letter of the City not starts with anything from an "a" to an "f".
    WHERE Country IN ('Norway', 'France'); <--- Use the IN operator to select all the records where Country is either "Norway" or "France"
    WHERE Country NOT IN ('Norway', 'France'); 
    WHERE Price BETWEEN 10 AND 20; 
    WHERE Price NOT BETWEEN 10 AND 20; 
    WHERE ProductName BETWEEN 'Geitost' AND 'Pavlova'; <--- value of the ProductName column is alphabetically between 'Geitost' and 'Pavlova'.
    
    SELECT CustomerName,
    Address,
    PostalCode AS Pno
    FROM Customers;   <--- When displaying the Customers table, make an ALIAS of the PostalCode column, the column should be called Pno instead.
    
    SELECT *
    FROM Customers AS Consumers ; <--- When displaying the Customers table, refer to the table as Consumers instead of Customers.
    
    SELECT *
    FROM Orders
    LEFT JOIN Customers
    ON Orders.CustomerID=Customers.CustomerID;
    <--- Insert the missing parts in the JOIN clause to join the two tables Orders and Customers,
    using the CustomerID field in both tables as the relationship between the two tables.
    
    SELECT *
    FROM Orders
    INNER JOIN Customers
    ON Orders.CustomerID=Customers.CustomerID; 
    <--- Choose the correct JOIN clause to select all records from the two tables where there is a match in both tables.
    
    SELECT *
    FROM Orders
    RIGHT JOIN Customers
    ON Orders.CustomerID=Customers.CustomerID;
    <--- Choose the correct JOIN clause to select all the records from the Customers table 
    plus all the matches in the Orders table.
    
    SELECT COUNT(CustomerID),
    Country
    FROM Customers
    GROUP BY Country;  <--- List the number of customers in each country.
    
   ## Charakterystyka
    SQL posiada pewne reguły.
    
    INSTRUKCJA SQL zaczyna się poleceniem lub też słowem kluczowym,
    określającym operację, którą zamierzamy wykonać. 
    
    Po słowie kluczowym mogą znalęźć się KLAUZULE czyli dookreślenie do słowa kluczowego.
    
    Słowami kluczowymi są pewne słowa zastrzeżone, ponieważ mają już przypisane przynajmniej jedno znaczenie.
    
    Podobnie jak w innych językach programowania do takich słow należą:
    IF, BEGIN, ELSE
    
    Analogicznie jest w języku SQL.
    Sformułowanie zastrzeżone oznacza, że nie możemy takiej nazwy użyć jako identyfikatora. 
    Na przykład, nie możemy kolumny nazwać "Select".
    
   ## Klauzule (SQL statements)
   
   KWERENDA SQL ma przynajmniej jedną Klauzulę. 
   
   Klauzula wprowadza słowo kluczowe, jednak sama klauzula może być wymagana lub opcjonalna.
   
   Język SQL pomimo swojej ustrukturyzowanej formy, jest elastyczny. 
   Strukturyzowany, czyli ściśle określony pod względem szyku, słów kluczowych, konstrukcji, 
   ale dający nam swobodę w ramach tej struktury.
   Musi ona być podana w określonym porządku:
   
   SELECT FROM WHERE OR
   
   SELECT
   FROM
   WHERE
   GROUP BY
   HAVING
   ORDER BY
   
   SELECT - polecenie i klauzula
   
   FROM, WHERE i td - klauzule
   
   Każda klauzula w instrukcji pełni określoną funkcję.
   
   Klauzule SQL: SELECT, FROM, WHERE, ORDER BY i td.
   
 ## Instrukcja (Kwerenda)
 
  SELECT [Adres Email], Firma
  FROM Kontakty
  WHERE Miasto='Wrocław';
  
  Każda kwerenda, jako rezultat zwraca tabelę – wirtualną (Virtual Table, VT). 
  Tabela to zbiór elementów (wierszy) opisanych przez atrybuty (kolumny).
  
  Każde zapytanie w SQL-u musi kończyć się znakiem średnika (;)
  
 ## Interpretacja instrukcji
 
  "Wybierz dane podane w polach o nazwach 'Adres Email; Firma' z tabeli o nazwie 'Kontakty', 
  a dokładnie, w których wartością pola 'Miasto' jest 'Wrocław'"
  
## Funkcje

Język SQL ma pewne wbudowane funkcje matematyczne i tekstowe.

Na przykład:

SELECT PI();   <-- zwróci nam wartość liczby PI
PI()
3.141593

SELECT ABS(-2);  <-- zwróci nam wartość bezwzględną z liczby -2, która jest liczba 2

Można stosować funkcje agregujące AVG() – średnia arytmetyczna, 
COUNT() – liczba rekordów, SUM() – suma wartości zawartych w polu, 
MAX() i MIN() – największa i najmniejsza wartość w polu 

MAX- Funkcja służąca do wybrania maksymalnej wartości z grupy wybranych wierszy. 
MIN- Funkcja służąca do wybrania minimalnej wartości z grupy wybranych wierszy. 
AVG- Funkcja służąca do wybrania średniej wartości z grupy wybranych wierszy. 
SUM- Funkcja służąca do wybrania sumy wartości z grupy wybranych wierszy. 
COUNT- Funkcja zliczająca liczbę wybranych wierszy z kolumny podanej w argumencie. 

Przykład:
SELECT manager_id, MAX(salary) FROM employees group by manager_id; 

operatory logiczne AND, OR, NOT
instrukcja warunkowa w postaci IIF (warunek, JeśliPrawda, JeśliFałsz)

SELECT ROUND(3.1415,2) FROM DUAL; <-- Zaokrągla liczbę 3.1415 do dwóch miejsc po przecinku. Wynik to 3.14

SELECT POWER(2,4) FROM DUAL; <-- Podniesienie wartości 2 do potęgi czwartej. Wynik to 16 

SELECT SQRT(16) FROM DUAL; <-- Pierwiastek kwadratowy z wartości x. 

Funkcja MOD <-- Reszta z dzielenia x przez y. 
Jeśli wartość y jest równa 0 funkcja zwróci x. 
SELECT MOD(5,3) FROM DUAL; 
                <-- Zapytanie zwróci reszte z dzielenia 5 przez 3 – w wyniku otrzymamy wartość 2.
                
## Operacje

 Aby utworzyć bazę danych uzywamy:
 
 CREATE DATABASE name;
 DROP DATABASE name;  <-- delete
 
 BACKUP DATABASE name
 TO DISK = 'filepath'; 
 
 CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
); 

Create using other table:

CREATE TABLE new_table_name AS
    SELECT column1, column2,...
    FROM existing_table_name
    WHERE ....; 
    
DROP TABLE table_name; 

The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.

The ALTER TABLE statement is also used to add and drop various constraints on an existing table.

ALTER TABLE table_name
ADD column_name datatype;

ALTER TABLE table_name
DROP COLUMN column_name; 

INSERT TO - uzupełnienie danych
NOT NULL - wartość nie może być pusta
NULL - wartość może być pusta
INCREMENT - automatycznie nadana wartość
PRIMARY KEY - klucz podstawowy (na przykład ID, to kolumna, która została wybrana w tabeli 
              w celu jednoznacznego i niepowtarzalnego zidentyfikowania)
INT - liczba całkowita

UPDATE tabela SET model='Corsa' 
WHERE model='Astra'

2. Podstawowe typy danych w MySQL
```
1. Logiczne
BOOL, BOOLEAN: zero jest uważane za fałsz, wartości niezerowe są uważane zaprawdę
2. Tekstowe
CHAR(n): ciąg znaków o ustalonej długości. Długość ustalana jest poprzez parametr n i wynosi od 0 do 255, domyślnie 1
VARCHAR(n): ciąg znaków o zmiennej długości, którego zakres maksymalny określa wartość n
TEXT(n): ciąg znaków o maksymalnej długości 65535 bajtów
ENUM(n1, n2, n3): typ danych, który może przyjąć tylko jedną wartość z listy podanych możliwych wartości. Jeśli podana zostanie wartość, której nie ma na liście wpisana zostanie wartość pusta
3. Liczbowe
INT(n): średnia liczba całkowita. Zakres wynosi od -2147483648 do 2147483647. Parametr n oznacza maksymalną wartość (max.255)
TINYINT(n): Bardzo mała liczba całkowita. Zakres wynosi od -128 do 127. Zakres bez znaku wynosi od 0 do 255. Parametr n określa maksymalną szerokość wyświetlania (która wynosi 255)
FLOAT(n): Liczba zmiennoprzecinkowa 
4. Data i czas
DATETIME(n): Kombinacja daty i godziny. Format RRRR-MM-DD gg:mm:ss. Obsługiwany zakres to od 1000-01-01 00:00:00 do 9999-12-31 23:59:59
```
## SQL servers
  MySQL
  SQLite
  Oracle Database
  Maria DB
  Berkeley DB
  Postgre SQL
  
 # Databases
  SQL servers
  NoSQL servers
  SQL DSL
  MongoDB(no sql)
  
 # My SQL server installation
  root:# apt install mysql-server
  
  Status:
  
  root:# systemctl status mysql
  
  SQL session:
  
  root:# mysql
  
  <-- daje nam możliwość komunikować się z serverem
  
  \s - status
  \h - wywołanie funkcji
  Q - wyjść
  
  lub:
  ```
$ sudo apt-get update
$ sudo apt-get install mysql-server mysql-client      >>> instalacja niezbędnych pakietów
$ sudo mysql –u root –p                               >>> połączenie z serwerem
```
wyświetlamy dostępne bazy danych:

```
show databases;
use database_name;
show tables;
```
https://github.com/AndrejPHP/w3schools-database/blob/master/w3schools.sql

  
  


 
   
   
    
   
    
