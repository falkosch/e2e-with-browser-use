Feature: Google Search for "LLM"

  Scenario: User searches for "LLM" on Google.de
    Given I open the browser
    And I navigate to "https://www.google.de"
    When I enter "LLM" into the search bar
    And I press "Enter"
    Then I should see search results related to "LLM"
