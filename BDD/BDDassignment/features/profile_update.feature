@Smoke @Regression
Feature: Profile Update
  As an employee
  I want to update my personal details in the My Info section
  So that my profile reflects the latest information

  Background:
    Given I am logged into OrangeHRM with username "Admin" and password "admin123"
    And I navigate to the My Info section

  Scenario: Update Nick Name and upload profile photograph
    When I change my Nick Name to "Sai"
    And I upload a profile photograph "C:/Users/YourPath/profile.jpg"
    Then I should see a success toast message "Successfully Updated"
    And my profile should display the new Nick Name "Sai"
    And my profile picture should be updated
