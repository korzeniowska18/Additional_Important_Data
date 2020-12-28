## Git connection commands:

  Git powstał w 2005 roku (jego pierwszą wersję stworzył twórca Linuxa Linus Torvald, szwedzkojęzyczny Fin).
  Git został napisany w języku C. Używa algorytmu SHA1, co czyni go też bardzo bezpiecznym (hash, identyfikator).
  
Working directory
Staging Area (index)
Git folder (Git repository) 

4 stany plików w repozytorium:
- nieśledzony (untracked)                          <- gdy dodamy nowy plik (lub usuniemy ze śledzonych)
- śledzony niezmodyfikowany (tracked unmodified)   <- pliki które zostały już dodane do repozytorium (gdy wykonamy commit) 
                                                   i od tego czasu w katalogu roboczym nie był zmieniany
- śledzony zmodyfikowany (tracked modified)        <- plik dodany wcześniej do repozytorium, a aktualnie zmieniony (edytowany) w folderze roboczym
- śledzony w poczekalni (tracked staged)           <- plik, który został dodany do indeksu (stage area) i oczekuje na commit 

```
$ git config -l
$ git config --global user.name "user_name"
$ git config --global user.email "user_email@users.noreply.github.com"

Remove a global identity:

git config --global --remove-section user.name
git config --global --remove-section user.email

```
## General git commands:
```
$ git init         <---Tworzy nowe repozytorium w katalogu, w którym polecenie jest wywołane
$ git status
$ git add <file/directory_name>
$ git status
$ git commit -m "Initial commit"
$ git status
$ git log
$ git push origin master
$ git pull
$ gitk 
$ gitg

```
```
$ git --version
$ which version
$ git remote add origin https://<your-git-service-address>/owner/repository.git
$ cd <path where you would like the clone to create a directory>
$ git clone https://yourusername@bitbucket.org/username/projectname.git

Helps command:

$ git diff --help   <will be appear Manual Page>
$ git help diff
$ git checkout -h
$ git-status(1) Manual Page
$ apt-get install git
$ git log             <will display all your commits with the author and hash. 
                      This will be shown over multiple lines per commit. >
$ git log --decorate --oneline --graph   <To see the log in a prettier graph-like structure>
$ git log --oneline    <will show all of your commits with only the first part of the hash and the commit message>
$ git shortlog     <summarizes git log and groups by author>
$ To simply see the number of commits and suppress the commit description, pass in the summary option:
-s
--summary
$ git shortlog -s
$ git log --all --grep "removed file"       <Will search for removed file string in all logs in all branches.>

$ git log --grep="add file" --invert-grep   <Will show all commits that do not contain add file.>
$ git log --after 2016-05-01

An alias to --after is --since.
Flags exist for the converse too: --before and --until.

$ git log --author=author

$ git show 48c83b3690dfc7b0e622fd220f8f37c26a77c934  (commit number)
$ git checkout -b <new-branch>               <--create new branch>
$ git checkout -b <new-branch> <existing-branch>
$ git rm filename      <-- delete file
$ git diff   <--is a multi-use Git command that when executed runs a diff function on Git data sources. 
$ git diff 1234abc..6789def # old new
$ git status -v
Which will trigger the verbose settings of the status command
$ git merge feature/add-gremlins

$ git commit --amend    <---Poprawki w ostatnim (najnowszym) commicie. Zmiany w
                           zawartości i message, nowe metadane też.

$ git commit --amend -m "our new message    <--- Jeśli chcemy zmienić tylko komentarz, to możemy napisać tak

$ git log --oneline //w jednej linii podstawowe informacje
$ git log --oneline 10 //ile linii (od najnowszych)
$ git log --since "2019" //od 2019
$ git log --since="5.4.2019" //od konkretnej daty; innym zapisem

$ git log --grep    <--- wyszukiwanie commitów
$ git log --grep "plik.txt"    <---wyszukiwanie w message, wielkośc liter ma znaczenie
$ git log --grep="delete"      <--- jw, ale w innym zapisie

$ git log --stat    <---które pliki zmienił commit i w jaki sposób wyświetla listę commitów jak git log

$ git show          <--- Co się zmieniło (szczegółowo) w danym commicie (wnajnowszym). Możemy też wskazać o jaki commit nam chodzi, np.
$ git show 5b8d8d0febd48406dc3dcc93599e23177d60b01e
$ git show 5b8d8d0

$ git diff (porównanie)
$ git diff nazwa-pliku      <---konkretny plik
$ git diff --cached         <---pliki w stage (pliki sledzone w poczekalni) z plikami z repozytorium
                            (domyślnie z tymi w HEAD, czyli ostatniego commitu w gałęzi). 
                            Zamiast cached można użyć też parametru --staged, który robi dokładnie to samo.
                            Możliwość porównania plików w różnych commitach
$ git diff 852ff1d 962a5ab nazwa-pliku      <--- porównanie wersji z commitów

$ git diff
$ git diff --staged
$ git diff nazwa-pliku

$ git rm plik                          <---Usuwa pliki z katalogu roboczego i wersję z indeksu. Informacją o tym
                                       znajduje się w staging area (najbliższy commit to uwzględni). Informację
                                       o tym zobaczymy po wyświetleniu satusu repozytorium (git status).
                                       Oczywiście nie usuwa takiego pliku z historii w repozytorium.
$ git rm --cached plik                 <---Usuwa pliki z indeksu, ale nie z katalogu roboczego (po tym poleceniu plik ma stan nieśledzony).
                                       Można więc powiedzieć, że robi 1 z 2 etapów, które wykonuje git rm plik.
$ rm file                              <---usuwa z katalogu roboczego.
$ git rm -- cached file                <--usuwamy z indeksu.
$ git rm file                          <---usuwa z katalogu roboczego i z indeksu.

$ git mv index.txt index.html
                                         <---Zamiana nazwy pliku. Przy czym w praktyce widzimy, że mamy
                                         zadanie renamed w następnym commicie, które oznacza
                                         polecenie usunięcia jednego pliku i dodania nowego.
                                         
$ git checkout plik                     <--- Zmiany z wersji roboczej są usuwane i przywracana jest (w katalogu roboczym) wersja,
                                        które znajduje się w indeksie. W praktyce jeśli nie mamy żadnej zmiany w staging area
                                        to wersja jaka była po ostatnim commicie
$ git checkout -- plik                  <--- lepiej tak git checkout -- plik, niż tak: git checkout plik
                                        Bezpieczniej z dwoma kreskami po poleceniu checkout. Bez dwóch
                                        kresek Git nie zawsze uzna, ze kolejnym parametrem będzie plik.
$ git checkout -- *.txt
$ git checkout HEAD -- plik             <---do katalogu roboczego przywracana jest wersja pliku z ostatniego commita

$ git checkout 5a33dd2
                                        <---Przywrócenie indeksu z tego commitu. W praktyce nasz katalog
                                        roboczy po takiej operacji będzie się składał z indeksu w chwili
                                        wykonania commita o danym identyfikatorze.
$ git checkout id-commita               <--ustawienie HEAD na tym commicie
$ git checkout nazwa-brancha            <--przełączenie na inną gałąź

$ git reset / git reset HEAD
                                        <--- Usuwa pliki ze staging area (pliki są nadal śledzone i są oczywiście w katalogu roboczym).
                                        Przywracamy stan indeksu do stanu po ostatnim commicie, więc
                                        wszystko co dodaliśmy do indeksu (staging area, poczekalnia) już się po tej operacji w nim nie znajduje.
                                        Użycie wskaźnika HEAD jest czytelniejsze, wiemy do czego wracamy (stanu po ostatnim commicie). 
                                        Ponadto możemy spokojnie użyć po nim ścieżki dio pliku (przy użycie po reset mogą być problemy i wtedy lepiej
$ git reset -- nazwa pliku

$ git reset / git reset HEAD
$ git reset
$ git reset HEAD
                                        <---Alternatywnie wskazujemy plik/pliki/katalog, którego zmiany
                                        chcemy usunąć ze staging area (przywrócić pierwotną wersję).
$ git reset -- plik
$ git reset HEAD plik

$ git rm plik                           <---usuwa plik z indeksu (staging area) i z katalogu roboczego
$ git rm --cached plik                  <---usuwa plik z indeksu, plik staje się nieśledzony.
$ git checkout -- plik                  <---do katalogu roboczego przywracana jest wersja, która znajduje się aktualnie w indeksie
$ git reset HEAD plik                   <---usuwa z indeksu zmiany (przywracamy do indeksu wersję jaka była po ostatnim commicie)

$ .gitignore                            <---Określamy listę plików i folderów, które nie trafią do repozytorium.
                                        .gitignore obejmie tylko pliki nieśledzone, więc każdy nowo dodany plik (katalog z
                                        plikami), by był ignorowany, musimy dodać do .gitignore. Jeśli pliki są już
                                        śledzone, musimy zmienić ich stan na nieśledzony). 
                                        
gałąź master

$ git branch                            <--- Na jakim branchu (gałęzi) się znajdujemy. Początkowo mamy jedną gałąż z nazwą master. Po wpisaniu git
                                        branch dostaniemy informację o istniejących gałęziach (by to zobaczyć wcześniej musimy zrobić choć jeden commit)
                                        
branches - gałęzie

Gałąź główna - master (pierwsza gałąź w naszym repozytorium)

Tworzenie osobnych gałęzi służy rozwijaniu niezależnych/testowych/pobocznych elementów projektu.

Gałęzie mogą być scalane - merge
Gałęzie mogą mieć zupełnie różną zawartość.

$ git branch                           <---lista wszystkich branchów
$ git branch                           <---nazwa-nowego-brancha //tworzymy nową gałąź
$ git checkout nazwa-istniejącego-brancha    <---przełączamy się na inną gałąź
$ git merge nazw-brancha                     <---łączenie gałęzi na której jesteśmy ze wskazaną gałęzią

$ Git push                              <---przekazywanie zmian z jednego repozytorium (naszego lokalnego)
                                        do innego repozytorium (zdalnego)
                                        
$ Git pull                              <---Pobieranie zmian z jednego repozytoriu (zdalnego) na inne (nasze lokalne).
                                        Nasze sklonowane repozytorium jest aktualizowane
```

