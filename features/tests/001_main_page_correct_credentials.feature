# Created by rapid at 06 apr 2023
Feature: # 001_main_page_correct_credentials

  Scenario: # 001_main_page_correct_credentials
    Given Loginpage
    Then Verify text 1 "Please sign in" is here
    Then Send correct login "gurovvic@gmail.com"
    Then Send correct password "QWERTY_GUROV"
    Then Click on "Sign in" button
    Then Verify text 2 "Start your test" is here
    And Verify username "gurovvic@gmail.com" is here

