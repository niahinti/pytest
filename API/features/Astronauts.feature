Feature: Astronauts

  Background:
    Given The url to get astronaut information is "http://api.open-notify.org/astros.json"

  Scenario Outline: Verify astronaut is not on the ISS
    When I send a GET request
    Then I should get a status code "200"
    And Name "<name>" should not be on the "<station>" station

    Examples:
      | name             | station  |
      | Andreas Mogensen | Tiangong |
      | Megan McArthur   | ISS      |