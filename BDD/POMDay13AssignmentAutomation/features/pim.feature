Feature: Employee Creation

  Scenario Outline: Add new employee
    When I enter "<FirstName>" and "<LastName>"
    Then Employee should be created successfully

    Examples:
      | FirstName | LastName  |
      | Linda     | Anderson  |
      | John      | Smith     |
      | Priya     | Reddy     |
