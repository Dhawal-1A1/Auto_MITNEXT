Feature: Automation Exercise E-commerce App
  Scenario: Withdrawal
    Given Launch Browser
    And Navigate to url
    And Enter UserID and Password
    When Click on Login button
    Then Verify Manager id
    Then Click on 'Withdrawal'
    When Enter Account Number, Amount and Description for withdrawl
    Then Click on withdrawl Submit button