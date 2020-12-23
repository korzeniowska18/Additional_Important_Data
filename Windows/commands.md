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
How to check IP and all Network's settings:

```
$ ipconfig
```
How to check your business domain to look up its server's IP address.

```
$ Nslookup
Default Server:  UnKnown
Address:  192.168.100.1
```
How to find the IP address of each server between your computer and some website.

```
$ tracert google.com

Tracing route to google.com [172.217.16.46]
over a maximum of 30 hops:

  1     2 ms     1 ms     2 ms  192.168.100.1
  
$ tracert onet.pl

Tracing route to onet.pl [213.180.141.140]
over a maximum of 30 hops:

  1     2 ms     2 ms     2 ms  192.168.100.1
```
how to check connection with unit:

$ ping 192.168.1.1     # =>(IP address)
