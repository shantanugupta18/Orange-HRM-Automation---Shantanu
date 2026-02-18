Feature: ESS Login

  Scenario Outline: ESS login validation
    Given the user is on the login page
    When the user logs in with "<username>" and "<password>"
    Then "<result>" should be displayed

    Examples:
      | TC_ID         | username | password     | result              |
      | TC_MyInfo_001 | Test     | test@12345   | MyInfo page visible |
      | TC_MyInfo_002 | Test     | xxxxxx       | Invalid credentials |
      | TC_MyInfo_003 | xxxxxxxx | test@12345   | Invalid credentials |
      | TC_MyInfo_004 | xxxxxxxx | xxxxxx       | Invalid credentials |