## Git connection commands:

  Git powstał w 2005 roku (jego pierwszą wersję stworzył twórca Linuxa Linus Torvald, szwedzkojęzyczny Fin).
  Git został napisany w języku C. Używa algorytmu SHA1, co czyni go też bardzo bezpiecznym (hash, identyfikator).
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
$ git init
$ git status
$ git add <file/directory_name>
$ git status
$ git commit -m "Initial commit"
$ git status
$ git log
$ git push origin master
$ git pull

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
```

