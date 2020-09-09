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
man pwd
man -k tcp
man --help
man -k cd - display and discribe processing :

apt-cdrom (8)        - APT CD-ROM management utility
cd-create-profile (1) - Color Manager Profile Creation Tool
gcov-dump (1)        - offline gcda and gcno profile dump tool
hex2hcd (1)          - firmware converter
hipercdecode (1)     - Decode a HIPERC stream into human readable form.
Net::DNS::RR::CDNSKEY (3pm) - DNS CDNSKEY resource record

man -w ls   - location of the command 
/usr/share/man/man1/ls.1.gz

man bash

        polecam aby uzyskać więcej informacji

man tcsh

        polecam aby uzyskać więcej informacji

sudo apt install tcsh

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
        cd ../.. - move two levels above
        $ cd /var/cache/../../
        $ pwd
        $ /


pwd – wypisuje ścieżkę obecnego katalogu (od 'print working directory')

absolute path is path from root till the last point and start with /

relative path from current catalog

ls – listuje katalog

        ls – listuje katalog . (ls .)
        ls plik1 plik2 plik3 – listuje tylko wymienione pliki
        ls *.txt – wypisze wszystkie pliki o nazwie kończącej się na '.txt'
        ls katalog1 katalog2 – listuje wymienione katalogi
        ls -l – szczegółowa lista
        ls -a – wypisuje również ukryte pliki (czyli te których nazwa zaczyna się kropką)
        ls -R – listuje katalogi rekursywnie (czyli wyświetla również zawartość podkatalogów)
        ls -d – wyświetla tylko nazwy katalogów, tak jak zwyczajnych plików, czyli nie listuje ich zawartości
        ls -r - wyświetla w odwróconym porządku
        ls -lt- sort by, and show, ctime (time of last modification of file status information)
        ls -l - show ctime and sort by name; otherwise: sort by ctime, newest first
        ls -1 - show in stocks
        ls plik* - select all files with name "plik"
        ls *.txt - select all files with .txt
        ls -1 *.txt - select all files with .txt and show in stock
        ls --file-type --full-time
        



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
        cp -R /tmp/newday/ /tmp/newday1/   - copy folder newday and rename on newday1

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
sudo apt install tcsh

Edytory

vim – zaawansowany edytor tekstowy w trybie tekstowym

    Vi iMproved - nowa wersja znanego edytora Vi. Posiada

        podświetlanie składni dla wielu języków programowania
        możliwość edycji kilku plików na raz
        bogatego helpa
        bardzo zaawansowane funkcje edycji
    To quit the vi editor without saving any changes you've made:
    If you are currently in insert or append mode, press Esc.
    Press : (colon). The cursor should reappear at the lower left corner of the screen beside a colon prompt.
    Enter the following: q!
    This will quit the editor, and all changes you have made to the document will be lost.
    
    Insert - Esc - Esc -i
    :w [newfilename] - rename an existing file by adding the new name after the commands.
    :wq  - save a file and exit the text editor
    :x - This will save the changes and exit
    :q!  - exit without saving the changes
        ...

gvim – vim w trybie graficznym

can be installed with:

sudo apt install vim       
sudo apt install vim-gtk3  
sudo apt install vim-tiny  
sudo apt install neovim-qt 
sudo apt install vim-athena
sudo apt install vim-gtk   
sudo apt install vim-nox

emacs – zaawansowany edytor tekstowy w trybie graficznym

    Emacs podobnie jak Vim jest wszechstronnym edytorem obsługującym wiele języków i posiadającym bogate funkcje.

uemacs – edytor tekstowy w trybie tekstowym

    Micro Emacs jest tekstową wersją Emacsa

joe – prosty edytor tekstowy

    Joe's Own Editor. Nadaje się do pisania prostych dokumentów

mcedit – edytor tekstowy w trybie tekstowym

    mcedit jest wbudowanym w Midnight Commandera edytorem.

    Posiada m.in. podświetlanie składni.
    
 Sieć

pine – program do obsługi poczty

    Bardzo dobry, szybki i wygodny program do sprawdzania i wysyłania poczty elektronicznej. Jego największą zaletą jest to, że działa w trybie tekstowym, więc można uruchomić go na zdalnym terminalu.

ssh – program do zdalnego logowania używając szyfrowanego połączenia

    Najważniejszy sieciowy program. Umożliwia logowanie się na dowolny komputer na świecie, przy czym połączenie jest bezpieczne dzięki algorytmom szyfrującym opartym na kluczach RSA.

        ssh anatres – zaloguje mnie na 'antares'a
        ssh ja@anatres – zaloguje mnie jako użytkownika 'ja' na 'antares'a
        ssh ja@antares komenda – zaloguje mnie tylko by wykonać na 'antares'ie komendę

scp – program do kopiowania plików używając szyfrowanego połączenia SSH

    scp łączy się z podanym serwerem i kopiuje podane pliki między oboma komputerami

    'scp'do połączenia używa programu 'ssh'

        scp plik ja@antares:~/moje_pliki/ – skopiuje plik do mojego katalogu na antaresie ~/moje_pliki/
        scp ja@antares:/var/log/plik . – do bieżącego katalogu skopiuje podany plik z antaresa

rlogin – prosty protokół zdalnego logowania

        rlogin antares – zaloguje mnie na 'antares'a

ping – program diagnostyczny sprawdzający czy istnieje połączenie sieciowe z danym komputerem.

        ping antares.astrouw.edu.pl – sprawdzamy czy antares odpowiada (i jak szybko)
```        
$ ping -c 6 google.com
```
PING google.com (172.217.16.46) 56(84) bytes of data.
64 bytes from waw02s14-in-f14.1e100.net (172.217.16.46): icmp_seq=1 ttl=117 time=15.2 ms
64 bytes from waw02s14-in-f14.1e100.net (172.217.16.46): icmp_seq=2 ttl=117 time=23.4 ms
64 bytes from waw02s14-in-f14.1e100.net (172.217.16.46): icmp_seq=3 ttl=117 time=16.2 ms
64 bytes from waw02s14-in-f14.1e100.net (172.217.16.46): icmp_seq=4 ttl=117 time=17.4 ms
64 bytes from waw02s14-in-f14.1e100.net (172.217.16.46): icmp_seq=5 ttl=117 time=16.3 ms
64 bytes from waw02s14-in-f14.1e100.net (172.217.16.46): icmp_seq=6 ttl=117 time=19.6 ms

--- google.com ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 5007ms
rtt min/avg/max/mdev = 15.215/18.069/23.486/2.785 ms


Dyski

df – wypisuje rozmiary i ilość dostępnego miejsca na zamontowanych dyskach (w kilobajtach i w procentach)

        df
        df /dev/sda1 – ogranicz wyniki tylko do jednej partycji
        df -h – wyświetl rozmiary w wygodnych dla użytkownika jednostkach (human readable)
        df -m – rozmiary w megabajtach

du – policz rozmiary katalogów i plików zawartych w podanym katalogu

        du – rozmiar obecnego katalogu
        du katalog – policz rozmiar podanego katalogu
        du -s – wypisz tylko sumę, a nie rozmiary poszczególnych podkatalogów
        du -sm – wypisz tylko sumę dla każdego katalogu i podaj rozmiar w megabajtach
        du -sm dir* | sort -n – posortuj wyniki od najmniejszego do największego z podanych katalogów


Środowisko

which – wypisuje gdzie znajduje się plik z programem o podanej nazwie

        which ls – zlokalizuj plik, który zostanie uruchomiony po wywołaniu komendy 'ls'

env – wypisuje aktualne wartości wszystkich zmiennych środowiskowych

alias – ustawia i wypisuje definicje skrótowych komend ('aliasów'), które są obecnie ustawione w środowisku

        alias – wypisuje aliasy
        alias ls 'ls --color=auto' – definiuje nowy alias o nazwie 'ls' i podanej treści


Urządzenia systemowe

/dev/null – studnia bez dna. Urządzenie do którego możemy pisać do woli, a wszystko co wpiszemy przepada.

        find -name "plik.*" 2>/dev/null – jeśli wsród wyników szukania nie chcemy oglądać komunikatów o błędach
        latex plik.tex >/dev/null – program wykona wszystkie czynności, ale nie zaśmieci nam konsoli logami
        licz >/dev/null 2>/dev/null & – jeśli chcemy puścić program w tle, a potem się wylogować (zamknąć konsole), musimy przekierować wyjścia z programu tak, aby nie próbował pisać do nieistniejącego już urządzenia. Urządzenie 'null' jest zawsze.

/dev/zero – składnica zer. Jest to urządzenie do czytania, które nigdy się nie kończy. Można z niego wczytać dowolną liczbę bajtów, a wszystkie będą równe zero.

        dd if=/dev/zero of=zera.txt count=1000 – wczyta tysiąc zer do pliku 'zera.txt'.
        cat /dev/zero – radzę nie próbować
        head -c 10 /dev/zero > zera.txt – wypisze pierwsze 10 bajtów z '/dev/zero' do pliku 'zera.txt'. W wyniku mamy plik z dziesięcioma zerami.

/dev/random – zbiór liczb losowych. Jest to urządzenie do czytania, które daje prawdziwie losowe dane. Korzysta przy tym z systemowego zbiornika entropii, który jest uzupełniany dzięki różnym przejawom aktywności użytkownika. Zbiór ten może się wyczerpać, dlatego nie należy z niego czytać wielu liczb na raz.

        od -t x1 -N 100 /dev/random – wypisze pierwsze 100 losowych bajtów z urządzenia /dev/random na ekran (w systemie szesnastkowym)

/dev/urandom – zbiór liczba pseudolosowych. Jest to urządzenie do czytania, które podaje liczby pseudolosowe. Ma ich do dyspozycji dowolnie dużo.

        od -t d1 -N 100 /dev/urandom – wypisze pierwsze 100 bajtów z urządzenia /dev/urandom na ekran (w systemie dziesiętnym)

/dev/stdin – standardowe wejście aktualnego procesu. Każdy proces który próbuje czytać z tego urządzenia, dostanie zawartość własnego wejścia.

        echo "ma kota" | cat ala.txt /dev/stdin – program cat połączy zawartość pliku ala.txt z tym co dostał na standardowe wejście
        (ale nie zmienia zawartości pliku)

/dev/stdout – standardowe wyjście aktualnego programu. Gdy proces wypisze coś do pliku /dev/stdout, pojawi się to na jego standardowym wyjściu.

        a2ps --output plik.ps plik.txt – program a2ps stworzy dokument postscript w pliku plik.ps
        a2ps --output /dev/stdout plik.txt – program a2ps wypisze dokument na ekran (jego standardowe wyjście)

/dev/stderr – standardowe wyjście dla błędów aktualnego programu. Gdy proces wypisze coś do pliku /dev/stderr, pojawi się to na jego standardowym wyjściu dla błędów. 


```
Resources:
```
*[http://www.astrouw.edu.pl/~jskowron////pracownia/komendy/](http://www.astrouw.edu.pl/~jskowron////pracownia/komendy/)

```
$ sudo apt-get install net-tools

$ ifconfig

enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::1381:71bf:cf55:2a87  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:87:2c:14  txqueuelen 1000  (Ethernet)
        RX packets 14656  bytes 19826502 (19.8 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2701  bytes 299629 (299.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 466  bytes 49216 (49.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 466  bytes 49216 (49.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
$ ifconfig enp0s3
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::1381:71bf:cf55:2a87  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:87:2c:14  txqueuelen 1000  (Ethernet)
        RX packets 14656  bytes 19826502 (19.8 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2701  bytes 299629 (299.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ ifconfig -a                >>> dispaly all available interface, even if they are down

$ ifconfig -s                >>> szort list, instead of details

Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
enp0s3    1500    14661      0      0 0          2706      0      0      0 BMRU
lo       65536      470      0      0 0           470      0      0      0 LRU

$ ifconfg -v                 >>> verbose mode, more details

$ ping 10.0.2.1              >>> ping Gateway
PING 10.0.2.1 (10.0.2.1) 56(84) bytes of data.
From 10.0.2.15 icmp_seq=1 Destination Host Unreachable

$  ping -c 5 8.8.8.8                                    >>> ping Google DNS
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=117 time=29.6 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=117 time=20.9 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=117 time=24.8 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=117 time=28.1 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=117 time=31.9 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4008ms
rtt min/avg/max/mdev = 20.972/27.120/31.942/3.844 ms
```
Additional Tools for Net Troubleshooting:

```
$ sudo apt install inetutils-traceroute
$ sudo apt install traceroute 
$ traceroute                          >>> is a network troubleshooting utility which shows number of hops taken to reach destination 
                                          also determine packets traveling path. Below we are tracing route to global DNS server IP Address 
                                          and able to reach destination also shows path of that packet is traveling.
                                          
$ traceroute 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.298 ms  0.113 ms  0.209 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  * * *
 8  * * *
 9  * * *
10  * * *
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  * * *
21  * * *
22  * * *
23  * * *
24  * * *
25  * * *
26  * * *
27  * * *
28  * * *
29  * * *
30  * * *

$ netstat -r                                     >>> Netstat (Network Statistic) command display connection info, routing table information etc. 
                                                     To displays routing table information use option as -r.
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
default         _gateway        0.0.0.0         UG        0 0          0 enp0s3
10.0.2.0        0.0.0.0         255.255.255.0   U         0 0          0 enp0s3
link-local      0.0.0.0         255.255.0.0     U         0 0          0 enp0s3

nslookup command also use to find out DNS related query. The following examples shows A Record (IP Address) of onet.pl.

$ nslookup onet.pl

Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	onet.pl
Address: 213.180.141.140

$ route

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         _gateway        0.0.0.0         UG    100    0        0 enp0s3
10.0.2.0        0.0.0.0         255.255.255.0   U     100    0        0 enp0s3
link-local      0.0.0.0         255.255.0.0     U     1000   0        0 enp0s3

$ host onet.pl

onet.pl has address 213.180.141.140
onet.pl mail is handled by 1 mx.poczta.onet.pl.

$ free - show memory status

              total        used        free      shared  buff/cache   available
Mem:        8585644     1064140     6433936       15916     1087568     7257180
Swap:       1466944           0     1466944

$ top  - show active processing (tasks, memory, users, used CPU%)

```
```
tree - show structure of all directories as tree

tree -d - show only catalogs
tree -d -L n - show how deep we are
tree -d -L 1 /  -  show one level below
tree -dL 2 /catalog_name  - show 2 levels below this catalog
tree -dL 2 /etc
tree -l /etc
tree --du -h /etc - show tree with size of files
tree -hF
tree -f -pug /etc - show tree with types and permissions

touch --date="2020-08-23  16:21:42" plik3.txt   - change modified date and time for file
mkdir -p /tmp/week1/app  - created parent directories "week1" and next directory "app"

Kopiowanie:

cp /home/nata/plik3.txt /tmp/
cp /home/nata/plik* /tmp/   - all files with "plik" name's copy in /tmp
cp /home/nata/lista.dat /home/nata/lista.data /tmp/   - copy several files
cp -r /home/nata/exercices/ /tmp/ - copy catalog "exercices" to /tmp
cp -r /etc/xdg/autostart/ /tmp/exercices/   - copy catalog "autostart" in /tmp/exercices

touch file1.txt /home/nata/
cp /etc/xdg/autostart/at* /home/nata/file1.txt 

cat file1.txt 

[Desktop Entry]
Type=Application
Name=AT-SPI D-Bus Bus
Exec=/usr/lib/at-spi2-core/at-spi-bus-launcher --launch-immediately
NoDisplay=true
X-GNOME-AutoRestart=true
X-GNOME-Autostart-Phase=Initialization

mv plik3.txt /tmp/newday/    - move plik3.txt in newday folder
mv /tmp/newday/plik3.txt /tmp/newday/newplik.txt   - change plik name if this plik is in the same directory
mv /tmp/newday/newplik.txt /tmp/newday/plik3.txt   - rename back

cp -R /tmp/newday/ /tmp/newday1/   - copy folder newday and rename on newday1
mv /tmp/newday1/ /tmp/newday1-2/   - changed folder name
mv *.txt /tmp/newday1-2/   - move files .txt from home directory when inside directory
rm /tmp/newday1-2/file1.txt   - deleted file file1.txt
rm -r /tmp/newday             - deleted folder newday with content
rm /tmp/newday1-2/*txt        - deleted all .txt files from folder newday1-2
rm -R /tmp/newday1-2/*        - deleted all content from folder newday1-2 (content included txt files and folder)
```
```
$ ls -li

total 16244
 467027 drwxr-xr-x  6 nata nata     4096 lip  8 15:19   nazwa_pliku   --- 467027(jest "i-node", informacja o węzłu, 
                                                                          węzeł nie przechowuj nazwy pliku i zawartość)
 ```
 ```
$ stat -f /home/nata/data/

  File: "/home/nata/data/"
    ID: 6ee6101e0de3ac55 Namelen: 255     Type: ext2/ext3
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 7745239    Free: 919523     Available: 520317
Inodes: Total: 1978592    Free: 1491923
```
```
$ stat /home/nata/data/                       - we can see (sieze, permissions, inode number, link count, type file(directory), group (1000), 
                                                           user name, data of modify, create, change, access time)

  File: /home/nata/data/
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: 801h/2049d	Inode: 442086      Links: 7
Access: (0755/drwxr-xr-x)  Uid: ( 1000/    nata)   Gid: ( 1000/    nata)
Access: 2020-09-08 04:56:51.299506798 +0200
Modify: 2020-08-24 14:05:42.623982728 +0200
Change: 2020-08-24 14:05:42.623982728 +0200
 Birth: -


```
```
Symbolik soft link, symlink, symbol link, soft link

$ ln -s /home/nata/Downloads/znalezione.log /znalezione-fss   - ln tworzy dowiązanie 
$ ls -lad /znalezione-fss /tmp/

drwxrwxrwt 17 root root 4096 wrz  9 12:31 /tmp/
lrwxrwxrwx  1 root root   35 wrz  9 12:28 /znalezione-fss -> /home/nata/Downloads/znalezione.log   - strzałka wskauje na symlink i że plik znalezione-fss
                                                                                                     został skopiowany z znalezione.log
                                                                                                     
$ ln znalezione.log znalezione_hard_link       -   hard link - dowiązanie twarde (links: 2)

$ stat znalezione_hard_link 

  File: znalezione_hard_link
  Size: 43        	Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d	Inode: 495491      Links: 2
Access: (0644/-rw-r--r--)  Uid: ( 1000/    nata)   Gid: ( 1000/    nata)
Access: 2020-09-09 12:20:25.640290657 +0200
Modify: 2020-08-07 10:12:01.160989648 +0200
Change: 2020-09-09 12:42:51.016614116 +0200
 Birth: -

```
```
Finding - wyszukiwanie by name, by user name

$ find /home/nata/lte/ -name "*copy*"

/home/nata/lte/copy3.txt
/home/nata/lte/copy2.txt
/home/nata/lte/copy5.txt
/home/nata/lte/copy4.txt

$ find /home/nata/ -name "*newnew*" -user nata

/home/nata/newnew.txt

$ find /home/nata/ -type f -name "*.LOG" -user nata -exec cp {} {}.bak \;

$ find /var/cache/debconf/ -name "*.dat"    - find all files with .dat

/var/cache/debconf/templates.dat
/var/cache/debconf/passwords.dat
/var/cache/debconf/config.dat

$ find -type f -size -1M -exec ls -sh {} \;
0 ./copy2.txt

root@nata-VirtualBox:~/lte# find -type f -size -20M -exec ls -sh {} \;

4,0K ./copy3.txt
0 ./copy2.txt
4,0K ./copy5.txt
4,0K ./copy4.txt

$ find /home/nata/lte/ -inum 563035         - find by inode number
/home/nata/lte/copy3.txt


```
usefull addition:

```
-a, --all            - do not ignore entries starting with
-A, --almost-all     - do not list implied . and ..
--author             - with -l, print the author of each file
-b, --escape         - print C-style escapes for nongraphic characters
--block-size=SIZE    - scale sizes by SIZE before printing them; e.g., '
--block-size=M'      - prints sizes in units of 1,048,576 bytes; see SIZE format below
-B, --ignore-backups - do not list implied entries ending with ~
-c   with -lt:       - sort by, and show, ctime (time of last modification of file status information); 
with -l:             - show ctime and sort by name; otherwise: sort by ctime, newest first
-C                   - list entries by columns
--color[=WHEN]       - colorize the output; WHEN can be 'always' (default if omitted), 'auto', or 'never'; more info below
-d, --directory      - list directories themselves, not their contents
-D, --dired          - generate output designed for Emacs' dired mode
-f                   - do not sort, enable -aU, disable -ls --color
-F, --classify       - append indicator (one of */=>@|) to entries
--file-type          - likewise, except do not append '*'
--format=WORD        - across -x, commas -m, horizontal -x, long -l, single-column -1, verbose -l, vertical -C
--full-time          - like -l --time-style=full-iso
-g                   - like -l, but do not list owner
--group-directories-first  - group directories before files;
                             can be augmented with a --sort option, but any use of --sort=none (-U) disables grouping
-G, --no-group       - in a long listing, don't print group names
-h, --human-readable - with -l and/or -s, print human readable sizes (e.g., 1K 234M 2G)
--si                 - likewise, but use powers of 1000 not 1024
-H, --dereference-command-line
              follow symbolic links listed on the command line
--dereference-command-line-symlink-to-dir   -  follow each command line symbolic link, that points to a directory
--hide=PATTERN        - do not list implied entries matching shell PATTERN (overridden by -a or -A)
--hyperlink[=WHEN]    - hyperlink file names; WHEN can be 'always' (default if omitted), 'auto', or 'never'
--indicator-style=WORD - append indicator with style WORD to entry names: none (default), slash (-p), file-type (--file-type), classify (-F)
-i, --inode           - print the index number of each file
-I, --ignore=PATTERN  - do not list implied entries matching shell PATTERN
-k, --kibibytes       - default to 1024-byte blocks for disk usage
-l                    - use a long listing format
-L, --dereference     - when showing file information for a symbolic link, show information for the file the link 
                        references rather than for the link itself
-m                    - fill width with a comma separated list of entries
-n, --numeric-uid-gid - like -l, but list numeric user and group IDs
-N, --literal         - print entry names without quoting
-o                    - like -l, but do not list group information
-p, --indicator-style=slash     - append / indicator to directories
-q, --hide-control-chars        - print ? instead of nongraphic characters
--show-control-chars            - show nongraphic characters as-is (the default, unless program is 'ls' and output is a terminal)
-Q, --quote-name       - enclose entry names in double quotes
--quoting-style=WORD   - use quoting style WORD for entry names: literal, locale, shell, shell-always, 
                         shell-escape, shell-escape-always, c, escape
-r, --reverse          - reverse order while sorting
-R, --recursive        - list subdirectories recursively
-s, --size             - print the allocated size of each file, in blocks
-S                     - sort by file size, largest first
--sort=WORD            - sort by WORD instead of name: none (-U), size (-S), time (-t), version (-v), extension (-X)
--time=WORD            - with  -l, show time as WORD instead of default modification time: atime or access or 
                         use (-u); ctime or status (-c); 
                         also use specified time as sort key if --sort=time (newest first)
--time-style=STYLE     - with -l, show times using style STYLE: full-iso, long-iso, iso, locale, 
                         or +FORMAT; FORMAT is interpreted like in 'date'; 
                         if FORMAT is  FORMAT1<newline>FORMAT2,  then  FORMAT1
                         applies to non-recent files and FORMAT2 to recent files; 
                         if STYLE is prefixed with 'posix-', STYLE takes effect only outside the POSIX locale
-t                     - sort by modification time, newest first
-T, --tabsize=COLS     - assume tab stops at each COLS instead of 8
-u                     - with -lt: sort by, and show, access time; with -l: 
                         show access time and sort by name; otherwise: sort by access time, newest first
-U                     - do not sort; list entries in directory order
-v                     - natural sort of (version) numbers within text
-w, --width=COLS       - set output width to COLS.  0 means no limit
-x                     - list entries by lines instead of by columns
-X                     - sort alphabetically by entry extension
-Z, --context          - print any security context of each file
-1                     - list one file per line.  Avoid '\n' with -q or -b
--help                 - display this help and exit
--version              - output version information and exit
```

Recources:

https://www.tecmint.com/linux-network-configuration-and-troubleshooting-commands/
