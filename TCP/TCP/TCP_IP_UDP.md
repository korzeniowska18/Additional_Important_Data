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

TCP

Najpopularniejszym protokołem warstwy transportowej jest TCP (ang. Transmission Control Protocol). Podczas transmisji danych, TCP zestawia połączenie pomiędzy komunikującymi się stronami (ang. connection oriented) przez zainicjowanie tzw. sesji (ang. session). TCP jest protokołem niezawodnym (ang. reliable), w którym odbiorca potwierdza otrzymanie każdej wiadomości (ang. acknowledge). Wszystkie wiadomości dostarczane są w takiej samej kolejności, w jakiej zostały wysłane (ang. ordering).

Wszystkie cechy wymienione powyżej są zapewniane prze warstwę TCP. Oznacza to, że TCP może współdziałać z innymi, bardziej zawodnymi protokołami niższych warstw i nie powinno to afektować komunikacji z perspektywy warstwy aplikacji.
Niezawodność TCP
(ang. reliability)

W czasie wysyłanie danych, TCP zapewnia, że wszystkie wiadomości zostały dostarczone do miejsca przeznaczenia. Odbiorca testuje każdy otrzymany pakiet pod kątem błędów transmisji (poprzez wyliczanie sumy kontrolnej danych). Jeśli wiadomość jest poprawna, odbiorca wysyła potwierdzenie (ang. acknowledgement) do nadawcy. Jeśli nadawca nie otrzyma potwierdzenia w przeciągu określonego (konfigurowalnego) czasu, to ponownie wysyła zagubiony pakiet.

Po kilku nieudanych próbach, TCP zakłada, że odbiorca jest nieosiągalny i informuje warstwę aplikacji, że transmisja zakończyła się niepowodzeniem.

UDP

Drugim popularnym protokołem używanym w warstwie transportowej jest UDP (ang. User Datagram Protocol lub Universal Datagram Protocol). Jest to prostszy protokół, w którym komunikacja odbywa się bez nawiązywania żadnego stałego połączenia pomiędzy aplikacjami. Wszystkie pakiety wysyłane są niezależnie od siebie.
```
Dzięki swojej prostocie UDP jest szybsze niż TCP. 
Z drugiej jednak strony, nie zapewnia takiej niezawodności działania jak TCP. 
Przede wszystkim UDP nie gwarantuje, że wiadomości rzeczywiście dotarły do odbiorcy. 
UDP nie dostarcza pakietów w takiej samej kolejności, w jakiej zostały one wysłane. 
Ciężar uporządkowania otrzymywanych wiadomości i sprawdzenia czy nie nastąpiły błędy transmisji spoczywa na otrzymującej je aplikacji.
```

Zastosowanie UDP

UDP jest preferowane jeśli przesyłane pakiety danych są nieistotne lub komunikacja musi odbywać się z wyjątkowo dużą prędkością. Przykładowo UDP jest używane do przesyłania zapytań DNS (z powodu bardzo dużej liczby zapytań kierowanych do relatywnie niewielu serwerów DNS). UDP jest używane również podczas transmisji audio i video, gdzie utrata pewnej liczby pakietów nie jest bardzo uciążliwa dla odbiorcy.

Istnieje wiele protokołów warstwy aplikacji, które używają UDP, na przykład:

    DNS
    DHCP
    TFTP
    SNMP
    RIP
    VOIP
