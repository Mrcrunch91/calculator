Feature: calculator
    Scenario: Get the hello message
        Given I request a message
        When the application gets the message
        Then I receive "Hello NateDogg, Spring Boot Here!" as a message