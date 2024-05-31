import requests


class ApiValidations:
    def __init__(self, response):
        self.response = response

    def validateStatusCode(self, code):
        assert self.response['status_code'] == code

    def validateData(self, data):
        assert self.response['data'] == data

    def validateAstronautNotOnStation(self, response, name, station):
        astronauts = response['data']['people']
        astronauts.sort(key=lambda x: x['name'].split()[-1])
        for astronaut in astronauts:
            print(astronaut)
            if astronaut['name'] == name and astronaut['craft'] == station:
                pytest.fail(f"{name} is on the {station} station")
