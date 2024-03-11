Feature: Automation Exercise E-commerce App
  Scenario: New account
    Given Launch Browser
    And Navigate to url
    And Enter UserID and Password
    When Click on Login button
    Then Verify Manager id
    Then click on New Account button
    When enter on customer id
    Then Select account type
    And Enter the initial deposit
    Then Click on new account submit button
