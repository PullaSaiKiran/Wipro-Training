Feature: Admin User Search
  As an Admin
  I want to filter users based on specific criteria
  So that I can quickly find existing users

  Background:
    Given I am logged into OrangeHRM with username "Admin" and password "admin123"
    And I navigate to the Admin module


  Scenario: Search for users with multiple criteria
    When I search for users with the following parameters:
      | Username | UserRole | Status   |
      | Admin    | Admin    | Enabled  |
    Then I should see the search results containing "Admin"
