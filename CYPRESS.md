# Cypress - 

to framework JavaScript do testów e2e (end to end), który skupia się na tym aby testowanie aplikacji było prostsze i szybsze.

# Cypress VS Selenium

* [complete framework](#complete-framework)
* [more stable](#more-stable)
* [not required solid programming skills](#not-required-solid-programming-skills)
* [test and mock APIs](#not-required-solid-programming-skills)
* [don't need test environment](#don't-need-test-environment)
* [no IE and Safari support](#no-IE-and-Safari-support)
* [asynchronous code](#asynchronous-code)
* [no mobile but mobile view](#no-mobile-but-mobile-view)
* [single domain and single tab](#single-domain-and-single-tab)
* [not friendly with iFrames](#not-friendly-with-iFrames)

What we need for Cypress:

```
install Chrome browser
install Node.js                       >>> $ sudo apt install nodejs
install Git                           >>> $ sudo apt-get install git
install IDE(Visual Studio Code)
```
https://github.com/nodesource/distributions/blob/master/README.md#debinstall

How to check versions:

```
$ google-chrome --version    >>> Google Chrome 81.0.4044.138 
$ node -v                    >>> v8.10.0
$ git --version              >>> git version 2.17.1

```
Cypress installation:

```
$ npm install cypress --save-dev
$ npx cypress open
```
https://docs.cypress.io/guides/references/configuration.html#Options

For example:
```
{
    "baseUrl": "https://localhost:4200",
    "ignoreTestFiles": "**/examples/*",
    "viewportHeight": 768,
    "viewportWidth": 1024
}
```
In integration folder create new file with test name: firstTest.spec.js

# The HTML DOM (Document Object Model)
```
* HTML DOM consists of: HTML tags, HTML attributes and Attribute values
* "Class" and "Values" are also HTML attribute names
* "Class" attribute can have several values and each value separated by space
* HTML tags usually come in pairs with opening and closing tag. Closing tag has the same name and forward slash.
* Value in between angle brackets >here< is a plain text
* Elements above the "key" Web element are Parent Elements
* Elements inside of the "key" Web element are Child Elements
* Elements placed at the same level side by side are Sibling Elements
```
Example for Test's structure:

```
describe("My first suite"), () => {

    describe("Suite section") () => {

        beforeEach("code for every test", () => {
            //repeatadly code
    })
    

    it("first test", () => {

    })

    it("second test", () => {

    })

    it("third test", () => {

    })


})



describe("My second suite"), () => {

    it("first test", () => {

    })

    it("second test", () => {

    })

    it("third test", () => {

    })


})
```

How to use Locators:

```
/// <reference types="cypress" />

describe("My first suite", () => {

    it("first test", () => {

        cy.visit('/')
        cy.contains('Forms').click()
        cy.contains('Form Layouts').click()

        //by Tag Name
        cy.get('input')

        //by ID
        cy.get('#inputEmail1')

        //by Class Name
        cy.get('.input-full-width')

        //by Attribute Name
        cy.get('[placeholder]')

        //by Attribute Name and value
        cy.get('[placeholder="Email"]')

        //by Class Value
        cy.get('[class="input-full-width size-medium shape-rectangle"]')

        //by Tag name Attribute with value
        cy.get('input[placeholder="Email"]')

        //by two different attributes
        cy.get('[placeholder="Email"][type="email"]')

        //by Tag name, Attribute with value, ID and class name
        cy.get('input[placeholder="Email"]#inputEmail1.input-full-width')

        //The most recomended way by Cypress(for elements which created own attributes, 
        //this is own locator and with this locator tests will always work
        cy.get('[data-cy="imputEmail1"]')

    })

})
```
In the test results we can to see how much elements with this Name found. 
