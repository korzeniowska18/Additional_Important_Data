# Some commands and solutions in Windows shell

```
$ netstat   >>> to polecenie służy do wyświetlania aktywnych połączeń

$ netstat –a   >>> to polecenie służy do  sprawdzenia zajętości portów TCP/UDP

$ netstat -a -n -o | findStr "4200"`     >>> to polecenie odnajduje PID process, który jest wykorzystany przez port

Po uruchomieniu proces otrzymuje swój identyfikator - PID

Aby zabić dany proces musimy znać jego aktualny PID. Odczytaj PID przynależny do konkretnego procesu i wykonujemy polecenie: taskkill

$ taskkill -f /pid 15836
SUCCESS. The process with PID 15836 has been terminated.

```
We can to fix this error in next way:

ERROR:

Port 4200 is already in use.Use ‘-port’ to specify a different port error Reasons

Resolution:
```
$ netstat -a -n -o | findStr "4200"`
TCP    127.0.0.1:4200         0.0.0.0:0              LISTENING       15836
$ $ taskkill -f /pid 15836
SUCCESS. The process with PID 15836 has been terminated.
```
