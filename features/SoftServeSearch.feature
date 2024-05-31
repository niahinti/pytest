Feature: SoftServeSearch

  Scenario: Search for Academy Page
    Given Im on SoftSearch main page with title "SoftServe | Software Development & Digital Services Company"
    When I click on the search icon
    And I type "Academy" in the search box in Search Page
    And I click on "IT Academy" search result in Search Page
    Then I should see "SoftServe Academy" page title
    Then I should see "Empowering learning solutions to start your career in IT." subtitle on SoftServe Academy page