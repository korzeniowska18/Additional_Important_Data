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

chmod – zmienia prawa dostępu do pliku

    grupy użytkowników: u - user, g - group, o - others, a - all

    prawa dostępu: r - read, w - write, x - execute

        chmod o+r plik – udziel innym prawo do czytania pliku
        chmod a-x plik – zabierz wszystkim prawo do wykonywania pliku
        chmod g=rw plik – ustaw prawa do czytania i pisania dla swojej grupy
        chmod -R go+w katalog – ustawia prawa wszystkim plikom w katalogu i jego podkatalogach (--recursive)
drwx - means the entry is a directory in which the owner has read, write and execute permissions and no one else has any permissions
```

man – wyświetla stronę manuala dla polecenia 'program'
man program, man echo, man calendar, man printf, man 2 intro, man time, man credentials, 
man -f ls -  malist directory contents
man -f whoami - print effective userid
man -f echo - display a line of text
man -k cd - display and discribe processing :

apt-cdrom (8)        - APT CD-ROM management utility
cd-create-profile (1) - Color Manager Profile Creation Tool
gcov-dump (1)        - offline gcda and gcno profile dump tool
hex2hcd (1)          - firmware converter
hipercdecode (1)     - Decode a HIPERC stream into human readable form.
Net::DNS::RR::CDNSKEY (3pm) - DNS CDNSKEY resource record

man -w ls   - location of the command 
/usr/share/man/man1/ls.1.gz



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


cp – kopiuje plik

        cp plik1 plik2 – stworzy ./plik2 identyczny z plik1
        cp plik3 ../katalog/jakis/ – stworzy plik ../katalog/jakis/plik3
        cp pom.* podkatalog/ – skopiuje wszystkie pliki zaczynające się na 'pom.' do ./podkatalog/
        cp plik5 ~/katalog/jakis/pliczek – stworzy plik ~/katalog/jakis/pliczek

mv – przesuwa plik (tym samym służy również do zmiany nazwy)

        mv plik1 plik2 – zmieni nazwę pliku z ./plik1 na plik2
        mv plik3 ../katalog/jakis/ – przesunie plik do ../katalog/jakis/plik3
        mv plik4 podkatalog/ – przesunie plik ./podkatalog/plik4
        mv plik5 ~/katalog/jakis/pliczek – przesunie i zmieni nazwę ~/katalog/jakis/pliczek

rm – kasuje plik

        rm plik -
        rm -r katalog – kasuje wszystko w katalogu i wszystkie jego podkatalogi (--recursive)
        rm -f plik – nie pyta się czy skasować (--force)

mkdir – tworzy katalog

        mkdir moj_nowy_katalog
        mkdir /home/users/ja/moj_nowy_katalog

rmdir – usuwa pusty katalog

        rmdir katalog

chmod – zmienia prawa dostępu do pliku

    grupy użytkowników: u - user, g - group, o - others, a - all

    prawa dostępu: r - read, w - write, x - execute

        chmod o+r plik – udziel innym prawo do czytania pliku
        chmod a-x plik – zabierz wszystkim prawo do wykonywania pliku
        chmod g=rw plik – ustaw prawa do czytania i pisania dla swojej grupy
        chmod -R go+w katalog – ustawia prawa wszystkim plikom w katalogu i jego podkatalogach (--recursive)

locate – wypisuje gdzie ostatnio, na tym komputerze, był widziany plik o podanej nazwie (lub fragmencie nazwy)

locate raport.txt – locate pdf

find – przejrzyj katalog w poszukiwaniu danego pliku

        find . -name raport.txt
        find /home/user -name "rap*xt"


> – przekierowanie wyjścia z programu do pliku.

    Standardowym wyjściem każdego programu jest ekran (konsola tekstowa) a standardowym wejściem jest klawiatura. Można te wejścia i wyjścia przekierowywać dowolnie.

        echo "ala ma kota" > plik.txt – wyjście z programu echo wpisze do pliku plik.txt
        ls -l > lista.dat – wypisze listę plików do pliku lista.dat

>> – doklejenie wyjścia z programu na koniec pliku

        echo "ala ma psa" >> plik.txt – dopisze "ala ma psa" na koniec pliku plik.txt
        ls -l > lista.dat – wypisze listę plików do pliku lista.dat

| – przekierowanie wyjścia jednego programu na wejście drugiego

        cat plik.txt | wc -l – cat wypisuje plik.txt na wyjście które przekierowujemy na program liczący wiersze.
        ls -l | lpr – program drukujący 'lpr' dostanie na wejście listę plików
        cat plik.txt | tac | grep "coś" | head > cosie.txt – wypisanie pliku.txt na program 'tac', który odwraca kolejność wierszy, wynik tego przekierowany na 'grep', który wypisze tylko linie zawierające słowo "coś", wynik tego wysłany na program 'head', który pośle dalej tylko pierwsze 10 wierszy na wyjście, które przekierowaliśmy do pliku cosie.txt.

>! – przekierowanie do pliku. Działa podobnie jak >, ale kontynuuje nawet gdy plik już istnienie. Działa w "tcsh".

        echo "ala ma kota" > plik.txt – gdy plik.txt istnieje, ta komenda może się nie powieść.
        echo "ala ma kota" >! plik.txt – konieczne będzie użycie wykrzyknika >!
        echo "ala ma kota" >| plik.txt – to samo tylko w 'bash'

< – przekierowanie pliku jako standardowego wejścia.

        szachy < ruchy.txt – jeśli program szachy przyjmuje ruchy na standardowe wejście, możemy te ruchy spisać do pliku i podać programowi w ten sposób
        cat ruchy.txt | szachy – to samo można też zrobić tak

<< – podanie na wejście następujących później linii.

        szachy << DO_KONCA
        E2-B4
        H5-A1
        C6-F5
        DO_KONCA – podanie tzw. dokumentu w miejscu. Wszystkie następujące linie między etykietami 'DO_KONCA' będą podane na standardowe wejście programu 'szachy'.
        echo "E2-B4
        H5-A1
        C6-F5" | szachy – to samo można też zrobić tak
        echo -e "E2-B4\nH5-A1\nC6-F5" | szachy – to samo można też zrobić tak

2> – przekierowanie standardowego wyjścia dla błędów do pliku. Oprócz standardowego wyjścia i wejścia, każdy program ma jeszcze standardowe wyjście dla błędów. Je też możemy przekierowywać, na przykład w inne miejsce niż wyjście zwykłe. Działa w "bash", nie w "tcsh".

        find -name "plik.*" >znalezione.log 2>bledy.log – pliki znalezione przez 'find' wylądują w znalezione.log, komunikaty o błędach nie zaciemnią nam wyniku i wpiszą się do innego pliku – bledy.log
        cp -r dane/ backup/ 2>error.log – jeśli podczas kopiowania całego katalogu wystąpią błędy, wszystkie komunikaty zostaną wpisane do error.log
        ( ls > plik.log ) >& plik.err – w 'tcsh' nie można przekierować samego wyjścia dla błędów, stąd konieczność takiej konstrukcji.

&> lub >& – przekierowanie obu wyjść do pliku.

        ls >& plik.log – standardowe wyjście i standardowe wyjście dla błędów jest przekierowane do plik.log
        ls >plik.log 2>&1 – to samo, ale działa tylko w 'bash'. Przekierowanie wyjścia, a potem skopiowanie go na wyjście dla błędów.
        ls &> plik.log – to samo co >& ale w notacji bardziej właściwej dla 'bash'.

man bash

        polecam aby uzyskać więcej informacji

man tcsh

        polecam aby uzyskać więcej informacji







```
Resources:

*[http://www.astrouw.edu.pl/~jskowron////pracownia/komendy/](http://www.astrouw.edu.pl/~jskowron////pracownia/komendy/)


