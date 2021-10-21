import requests

class RandomDog:
    def __init__(self, api_url):
        self.api_url = api_url
        # url = https://dog.ceo/api/breeds/image/random

    def __self__(self):
        return (str(self.api_url))

    def get(self):
        self.result = requests.get(self.api_url)

    def response(self):
        response = self.result.json()

    def answer(self):
        return self.result.json()["message"]
