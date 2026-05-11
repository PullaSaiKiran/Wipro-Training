Feature: Admin Search
  Scenario: Search with multiple criteria
    When I enter the following search criteria:
      | Field     | Value   |
      | Username  | Admin   |
      | User Role | Admin   |
      | Status    | Enabled |
    Then Search results should be displayed

