from pytest_bdd import *
from pytest_bdd import parsers
import requests
from pytest_bdd import scenarios, given, when, then, parsers
from conftest import global_state, response


@scenario("../features/Astronauts.feature", "Verify astronaut is not on the ISS")
def test_setUp(global_state, response):
    pass


@given(parsers.parse("The url to get austronaut information is \"{url}\""))
def set_api_url(global_state, url):
    global_state['api_url'] = url


@when(parsers.parse("I send a GET request"))
def send_get_request(global_state, response):
    resp = requests.get(global_state['api_url'])
    response['status_code'] = resp.status_code
    response['data'] = resp.json()


@then(parsers.parse("I should get a status code \"{code}\""))
def check_status_code(response, code):
    assert response['status_code'] == int(code)


@then(parsers.parse("Name \"{name}\" should not be on the \"{station}\" station"))
def verify_astronaut_not_on_station(response, name, station):
    astronauts = response['data']['people']
    astronauts.sort(key=lambda x: x['name'].split()[-1])
    for astronaut in astronauts:
        print(astronaut)
        if astronaut['name'] == name and astronaut['craft'] == station:
            pytest.fail(f"{name} is on the {station} station")
