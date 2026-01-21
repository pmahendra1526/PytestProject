
Feature: Bank Transaction
        Tests pertaining to banking transaction like withdrawal, deposit

    Scenario: Withdrawal of Money
        Given The account balance is 100
        When The account holder withdraw 30
        Then The account balance should be 70

    Scenario: Deposit Money
        Given The account balance is 100
        When The account holder deposit 50
        Then The account balance should be 150

    Scenario: Removal of Items from set
        Given A set of 3 fruits
        When Remove a fruit from a set
        Then The set will have two fruits


