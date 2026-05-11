Feature: Leave Application Workflow

  Scenario: Apply one day leave
    When I apply for one day leave
    Then I should see a success message for profile update
    And My leave balance should be reduced by one
