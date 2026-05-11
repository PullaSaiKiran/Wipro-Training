Feature: Employee Management (PIM Module)
  As an HR user
  I want to add new employees in the PIM module
  So that their records are stored in the system

  Background:
    Given I am logged into OrangeHRM with username "Admin" and password "admin123"
    And I navigate to the PIM module
    And I click on "Add Employee"

  Scenario Outline: Add a new employee with unique details
    When I enter First Name "<FirstName>"
    And I enter Last Name "<LastName>"
    And I click the Save button
    Then I should see the employee profile page for "<FirstName>" "<LastName>"

    Examples:
      | FirstName | LastName  |
      | John      | Doe       |
      | Alice     | Smith     |
      | Raj       | Kumar     |
