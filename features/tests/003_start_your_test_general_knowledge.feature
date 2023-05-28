# Created by rapid at 05 apr 2023
Feature: # 003_start_your_test_general_knowledge

  Scenario: # 003_start_your_test_general_knowledge
    Given Loginpage
    Then Login with the right credentials
    Then Verify 1 "General knowledge (BASIC CDL KNOWLEDGE) (continue)" button text is here
    Then Verify 2 "Air brakes" button text is here
    Then Verify 3 "Combination vehicle" button text is here
    Then Verify 4 "ELDT Hazmat endorsement" button text is here
    And Verify "© 2023. All rights reserved." text is here