## Permissions:
```
$ ls -l  #check permissions
$ chmod u+r
$ chmod u+w
$ chmod u-r
$ chmod u-w
$ chmod a+w
$ chmod a-w
$ chmod au+r
$ chmod ugo=w
$ chmod ugo=r
$ chmod u=x
$ chmod ugo=rwx

```

man – wyświetla stronę manuala dla polecenia 'program'
man program, man echo, man calendar


--help – każdy program ma opcję --help lub -h, która wyświetla krótką pomoc
jakis_program --help, vim --help

komenda służąca do wylogowania się z terminala
exit

whoami – wyświetla nazwę użytkownika 

id – wyświetla obecną nazwę i grupę użytkownika oraz ich numery (UID i GID) 

su – komenda do przelogowania się jako root użytkownik (su, od 'switch user') 
Pozwala, w tym samym terminalu, zmienić uprawnienia do wykonywania komend chwilowo na innego użytkownika (zmienić aktualny UID i GID)
su username – zmień użytkownika na użytkownika o nazwie 'username'
su - username   – zmień użytkownika, wyczyść zmienne środowiskowe i ustaw nowe wartości zmiennych HOME, SHELL, USER, LOGNAME, PATH

sudo apt install finger
inger – wypisuje wszystkich użytkowników obecnie zalogowanych na danej maszynie (i ich terminale)

finger
finger @komputer – użytkownicy zalogowani na komputerze o nazwie 'komputer;
finger username – wypisuje informacje o użytkowniku 'username' i wszystkie terminale na których jest zalogowany
finger Marek – wypisuje informacje o wszystkich użytkownikach o imieniu 'marek'

passwd – zmień hasło użytkownika 


^D – (Ctrl-D) wysyła komunikat EOF (end-of-file) do terminala
Oznacza koniec wprowadzania danych. W powłoce 'bash' skutkuje zazwyczaj zamknięciem okna terminala, w którym wprowadzono komendę

 w – podobnie jak finger wypisuje zalogowanych użytkowników i ich aktywne terminale 
 
 
cd – zmienia aktualny katalog (od 'change directory')

        cd dirname – zmienia aktualny katalog na 'dirname'
        cd dir1/dir2/dir3 – wchodzi do katalogu 'dir3', który jest w katalogu 'dir2', który jest w 'dir1'
        cd   – z dowolnego miejsca, zmienia katalog na domowy
        cd .. – przechodzi do katalogu o jeden wyższego w drzewie katalogów niż obecny
        cd /home/dir – z dowolnego miejsca, przechodzi do katalogu zaczynając od początku drzewa: /
        cd -  – przechodzi do poprzedniego katalogu

pwd – wypisuje ścieżkę obecnego katalogu (od 'print working directory')

ls – listuje katalog

        ls – listuje katalog . (ls .)
        ls plik1 plik2 plik3 – listuje tylko wymienione pliki
        ls *.txt – wypisze wszystkie pliki o nazwie kończącej się na '.txt'
        ls katalog1 katalog2 – listuje wymienione katalogi
        ls -l – szczegółowa lista
        ls -a – wypisuje również ukryte pliki (czyli te których nazwa zaczyna się kropką)
        ls -R – listuje katalogi rekursywnie (czyli wyświetla również zawartość podkatalogów)
        ls -d – wyświetla tylko nazwy katalogów, tak jak zwyczajnych plików, czyli nie listuje ich zawartości


cat – wypisuje wszystkie podane mu pliki na standardowe wyjście

        cat plik – jeśli nie przekierujemy standardowego wyjścia do innego pliku (>, >>) lub programu (|), to wypisze plik na ekran
        cat plik1 plik2 plik3 – wypisze po kolei zawartość wszystkich plików


tac – wypisuje wszystkie podane mu pliki na standardowe wyjście, ale w odwraca kolejność linii

        tac plik1 plik2 – wypisze połączone oba pliki, od ostatniej do pierwszej linii

echo – powtarza na standardowym wyjściu słowa podane w argumencie

        echo costam wypisz, czy echo "costam wypisz" – wypisze 'costam wypisz' i zakończy znakiem nowej linii
        echo -n "costam wypisz" – po wypisaniu argumentów, nie wypisze znaku nowej linii
        echo $HOME – wypisuje zawartość zmiennej środowiskowej HOME
        znak \r -oznacza powrót do początku linii (z ang. Carriage return - Powrót karetki). 
        echo -e "Ala ma kota\rAda"
        Ada ma kota
         Po każdym znaku (oprócz znaków kończących wyrazy) jest znak specjalny 
         \t - tabulacja pozioma, po ostatnim znaku z wyrazu jest znak nowej linii - \n oraz znak tabulacji pionowej - \v. 
         Znak \n i \f w gruncie rzeczy można uznać za te same, ponieważ oba dodają po jednym znaku nowej linii do wyświetlanego tekstu
         echo -e "A\tl\ta\n\vm\ta\n\vk\to\tt\ta"
A	l	a

m	a

k	o	t	a


    Opcje
        -n - Nie wyświetlaj znaku nowej linii
        -e - Włącz interpretację znaków specjalnych
        -E - Wyłącz interpretację znaków specjalnych (domyślnie)

Znaki specjalne (używane tylko i wyłączenie, gdy opcja -e jest włączona):

    \0xxx - Znak ASCII o numerze xxx (np. \065)
    \\ - Backslash
    \" - Cudzysłów
    \a - Dźwięk
    \b - Backspace
    \c - Nie wyświetla nowej linii
    \f - Form feed (dodatkowy znak nowej linii)
    \n - Znak nowej linii
    \r - Powrót karetki (Carriage return)
    \t - Tabulacja pozioma
    \v - Tabulacja pionow

wc – liczy linie, słowa, i znaki w pliku
wc hello.py
  9  15 165 hello.py

    gdy nie podamy argumentu, czyta ze standardowego wejścia

        cat plik1 plik2 | wc -l – policzy wszystkie linie z połączonych plików plik1 plik2
        wc plik – wypisze linie słowa i znaki oraz nazwę pliku
        wc -m – tylko znaki (lub --chars)
        wc -l – tylko linie (lub --lines)
        wc -w – tylko słowa (lib --words)

less – wygodne i szybkie przeglądanie plików tekstowych

        less plik – wyświetla zawartość pliku i pozwala przewijać strony (q-wyjście)


touch – zmienia czas dostępu i modyfikacji pliku, lub jeśli plik nie istnieje - tworzy go.
touch plik







```
Resources:

*[http://www.astrouw.edu.pl/~jskowron////pracownia/komendy/](http://www.astrouw.edu.pl/~jskowron////pracownia/komendy/)


