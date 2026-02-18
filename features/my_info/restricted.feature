Feature: Restricted Sections

  Background:
    Given the user is logged in with valid ESS credentials
    And the user navigates to My Info

  Scenario Outline: Read-only validation
    When the user opens "<section>" section
    Then all fields should be non-editable

    Examples:
      | TC_ID         | section  |
      | TC_MyInfo_023 | Job      |
      | TC_MyInfo_024 | Salary   |
      | TC_MyInfo_026 | Report To|