TCP/IP (ang. Transmission Control Protocol/Internet Protocol) to zbiór protokołów służących do transmisji danych przez sieci komputerowe.

* [http://www.crypto-it.net/pl/teoria/protokoly-tcp-ip.html](http://www.crypto-it.net/pl/teoria/protokoly-tcp-ip.html)

Pierwsza z czterech warstw TCP/IP pośredniczy w komunikacji pomiędzy programami komputerowymi i protokołami niższych warstw, umożliwiając w ten sposób aplikacjom korzystanie z sieci. Programy mogą wykorzystywać różne protokoły warstwy aplikacji do przeprowadzania różnych operacji w sieci.

Istnieje wiele protokołów warstwy aplikacji, które wykorzystują transmisję TCP/IP. Jednymi z ważniejszych protokołów warstwy aplikacji są:

```
    HTTP, HTTPS - do przeglądania stron www,
    FTP, TFTP, NFS - do transmisji plików,
    SMTP - do wysyłania wiadomości email,
    POP3 - do otrzymywania wiadomości email,
    IMAP - do zarządzania wiadomościami email na serwerach,
    Telnet, rLogin - do zdalnego logowania się na innych komputerach,
    SNMP - do zarządzania sieciami komputerowymi,
    DNS - DNS - do znajdowania adresów IP przypisanych do adresów WWW,
    IRC - do czatów online
    
 ```

UDP

Drugim popularnym protokołem używanym w warstwie transportowej jest UDP (ang. User Datagram Protocol lub Universal Datagram Protocol). Jest to prostszy protokół, w którym komunikacja odbywa się bez nawiązywania żadnego stałego połączenia pomiędzy aplikacjami. Wszystkie pakiety wysyłane są niezależnie od siebie.
```
Dzięki swojej prostocie UDP jest szybsze niż TCP. 
Z drugiej jednak strony, nie zapewnia takiej niezawodności działania jak TCP. 
Przede wszystkim UDP nie gwarantuje, że wiadomości rzeczywiście dotarły do odbiorcy. 
UDP nie dostarcza pakietów w takiej samej kolejności, w jakiej zostały one wysłane. 
Ciężar uporządkowania otrzymywanych wiadomości i sprawdzenia czy nie nastąpiły błędy transmisji spoczywa na otrzymującej je aplikacji.
```
