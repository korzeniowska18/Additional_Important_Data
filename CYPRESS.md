# Cypress - 

to framework JavaScript do testów e2e (end to end), który skupia się na tym aby testowanie aplikacji było prostsze i szybsze.

My Notes according to course from Udemy.com:

https://www.udemy.com/course/cypress-web-automation-testing-from-zero-to-hero/learn/lecture/18179588?start=0#overview

I can recommend this course. 

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

Co odróżnia cypressa od innych narzędzi?

* Nie opiera się na Selenium – zbudowany jest na nowej architekturze. Cypress działa w tej samej pętli uruchomieniowej, co twoja aplikacja.
* Koncentruje się na sprawnym wykonywaniu testów – jego użycie jest intuicyjne i proste.
* Jest uniwersalny – działa prawdopodobnie na wszystkim co może być uruchomione w przeglądarce. Dobrze powinien sobie poradzić nawet na starszych aplikacjach, 
  nie tylko tych używających nowoczesnych frameworków.
* Testy są pisane w javascripcie – dla jednych wada dla innych zaleta ale cypress jest oparty na javascripcie.
* Wszystko czego potrzeba w 1 narzędziu – Nie trzeba instalować osobnych narzędzi aby uruchomić testy.
* Narzędzie zarówno dla programistów jak i QA.
* Cypress jest szybki – pozwala na równoczesny development i testowanie.

More:

https://devenv.pl/cypress-wprowadzenie/


What we need for using Cypress:

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
$ npm start              >>> start application
```
How to Update Cypress:

```
To update Cypress:

Quit this app.
If using npm, run 
$ npm install --save-dev cypress@5.0.0
If using yarn, run 
$ yarn upgrade cypress@5.0.0
Run 
$ node_modules/.bin/cypress open >>> to open the new version.
```
Other way for update Cypres:
```
open in app in VSC file: 
package.json
find line with:
"cypress": "^4.12.1"    >>> change version for available version
"cypress": "^5.0.0"
Open Terminal:
$ npm install            >>> after the process finish next command
$ npx cypress open       >>> we will to see new updated version, in Changelog we can see all changing in new version(new features, bugs fixed)
                             this can be usefull information
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

How to find Web Elements:

```

    it.only('second test', () => {

        cy.visit('/')
        cy.contains('Forms').click()
        cy.contains('Form Layouts').click()

        cy.get('[data-cy="signInButton"]')
        cy.contains('Sign in')
        cy.contains('[status="primary"]', 'Sign in')

        cy.get('#inputEmail3')
            .parents('form')
            .find('button')
            .should('contain', 'Sign in')
            .parents('form')
            .find('nb-checkbox')
            .click()

        cy.contains('nb-card', 'Horizontal form').find('[type="email"]')


    })

})
```
How to save some methods(then, wrap) and use it later:

```
//This is Cypress style >>>

        //cy.contains('nb-card', 'Using the Grid').find('[for="inputEmail1"]').should('contain', 'Email')
        //cy.contains('nb-card', 'Using the Grid').find('[for="inputPassword2"]').should('contain', 'Password')

        //cy.contains('nb-card', 'Basic form').find('[for="exampleInputEmail1"]').should('contain', 'Email address')
        //cy.contains('nb-card', 'Basic form').find('[for="exampleInputPassword1"]').should('contain', 'Password')
        
        // This is Jake Query style (JQuery)//

        cy.contains('nb-card', 'Using the Grid').then( firstForm => {
            const EmailLabelFirst = firstForm.find('[for="inputEmail1"]').text()
            const PasswordLabelFirst = firstForm.find('[for="inputPassword2"]').text()
            expect(EmailLabelFirst).to.equal('Email')
            expect(PasswordLabelFirst).to.equal('Password')

            cy.contains('nb-card', 'Basic form').then( secondForm => {
                const PasswordSecondText = secondForm.find('[for="exampleInputPassword1"]').text()
                expect(PasswordLabelFirst).to.equal(PasswordSecondText)

                cy.wrap(secondForm).find('[for="exampleInputPassword1"]').should('contain', 'Password')        >>> Cypress style

            })
