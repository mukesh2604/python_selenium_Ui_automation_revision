import requests

class ApiClient:

    def __init__(self, api_url):
        self.api_url = api_url

    def get(self, endpoints):
        response = requests.get(f"{self.api_url}/{endpoints}")
        return response

    def post(self, payload, endpoints):
        response = requests.post(f"{self.api_url}/{endpoints}", json=payload)
        return response

    def put(self, payload, endpoints):
        response = requests.put(f"{self.api_url}/{endpoints}", json=payload)
        return response

    def delete(self, endpoints):
        response = requests.delete(f"{self.api_url}/{endpoints}")
        return response