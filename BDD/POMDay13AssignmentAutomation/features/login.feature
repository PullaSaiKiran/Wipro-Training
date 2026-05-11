Feature: User Authentication

  Scenario: Valid login
    Given User is on the OrangeHRM login page
    When User enters username "Admin" and password "admin123"
    Then User should be redirected to dashboard
