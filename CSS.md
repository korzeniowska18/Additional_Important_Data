 ## CSS 

   Kaskadowe arkusze stylów (ang. Cascading Style Sheets, w skrócie CSS).
   Jest to język służący do opisu formy prezentacji (wyświetlania) stron WWW.
   
   Jest to coś co pozwala określać styl tagów. 
   Prezglądarka ma włąsne style, a my możemy nadpisać pewne style, 
   jak nie nadpiszemy to zostaną domyślne.
   
   CSS pozwala zmniejszyć zakres prac podczas wprowadzenia zmian, 
   wprowadzając zmienę tylko w jednym miejscu dla wielu elementów.
   ```
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
 ```
 #ostatni paragraph będzie wyświetlony na niebiesko, wcześniejsze na zielono, 
 jest to style inline - styl w linii
 
 Jeśli wcześniej dodamy linię:
 ```
 <link hrew="style.css" rel="stylesheet" type='text/css"
 
 A wcześniej stworzymy plik "style.css" z zawartością:
 p
 {
 color: purple;
}
 To teraz w naszej kaskadzie wszystkie napisy bedą koloru purple, oprócz ostatniego
 
 Możemy nadpisać zasady dla dwóch tagów:
 
 p, b 
 
{
}
```
Wprowadzenie zmian na podstawie class.
Klasa zawiera wiele elementów należących do jednej klasy.
```
p.definicja
{
color: red;
}

<p class="definicja">To jest niezwykły tekst</p>
<p>To jest tekst</p>
<p class="definicja">To jest niezwykły tekst</p>
<p b="definickja">To jest tekst</p>
```
Jeśli chcemy zmian dla "b" również
```
p.definicja, b.definicja
{
color: red;
}
```
dla wszystkich:
```
*.definicja
```
ID - jest to identyfikator, jedyny w swoim rodzaju.
Identyfikatora używa się do czegoś co występuje tylko raz na stronie.
Ten sam identyfikator można użyć na podstronie. 
```
<h1 id="wyloguj">Wyloguj</h1>
```
Aby wprowadzić zmiany dotyczące ID odwołujemy się w ten sposób:
```
h1#wyloguj
{
color: blue;
}
```
Używając "#" szukasz tylko jednego elementu, tak więc 
po znalezieniu go w drzewie (strukturze) strony, przeglądarka nie musi szukać dalej.

<p> - używamy do tworzenia tekstów, akapitów, paragraph wyświetla tekst z odstępem
 
 <span> używamy do tekstu, który ma być wyświetlony w jednej linii. 
 Span, jest to rozpietość, odległość pomiędzy jednym punktem a drugim.
 
 <div> tworzy bloczki i jest wyświetlany w blokach. 
 
 ```
 text-align: justify;  <-- używamy do div, ale nie używamy do span, bo nic nie zmienia
 
 width: 600px;         <-- możemy zmieniać szerokość bloku w div
 
 background: purple;   <-- zmieniamy tło dla span lub div
 
 text-align: center;
 
 class="center large"  <--używamy dwie klasy "center" i "large"
 
 Te zmiany będą dotyczyć każdego elementu HTML an stronie:
 
 * {
  text-align: center;
  color: blue;
}
 
 ```
Background property:

```
The background property is a shorthand property for:

    background-color
    background-image
    background-position
    background-size
    background-repeat
    background-origin
    background-clip
    background-attachment

background-repeat: repeat|repeat-x|repeat-y|no-repeat|initial|inherit;
repeat 	The background image is repeated both vertically and horizontally.  
        The last image will be clipped if it does not fit. This is default 	
repeat-x 	The background image is repeated only horizontally 	
repeat-y 	The background image is repeated only vertically 	
no-repeat 	The background-image is not repeated. The image will only be shown once 	
space 	The background-image is repeated as much as possible without clipping. 
       The first and last images are pinned to either side of the element, 
       and whitespace is distributed evenly between the images 	
round 	The background-image is repeated and squished or stretched to fill the space (no gaps) 	
initial 	Sets this property to its default value. Read about initial 	
inherit 	Inherits this property from its parent element. Read about inherit
```
Border
```
border-style: dotted;
border-width: 4px;
border-color: red;
border-top-style: dotted;
border-top-width: 4px;
border-top-color: red;
```
Margin
```
margin: 20px;
margin-top: 50px;
margin-bottom: 50px;
margin-right: 25px;
margin-left: 25px;
width: 300px;
margin: auto;   <-- Use the margin property to center align the <h1> element.
```
Padding
```
padding: 30px;
padding-top: 25px;
padding-bottom: 25px;
padding-left: 50px;
padding-right: 50px;
```
Height/Width
```
height: 100px;
width: 50%;
```
Box Model (div)
```
div {
  background-color: lightblue;
  width: 200px;
  padding: 25px;
  border-width: 25px;
  border-style: solid;
  border-color: navy;
}
div {
  background-color: lightblue;
  width: 200px;
  padding: 25px;
  border: 25px solid navy;
  margin: 25px;
}
```
Outline (pogrubiona ramka)
```
p {
  outline-style: solid;
  outline-width: 5px;
  outline-color: green;
}
ramka z czerwonymi pogrubionymi kółeczkami:
p {
  outline: red dotted 10px;
}
```
Text
```
Set the text color for the page to "red", and the text color for <h1> to "blue".
body {
  color: red;
}

h1 {
  color: blue;
}
h1 {
  text-align: center;
}
text-decoration: none;   <--- usunąć podkreślenie linka
text-transform: uppercase;   <--- zmienić text na duże pogrubione litery
text-transform: capitalize;   <-- zmienić text aby każde słowo zaczynało się od dużej litery
text-indent: 20px;   <--akapit pierwszej linii 20px 
```
Font
```
body {
  font-family: "Courier New";
}                                <-- page font family
p {
  font-style: italic;
}                                 <-- <p> elements as "italic" text
body {
  font-size: 20px;
}                              <-- font size for the page
h1 {
  font-size: 3em;
}
Wartość 1em jest równa wartości czcionki tekstu jaką posiada rodzic danego elementu HTML. 
Jeżeli rodzic elementu HTML posiada wartość właściwości font-size równą 15px, 
to wartość 1em, użyta w jakichkolwiek właściwościach CSS dzieci wspomnianego elementu rodzica, 
będzie wynosić również 15px. Wartość 1.2em będzie wynosić 18px, bo 15 × 1.2 = 18. 
Wartość 1.3em będzie wynosić 19.5px, bo 15 × 1.3 = 19.5 itd.

Określamy wartości właściwości font-size w jednostce em, 
dla poszczególnych części naszego kolumnowego układu elementów HTML: 
#caly_blok {
  font-size:15px;
  min-width:480px;
  max-width:1600px;
  border-left:1px solid gold;
  border-right:1px solid gold;
}

#naglowek {
  background-color:gold;
  text-align:center;
  font-size:1.6em;
  /* 1.6em = 24px, bo 15px × 1.6 = 24px */
}
Od teraz, wystarczy że zmienimy wartość właściwości font-size w regule CSS, 
która odnosi się do elementu #caly_blok, a przeglądarka internetowa sama obliczy 
wartości pozostałych właściwości CSS, w których została wykorzystana jednostka wartości em.

font-weight: bold;    <--- pogrubiona czcionka
p {
  font: italic 20px Verdana;
}                                <--- kursywa(pochylona), rozmiar czcionki, styl(rodzaj)
```
Links
```
a {
  color: green;
}

Set the color for unvisited links to "red", and the color for visited links "blue"

/* mouse over link */
a:link {
  color: red;
}

/* selected link */
a:visited {
  color: blue;
}

Remove underlines for visited and unvisited links, and specify "underline" for the hover and active link states.

<style>
/* unvisited link */
a:link {
  text-decoration: none;
}

/* visited link */
a:visited {
  text-decoration: none;
}

/* mouse over link */
a:hover {
  text-decoration: underline;
}

/* selected link */
a:active {
  text-decoration: underline;
}
</style>
------
a:active {
  background-color: yellow;
}
```
Lists
```
ul {
  list-style-type: square;
}
ol - ordered list
ul - unordered list
Set the image "sqpurple.gif" as the list item marker for the unordered list.
ul {
  list-style-image: url('sqpurple.gif');
}

Bajerki:)
With the list-style property: Set the unordered list marker to "img_marker.png", 
with a backup style of "circle", and display the markers inside the content flow.

The list-style property contains:
list-style-type list-style-position list-style-image

ul {
  list-style: circle inside url('img_marker.png');
}

Remove the bullets/markers from the list items.
Use the list-style-type property. (usuwanie kropeczek przed listą)
ul {
  list-style-type: none;
}
```
Tables
```
Set the border to "2px solid green" for table, th and td elements.
table, th, td {
  border: 2px solid green;
}
Collapse the table borders into a single border.
table {
  border-collapse: collapse;
}
table, td, th {
  border: 1px solid black;
}
Set the width of the table to "100%".
table {
  width: 100%;
}
Set the text alignment in <td> elements to "right".
td {
  text-align: right;
}
Set the padding in <th> elements to "15px".
th {
  padding: 15px;
}
```
Display/Visibility

```
Hide the <h1> element. It should still take up the same space as before.
h1 {
  visibility: hidden;
}
Hide the <h1> element. It should not take up any space.
h1 {
  display: none;
}
Display the list items as inline elements.
li {
  display: inline;
}

Display the <strong> elements as block elements.
strong {
  display:block;
}
```
Positioning
```
Position the <h1> element relative to the browser window. 50px from the top, and 50px from the right.
h1 {
  position: fixed;
  top: 50px;
  right: 50px;
  color: red;
}
Position the <h1> element 20px left, and 30px down, relative to its normal position.
h1 {
  position: relative;  <-- jeśli chce przesunąć w dół, piszę top
  top: 30px;
  left: -20px;
  color: red;
}
All CSS Positioning Properties
bottom 	- Sets the bottom margin edge for a positioned box
clip 	  - Clips an absolutely positioned element
left 	  - Sets the left margin edge for a positioned box
position -	Specifies the type of positioning for an element
right 	  - Sets the right margin edge for a positioned box
top      -	Sets the top margin edge for a positioned box
z-index 	- Sets the stack order of an element (behind the text)

Position the <h1> element 50px from the left, and 100px from the top, relative to the HTML page.
body, h1 {
  position: absolute;
  left: 50px;
  top: 100px;
  color: red;
}
Position the <img> element behind the text.
img {
  position: absolute;
  left: 0px;
  top: 0px;
  z-index: -1;
}
Position the element with the "topleft" class 30px from the left, and 15px from the top, relative to its container.
.topleft {
  position: absolute;
  top: 15px;
  left: 30px;
  font-size: 18px;
}
```
Overflow
```
Add a scrollbar to the <div> element.
div {
  background-color: #eee;
  width: 200px;
  height: 70px;
  border: 1px dotted black;
  overflow: scroll;
}
Specify that the overflowing text in the <div> element should not be visible, not even with scrolling.
div {
  background-color: lightblue;
  width: 200px;
  height: 200px;
  overflow: hidden;
}
Add a horizontal scrollbar to <div>.
overflow-x: scroll;
```
Align
```
Center align the <div> element using margins.
div {
  width: 300px;
  background-color: #b0e0e6;
  text-align: center;
  margin: auto;
}
Position the <div> element all the way to the right using absolute positioning.
div {
  position: absolute;
  right: 0px;
  width: 300px;
  background-color: #b0e0e6;
}
```
Combinators
```
Change the color of all <p> elements, that are descendants of <div> elements, to "red".
div p {          <-- wszystkie elemnty "p" wewnatrz "div"
  color: red;
}
Change the color of all <p> elements, that are immediate children of <div> elements, to "red".
div > p {        <-- wszystkie bezpośrednie elementy "p" wewnątrz 'div", span już nie
  color: red;
}
Change the color of <p> elements, that are the adjacent (immediately following) 
sibling of a <div> element, to "red".  <-- element, który idzie bezpośrednio po <div>
div + p {
  color: red;
}
Change the color of <p> elements, that are the siblings of a <div> element, to "red".
div ~ p {
  color: red;
}
```
Pseudo-classes
```
Set the background color for visited and unvisited links to "lightblue", 
and the background color for the hover and active link states to "yellow".
/* unvisited link */
a:link {
  background-color: lightblue;
}

/* visited link */
a:visited {
  background-color: lightblue;
}

/* mouse over link */
a:hover {
  background-color: yellow;
}

/* selected link */
a:active {
  background-color: yellow;
}
Change the background color, when a user hovers over p elements, with the class "highlight", to "lightblue".
p.highlight:hover {
  background-color: lightblue;
}
Set the background color of <p> elements, that are the first child of any element, to "lightblue".
p:first-child {
  background-color: lightblue;
}                               <--- tło perwszego elementu <p>
Set the background color of <input> elements that are in focus (clicked or active), to "lightblue".
input:focus {
  background-color: lightblue;
}                                  <--- podświetla kolorem pole do wpisania, kiedy się klika na to pole

```
Pseudo-elements
```
Set text color to red, for the first line of the <p> element.
p::first-line {
  color: red;
}
Set text color to "red", and the text size to "xx-large", for the first letter of the <p> element.
p::first-letter {
  color: red;
  font-size: xx-large;
}
Insert the image "smiley.gif" before, and after <p> elements, using the ::before and ::after pseudo-elements.
p::before{
  content: url(smiley.gif);
}
p::after{
  content: url(smiley.gif);
}
```
Opacity
```
Set the transparency/opacity of the <img> element to "0.4".
img {
  opacity: 0.4;
}                   <-- obrazek pod wualą:)

Exercise:

Remove the transparency/opacity of the <img> element when the user hovers over it with the mouse pointer.

img {
  opacity: 0.4;
}
img:hover {
  opacity: 1.0;
}                    <--kiedy najezdżamy kursorem na rysunek, jest przezrocysty
```
Attribute Selectors
```
a, target {
  background-color: lightblue;
}
Set the background-color to "lightblue" for elements with an attribute like: target="_blank"
a, target._blank {
  background-color: lightblue;
}
lub >>>
a[target="_blank"] {
  background-color: lightblue;
}

Set a border with the color "red", around elements with a "title" attribute containing the word "red".
Use attribute selector [attribute~=value].
[title~="red"] {
  border: 5px solid red;
}                              <-- ramki dookoła obrazków, które zawierają w opisie słowo "red"
Set a border with the color "red", around elements with a "title" attribute starting with "red".
[title^="red"] {
  border: 5px solid red;
}                               <-- ramki dookoła obrazków, które zawierają w opisie jako pierwsze słowo "red"
Set a border with the color "red", around elements with a "title" attribute ending with the word "flower" (not flowers).
[title$="flower"] {
  border: 5px solid red;
}                                <-- ramki dookoła obrazków, które zawierają w opisie jako ostatnie słowo "flower"
Set a border with the color "red", around elements with a "title" attribute containing the value "flow".
[title*="flow"] {
  border: 5px solid red;
}                                 <-- ramki dookoła obrazków, które zawierają w opisie jako elementy słowa "flow"
```
Rounded Corners
```
Give the <div> element rounded corners (use the shorthand property and the value "25px").
div {
  background: #73AD21;
  padding: 20px; 
  width: 200px;  
  border-radius: 25px;
}                                  <-- zaokragła kąty ramki
Give the <div> element a rounded corner (25px radius) on the bottom left side.
div {
  border-bottom-left-radius: 25px;
  background: #73AD21;
  padding: 20px; 
  width: 200px;  
}                              <-- zaokrągla lewy dolny kąt
  
```
Border Images
```
Give the <div> element an image border using the image "border.png". Slice the image at 30px and repeat it.
div { 
  border: 10px solid transparent;
  border-image: url(border.png) 30 round;
}                                          <--- ramka z powtarzających się kwadracików

Give the <div> element an image border using the image "border.png". Slice the image at 30px and stretch it.
div {
  border: 10px solid transparent;
  border-image: url("border.png") 30 stretch;
}
```
Backgrounds
```
Add a second background image ("img_flwr.gif") to the <body> element. Make sure that "img_flwr.gif" is displayed on top of the current background image.
Jedno tło na drugim
body {
  background-image: url(img_flwr.gif), url(paper.gif);
}
Change the size of the background image to: width 100px, height 80px.
body {
  background:url(img_flwr.gif);
  background-size: 100px 80px;
  background-repeat: no-repeat;
}
Change the size of the background image so it always fits the entire page.
Zmień rozmiar obrazu tła, aby zawsze pasował do całej strony.
html { 
  background: url(img_flower.jpg) no-repeat center center fixed; 
  background-size: cover;
}
Specify that the background image position should start from the upper left corner of the content-box.
Określ, że pozycja obrazu tła powinna zaczynać się od lewego górnego rogu pola treści.
div { 
  border: 10px solid black;
  padding: 35px;
  background: url(img_flwr.gif);
  background-repeat: no-repeat;
  background-origin: content-box;
}
Specify that the "painting area" of the background should be to the outside edge of the padding.
Określ, że „obszar malowania” tła powinien znajdować się na zewnętrznej krawędzi wypełnienia.
div { 
  border: 10px dotted black;
  padding: 35px;
  background: lightblue;
  background-clip: padding-box;
}
```
Colors
```
Set the opacity for the background color of the <h1> element to "0.3" by using a RGBA color instead of RGB.
h1 {
   background-color: rgba(0,255,0,0.3);
}
Set the following HSL color as the background of the <h1> element:
Set the Hue to red (0), Saturation to 100%, and lightness to 50%.
h1 {
   background-color: hsl(0,100%,50%);
}
Set the opacity for the background color of the <h1> element to "0.3" by using a HSLA color instead of HSL.
h1 {
  background-color: hsla(0,100%,50%,0.3);
}
Set the transparency/opacity of the <h1> element to "0.4".
h1 {
  background-color: red;
  opacity: 0.4;
}
```
Gradients
```
Set a linear gradient background for the <div> element, going from the top to bottom, transitioning from "white" to "green".
div {
  background-image: linear-gradient(white, green);
}                                        <--- ładne tło z nierównym kolorem, od ciemniejszego do bardziej jasnego
Set a linear gradient background for the <div> element, going from the top left to the bottom right, transitioning from "white" to "green".
div {
  background-image: linear-gradient(to bottom right, white, green);
}                                        <--- kolor się zmienia, od lewego górnego rogu do prawego dolnego, w prawym jest bardziej nasycony
Set a linear gradient background for the <div> element, going at a 70 degree angle, transitioning from "white" to "green".
div {
  background-image: linear-gradient(70deg, white, green);
}
Set a linear gradient background for the <div> element, going from the top to bottom, transitioning from "white" to "red" to "blue" to "green".
div {
  background-image: linear-gradient(white, red, blue, green);
}
Set a linear gradient background for the <div> element, going from the top to bottom, transitioning from "rgba(0,255,0,0.2)" to "rgba(0,255,0,1)".
div {
  background-image: linear-gradient(rgba(0,255,0,0.2), rgba(0,255,0,1));
}
Set a radial gradient background for the <div> element, transitioning from "white" to "green".
div {
  background-image: radial-gradient(white, green);
}                                 <--- color zostaje rozprowadzony na stronie od środka

Set a radial gradient background for the <div> element, with a circle shape, transitioning from "white" to "green".
div {
  background-image: radial-gradient(circle, white, green);
}

```
Shadow Effects
```
Set a "2px" horizontal, and "2px" vertical, text shadow for the <h1> element.
h1 {
  text-shadow: 2px 2px;
}                            <--- cień za tekstem
Change the color of the text shadow to "green", and set a "5px" blur radius.
h1 {
  text-shadow: 2px 2px 5px green;
}
Add a new shadow (do not remove the current one) to the <h1> element with: no horizontal or vertical shadow, 10px blur, and a red color.
h1 {
  text-shadow: 2px 2px 5px green, 0 0 10px red;
}
Set a "10px" horizontal, and "10px" vertical, box shadow for the <div> element.
div {
  box-shadow: 10px 10px;
}
Change the color of the box shadow to "grey", and set a "5px" blur.
div {
  box-shadow: 10px 10px 5px grey;
}

```
Text Effects
```
Specify that the overflowed content for the <p> element should be signaled with an ellipsis (...)
p {
  white-space: nowrap; 
  width: 200px; 
  border: 1px solid #000000;
  overflow: hidden;
  text-overflow: ellipsis;
}
Specify that text in the <p> element should wrap, even if it needs to split in the middle of a word.
p {
  width: 150px; 
  border: 1px solid #000000;
  word-wrap: break-word;
}                              <-- kiedy długie słowo ucieka za ramkę
Specify that text in the <p> element can break between any two letters.
p {
  width: 150px; 
  border: 1px solid #000000;
  word-break: break-all;
}
```
Web Fonts
```
Add a web font with the name "sansation" and the URL "sansation_light.woff".
@font-face {
   font-family: sansation;
   src: url(sansation_light.woff);
}
body {
  font-family: sansation;
}
Add another @font-face rule for bold characters of the "sansation" font. Use the URL "sansation_bold.woff".
@font-face {
   font-family: sansation;
   font-weight: bold;
   src: url(sansation_bold.woff);
}

body {
   font-family: sansation;
}
```
2D Transforms
```
With the transform property, move the <div> element 100px to the right, and 200px down.
div {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  border: 1px solid black;
  transform: translate(100px,200px);
}
With the transform property, rotate the <div> element 45 degrees.
div {
  width: 100px;
  height: 100px;
  margin: 50px;
  background-color: lightblue;
  border: 1px solid black;
  transform: rotate(45deg);                      < --- rotate - obraca element
}
With the transform property, change the size of the <div> to half its width, but double its height.
div {
  width: 100px;
  height: 100px;
  margin: 50px;
  background-color: lightblue;
  border: 1px solid black;
  transform:scale(0.5, 2);               <--- scale - zmienia rozmiar
}
With the transform property, skew the <div> element 20 degrees along the X-axis, and 30 degrees along the Y-axis.
Use the skew(), or skewX() and skewY() methods.
div {
  width: 100px;
  height: 100px;
  margin: 50px;
  background-color: lightblue;
  border: 1px solid black;
  transform: skew(20deg, 30deg);                  <--- rozciąga element pod skosem
}
```
3D Transforms
```
With the transform property, rotate the <div> element 150deg around its X-axis.
Use the rotateX() method.
div {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  border: 1px solid black;
  transform: rotateX(150deg);
}                                         <--- rotateX obraca element do góry nogami
With the transform property, rotate the <div> element 120deg around its Y-axis.
Use the rotateY() method.
div {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  border: 1px solid black;
  transform: rotateY(120deg);
}                                         <-- obraca tak, że litery czytamy z lewa na prawo
With the transform property, rotate the <div> element 90deg around its Z-axis.
Use the rotateZ() method.
div {
  width: 100px;
  height: 100px;
  background-color: lightblue;
  border: 1px solid black;
  transform: rotateZ(90deg);
}                                        <--- rotateZ przewraca element na bok

```
Transitions
```
Add a 2 second transition effect for width changes of the <div> element.
div {
  width: 100px;
  height: 100px;
  background: red;
  transition: width 2s;
}
Specify that the transition of the <div> element should have a "ease-in-out" speed curve.
Use the transition-timing-function property.
div {
  width: 100px;
  height: 100px;
  background: red;
  transition: width 2s;
  transition-timing-function: ease-in-out;
}
Specify that the transition of the <div> element should have a "0.5" second delay before starting.
Use the transition-delay property.
div {
  width: 100px;
  height: 100px;
  background: red;
  transition: width 2s;
  transition-delay: 0.5s;
}
Add a 2 second transition effect for background, and transform changes of the <div> element.
Use the transition property, with 2 sets of values (separated by comma).
div {
  width: 100px;
  height: 100px;
  background: red;
  transition: background 2s, transform 2s;
}
Using the transition shorthand property, specify width changes for the <div> element should have:
"2" second duration, "ease-in-out" speed curve, and a "0.5" second delay before starting.
transition: property duration timing-function delay.
div {
  width: 100px;
  height: 100px;
  background: red;
  transition: width 2s ease-in-out 0.5s;
}
```
Animations
```
Add a 2 second animation for the <div> element, which changes the color from red to blue. Call the animation "example"
Use the @keyframes rule, and the animation-name, and animation-duration properties.
div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 2s;
}

@keyframes example {
  from {background-color: red;}
  to {background-color: blue;}
}                                      <--- element div(kwadrat) zmienia kolor na 2 sekundy
Add the following 5 steps to the animation "example" (using 0%, 25%, 50%, 75%, and 100%):

    0% - Set background color to "red", left position to "0px", top position to: "0px"
    25% - Set background color to "blue", left position to "0px", top position to: "200px"
    50% - Set background color to "green", left position to "200px", top position to: "200px"
    75% - Set background color to "yellow", left position to "200px", top position to: "0px"
    100% - Set background color to "red", left position to "0px", top position to: "0px"

div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
}

@keyframes example {
  0%   {background-color: red; left:0px; top:0px;}
  25%  {background-color: blue; left:0px; top:200px;}
  50%  {background-color: green; left:200px; top:200px;}
  75%  {background-color: yellow; left:200px; top:0px;}
  100% {background-color: red; left:0px; top:0px;}
}                                                    <--- sprawia to, ze element div(kwadrat) przemieszcza się i zmienia kolor
Specify that the animation of the <div> element should have a "1" second delay before starting.
Use the animation-delay property.
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 2s;
  animation-delay: 1s;
}

@keyframes example {
  0%   {background-color: red; left:0px;}
  50%  {background-color: yellow; left:200px;}
  100% {background-color: red; left:0px;}
}                                                    <-- element div przemieszcza sie w bok i zmienia kolor
Specify that the animation of the <div> element should continue to loop for ever.
Use the animation-iteration-count property.
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes example {
  0%   {background-color: red; left:0px;}
  50%  {background-color: yellow; left:200px;}
  100% {background-color: red; left:0px;}
}                                        <--- animacja jest zapętlona i działa cały czas, kwadrat cały czas przesuwa się z prawa na lewo
                                              i z powrotem i zmienai kolor
Specify that the animation of the <div> element should alternate between running forwards and backwards.
Use the animation-direction property.
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: infinite;
  animation-direction: alternate;   
}

@keyframes example {
  0%   {background-color: red; left:0px; top:0px;}
  25%  {background-color: blue; left:0px; top:200px;}
  50%  {background-color: green; left:200px; top:200px;}
  75%  {background-color: yellow; left:200px; top:0px;}
  100% {background-color: red; left:0px; top:0px;}
}                                                                  < -- na początku animacja działą w tym kierunku: w dół w prawo, do góry, w lewo i t.d.w kółko
                                                                        po zmianie animation-direction: a teraz w dół w prawo, do góry, w lewo, 
                                                                        ale potom w prawo, w dół, w lewo, do góry (czyli nie w kółko, a zmienia kierunek)
```
