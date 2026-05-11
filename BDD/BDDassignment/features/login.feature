Feature: User Authentication (Login Feature)
  As a valid OrangeHRM user
  I want to log into the system
  So that I can access the dashboard

  Background:
    Given I am on the OrangeHRM login page

  Scenario: Successful login with valid credentials
    When I enter username "Admin"
    And I enter password "admin123"
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see "Dashboard" on the page

  Scenario: Unsuccessful login with invalid password
    When I enter username "Admin"
    And I enter password "wrongPassword"
    And I click the login button
    Then I should see an error message containing "Invalid credentials"
