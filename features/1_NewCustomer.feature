Feature: Automation Exercise E-commerce App
  Scenario: Register User
    Given Launch Browser
    And Navigate to url
    And Enter UserID and Password
    When Click on Login button
    Then Verify Manager id
    When Click on New Customer
    Then Fill Details
    Then Click on Submit button
