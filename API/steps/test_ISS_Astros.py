from pytest_bdd import *
from pytest_bdd import parsers
import requests
from pytest_bdd import scenarios, given, when, then, parsers
from conftest import global_state, response

@scenario("../features/Astronauts.feature", "Verify astronaut is not on the ISS")

def test_setUpAstros(global_state, response):
    pass


@given(parsers.parse("The url to get astronaut information is \"{url}\""))
def set_api_url(global_state, url):
    global_state['api_url'] = url


@when(parsers.parse("I send a GET request"))
def send_get_request(global_state, response):
    resp = requests.get(global_state['api_url'])
    response['status_code'] = resp.status_code
    response['data'] = resp.json()


@then(parsers.parse("I should get a status code \"200\""))
def check_status_code(response):
    assert response['status_code'] == 200


@then(parsers.parse("Name <name> should not be on the <station> station"))
def verify_astronaut_not_on_station(response, name, station):
    astronauts = response['data']['people']
    for astronaut in astronauts:
        if astronaut['name'] == name and astronaut['craft'] == station:
            pytest.fail(f"{name} is on the {station} station")
