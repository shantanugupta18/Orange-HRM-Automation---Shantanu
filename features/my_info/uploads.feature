Feature: Photograph & Attachment Uploads

  Background:
    Given the user is logged in with valid ESS credentials
    And the user navigates to My Info

  Scenario Outline: Upload validation
    When the user uploads "<file>"
    Then "<outcome>" should be shown

    Examples:
      | TC_ID           | file           | outcome             |
      | TC_MyInfo_008.1 | photo_1mb.jpg  | Upload successful   |
      | TC_MyInfo_008.3 | photo_big.jpg  | Validation failed   |
      | TC_MyInfo_042.1 | doc_small.pdf  | Upload successful   |
      | TC_MyInfo_042.3 | doc_big.pdf    | Validation failed   |