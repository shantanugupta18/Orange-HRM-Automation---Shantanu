Feature: My Info smoke coverage

  Scenario Outline: Validate MyInfo flows
    Given the user is logged in with valid ESS credentials
    When the user navigates to My Info section
    Then the requested section should be visible

    Examples:
      | TC_ID |
      | TC_MyInfo_001 |
      | TC_MyInfo_005 |
      | TC_MyInfo_009 |
      | TC_MyInfo_025 |
