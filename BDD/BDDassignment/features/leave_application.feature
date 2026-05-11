Feature: Leave Application Workflow
  As an employee
  I want to apply for medical leave
  So that my manager can approve it

  Background:
    Given I am logged into OrangeHRM with username "Admin" and password "admin123"
    And I navigate to the Leave module

  Scenario: Apply for Medical Leave and verify status
    When I apply for "Medical Leave" from "2026-05-10" to "2026-05-12"
    Then I should see a success toast message "Successfully Saved"
    And my leave balance should be reduced
    And the leave status should be "Pending Approval"
