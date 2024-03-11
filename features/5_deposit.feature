Feature: Automation Exercise E-commerce App
  Scenario: Deposit
    Given Launch Browser
    And Navigate to url
    And Enter UserID and Password
    When Click on Login button
    Then Verify Manager id
    And Click on Deposit
    Then Enter Account Number, Amount and Discription
    And Click on deposit submit button
