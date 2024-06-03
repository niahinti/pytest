from pytest_bdd import *
from pytest_bdd import parsers
import requests
from pytest_bdd import scenarios, given, when, then, parsers
from conftest import global_state, response
from API.apiRequests.apiRequests import ApiRequests as api
from API.apiRequests.apiValidations import ApiValidations as validate


@scenario("../features/Astronauts.feature", "Verify astronaut is not on the ISS")
def test_setUp(global_state, response):
    pass


@given(parsers.parse("The url to get astronaut information is \"{url}\""))
def set_api_url(global_state, url):
    global_state['api_url'] = url


@when(parsers.parse("I send a GET request"))
def send_get_request(global_state, response):
    api(response).sendGetRequest(global_state['api_url'])


@then(parsers.parse("I should get a status code \"{code:d}\""))
def check_status_code(response, code):
    validate(response).validateStatusCode(code)


@then(parsers.parse("Name \"{name}\" should not be on the \"{station}\" station"))
def verify_astronaut_not_on_station(response, name, station):
    validate(response).validateAstronautNotOnStation(response, name, station)
