Feature: Astronauts

  Background:
    Given The url to get austronaut information is "http://api.open-notify.org/astros.json"

  Scenario Outline: Verify astronaut is not on the ISS
    When I send a GET request
    Then I should get a status code "200"
    And Name "<name>" should not be on the "<station>" station

    Examples:
      | name             | station  |
      | Andreas Mogensen | Tiangong |
      | Megan McArthur   | ISS      |


  Scenario: Verify how many astronauts are on the ISS
    When I send a GET request
    Then I should get a status code "200"
    And There should be more than "3" people on the ISS
