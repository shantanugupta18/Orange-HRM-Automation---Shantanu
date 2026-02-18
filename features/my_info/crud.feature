Feature: CRUD Operations (Emergency, Dependants, Immigration, Qualifications, Membership)

  Background:
    Given the user is logged in with valid ESS credentials
    And the user navigates to My Info

  Scenario Outline: Add record
    When the user opens "<section>" section
    And the user adds a new record
    Then the record should appear in the table

    Examples:
      | TC_ID         | section            |
      | TC_MyInfo_011 | Emergency Contacts |
      | TC_MyInfo_015 | Dependants         |
      | TC_MyInfo_019 | Immigration        |
      | TC_MyInfo_027 | Qualifications     |
      | TC_MyInfo_045 | Membership         |

  Scenario Outline: Delete record
    When the user opens "<section>" section
    And the user deletes a record
    Then the record should be removed from the table

    Examples:
      | TC_ID         | section            |
      | TC_MyInfo_013 | Emergency Contacts |
      | TC_MyInfo_017 | Dependants         |
      | TC_MyInfo_021 | Immigration        |
      | TC_MyInfo_029 | Qualifications     |
      | TC_MyInfo_047 | Membership         |