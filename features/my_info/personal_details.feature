Feature: Personal Details

  Background:
    Given the user is logged in with valid ESS credentials
    And the user navigates to My Info

  Scenario: View Personal Details (TC_MyInfo_005)
    When the user opens "Personal Details" section
    Then the page header should be "Personal Details"

  Scenario: Edit Personal Details (TC_MyInfo_006)
    When the user edits allowed personal details
    Then changes should be saved successfully

  Scenario: Restricted fields in Personal Details (TC_MyInfo_007)
    When the user opens "Personal Details" section
    Then restricted fields should be non-editable