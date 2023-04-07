# Created by rapid at 05 apr 2023
Feature: # 002_main_page_wrong_credentials

  Scenario: # 002_main_page_wrong_credentials
    Given Loginpage
    Then Verify text 1 "Please sign in" is here
    Then Send wrong login "WRONG@gmail.com"
    Then Send wrong password "WRONG_GUROV"
    Then Click on Sign in button
    And Verify text "Invalid Login or Password" is here