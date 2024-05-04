import sys
import os
import requests
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

import django

django.setup()



from django.conf import settings



if settings.SANDBOX:
    sandbox = "sandbox"
else:
    sandbox = "www"


class ZarinPalSandBox:
    _payment_request_url = (
        f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
    )
    _payment_verify_url = (
        f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
    )
    _payment_page_url = f"https://{sandbox}.zarinpal.com/pg/StartPay/"
    _callback_url = "http://redreseller.com/verify"

    def __init__(self, merchant_id='settings.MERCHANT'):
        self.merchant_id = merchant_id

    def payment_request(self, amount, callback_url=_callback_url, description='پرداختی کاربر'):

        payload = json.dumps(
            {
                "MerchantID": self.merchant_id,
                "Amount": amount,
                'CallbackURL' : self._callback_url,
                "Description": description
            }
        )

        headers = {"Content-Type": "application/json"}

        response = requests.post(
            self._payment_request_url, headers=headers, data=payload
        )

        return response.json()

    def payment_verify(self, amount, authority):
        payload = json.dumps({
            "MerchantID": self.merchant_id,
            "Amount": amount,
            "Authority": authority
            })
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(self._payment_verify_url, headers=headers, data=payload)

        return response.json()

    def generate_payment_url(self, authority):
        return f'{self._payment_page_url}{authority}'
    

if __name__ == '__main__':
    # On Windows, CMD

    zarinpal = ZarinPalSandBox("4ced0a1e-4ad8-4309-9668-3ea3ae8e8897")
    
    response = zarinpal.payment_request(15000)
    print(response)
    input('generating payment url?')
    print(zarinpal.generate_payment_url(response['Authority']))


    input('check the payment...')
    print(zarinpal.payment_verify(15000, response['Authority']))