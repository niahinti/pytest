import requests


class ApiRequests:

    def __init__(self, response):
        self.response = response

    def sendGetRequest(self, url):
        resp = requests.get(url)
        self.response['status_code'] = resp.status_code
        self.response['data'] = resp.json()
        return resp
