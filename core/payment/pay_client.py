import requests
import json


class PayClient:

    _payment_request_url = "https://pay.ir/pg/send"
    _payment_page_url = "https://pay.ir/pg/{}"
    _payment_verify_url = 'https://pay.ir/pg/verify'

    _redirect_url = 'http://127.0.0.1:8000/' # Your url for redirect after operation

    _headers = {"Content-Type": "application/json"}

    def __init__(self, api_key):
        self._api_key = api_key


    def payment_request_url(self, amount, mobile=None, description=None):
        payload = json.dumps({
            'api': self._api_key,
            'amount': amount,
            'redirect': self._redirect_url
        })

        response = requests.post(self._payment_request_url, headers=self._headers, data=payload)

        return response.json() # Response = {"status": 1, "token": "توکن پرداخت"}

    def generate_payment_url(self, token):
        return self._payment_page_url.format(token)


    def payment_verify(self, token):
        payload = json.dumps({
            'api': self._api_key,
            'token': token
        })

        response = requests.post(self._payment_verify_url, headers=self._headers, data=payload)

        return response.json()

