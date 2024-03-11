Feature: Automation Exercise E-commerce App
  Scenario: Edit account
    Given Launch Browser
    And Navigate to url
    And Enter UserID and Password
    When Click on Login button
    Then Verify Manager id
    And Click on Edit Account button
    When Enter the Account No
    Then Click on edit account submit button
