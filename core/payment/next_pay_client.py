import requests
import json


class NextPay:
    _payment_request_url = "https://nextpay.org/nx/gateway/token"
    _payment_page_url = "https://nextpay.org/nx/gateway/payment/{}"
    _payment_verify_url = "https://nextpay.org/nx/gateway/verify"

    _callback_uri = (
        "http://127.0.0.1:8000/verify/"  # Your url for redirect after operation
    )

    _headers = {"Content-Type": "application/json"}

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def payment_request(self, amount, order_id):
        payload = json.dumps(
            {
                "api_key": self.api_key,
                "amount": amount,
                "order_id": order_id,
                "callback_uri": self._callback_uri,
            }
        )

        response = requests.post(
            self._payment_request_url, headers=self._headers, data=payload
        )

        return response.json()

    def payment_verify(self, amount, trans_id):
        payload = json.dumps(
            {"api_key": self.api_key, "amount": amount, "trans_id": trans_id}
        )
        response = requests.post(
            self._payment_verify_url, headers=self._headers, data=payload
        )

        return response.json()

    def generate_payment_url(self, trans_id):
        return self._payment_page_url.format(trans_id)
