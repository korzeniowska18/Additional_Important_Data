 ## CSS 

   Kaskadowe arkusze stylów (ang. Cascading Style Sheets, w skrócie CSS).
   Jest to język służący do opisu formy prezentacji (wyświetlania) stron WWW.
   
   Jest to coś co pozwala określać styl tagów. 
   Prezglądarka ma włąsne style, a my możemy nadpisać pewne style, 
   jak nie nadpiszemy to zostaną domyślne.
   
   CSS pozwala zmćniejszyć zakres prac podczas wprowadzenia zmian. 

   <style type="text/css">
      /*<![CDATA[*/   ---- CDATA = character data
      p
       {
        color: green;
        font-size: 30px;
       }
      p
      /*]]>*/
   </style>
   </head>
    <body>
 <p>Ciekawa informacja</p>
 <p>Ciekawa informacja</p>
 <p>Ciekawa informacja</p>
 <p style=color: blue>Ciekawa informacja</p>
 
 #ostatni paragraph będzie wyświetlony na niebiesko, wcześniejsze na zielono, 
 jest to style inline - styl w linii
 
 Jeśli wcześniej dodamy linię:
 <link hrew="style.css" rel="stylesheet" type='text/css"
 
 A wcześniej stworzymy plik "style.css" z zawartością:
 p
 {
 color: purple
}
 To teraz w naszej kaskade wszystkie napisy bedą koloru purple, oprócz ostatniego
 
 Możemy nadpisać zasady do fwóch tagów:
 
 p, b 
 
{
}

