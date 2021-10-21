import requests
import http.client
import json

class MagicBall:

    def __init__(self, api_url):
        self.api_url = api_url
        # url = https://yesno.wtf/api

    def __self__(self):
        return (str(self.api_url))

    def get(self):
        self.result = requests.get(self.api_url)


    def response(self):
        response = self.result.json()

    def answer(self):
        return self.result.json()['answer']
