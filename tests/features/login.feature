@login @regression
Feature: Orange HRM Login Functionality
  Background:
    Given user navigates to Orange HRM Login page

  @TES-0001 @smoke
  Scenario: Verify user can login with valid credentials
    Given user enters username as Admin
    When user enters password as admin123
    And user clicks the login button
    Then user is navigated to dashboard

  @TES-0002 @smoke
  Scenario: Verify user can log out
    Given user enters username as Admin
    When user enters password as admin123
    And user clicks the login button
    When user is navigated to dashboard