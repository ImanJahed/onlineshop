import requests
import json


class PayClient:

    _payment_request_url = "https://pay.ir/pg/send"
    _payment_page_url = "https://pay.ir/pg/{}/"
    _payment_verify_url = 'https://pay.ir/pg/verify'
    _redirect_url = 'http://127.0.0.1:8000/' # Your url for redirect after operation

    _headers = {"Content-Type": "application/json"}

    def __init__(self, api_key):
        self._api_key = api_key


    def payment_request(self, amount, mobile=None, description=None):
        payload = json.dumps({
            'api': self._api_key,
            'amount': amount,
            'redirect': self._redirect_url
        })

        response = requests.post(self._payment_request_url, headers=self._headers, data=payload)

        return response.json() #Response {"status": 1, "token": "توکن پرداخت"}


    def payment_verify(self,api, token):
        payload = json.dumps({
            'api': api,
            'token': token
        })

        response = requests.post(self._payment_verify_url, headers=self._headers, data=payload)

        return response.json()
        #Response = {
        #     "status": 1,
        #     "amount": "مبلغ تراکنش",
        #     "transId": "شماره تراکنش",
        #     "factorNumber": "شماره فاکتور",
        #     "mobile": "شماره موبایل",
        #     "description": "توضیحات",
        #     "cardNumber": "شماره کارت",
        #     "message": "OK",
        # }


    def generate_payment_url(self, token):
        return self._payment_page_url.format(token)
    

if __name__ == '__main__':
    # On Windows, CMD

    pay = PayClient("test")
    
    response = pay.payment_request(15000)
    print(response)

    input('generating payment url?')
    print(pay.generate_payment_url(response['token']))

    # Redirect:==> http://127.0.0.1:8000/?status=1&token=dJiTppY /// https://Your-CallBack-URL?status={transaction_status}&token={token}

    input('check the payment...')
    print(pay.payment_verify(15000, response['token']))


# {
# '0':'درحال حاضر درگاه بانکی قطع شده و مشکل بزودی برطرف می شود',
# '-1':'API Key ارسال نمی شود',
# '-2':'Token ارسال نمی شود',
# '-3':'API Key ارسال شده اشتباه است',
# '-4':'امکان انجام تراکنش برای این پذیرنده وجود ندارد',
# '-5':'تراکنش با خطا مواجه شده است',
# '-6':'تراکنش تکراریست یا قبلا انجام شده',
# '-7':'مقدار Token ارسالی اشتباه است',
# '-8':'شماره تراکنش ارسالی اشتباه است',
# '-9':'زمان مجاز برای انجام تراکنش تمام شده',
# '-10':'مبلغ تراکنش ارسال نمی شود',
# '-11':'مبلغ تراکنش باید به صورت عددی و با کاراکترهای لاتین باشد',
# '-12':'مبلغ تراکنش می بایست عددی بین 10,000 و 500,000,000 ریال باشد',
# '-13':'مقدار آدرس بازگشتی ارسال نمی شود',
# '-14':'آدرس بازگشتی ارسالی با آدرس درگاه ثبت شده در شبکه پرداخت پی یکسان نیست',
# '-15':'امکان وریفای وجود ندارد. این تراکنش پرداخت نشده است',
# '-16':'یک یا چند شماره موبایل از اطلاعات پذیرندگان ارسال شده اشتباه است',
# '-17':'میزان سهم ارسالی باید بصورت عددی و بین 1 تا 100 باشد',
# '-18':'فرمت پذیرندگان صحیح نمی باشد',
# '-19':'هر پذیرنده فقط یک سهم میتواند داشته باشد',
# '-20':'مجموع سهم پذیرنده ها باید 100 درصد باشد',
# '-21':'Reseller ID ارسالی اشتباه است',
# '-22':'فرمت یا طول مقادیر ارسالی به درگاه اشتباه است',
# '-23':'سوییچ PSP ( درگاه بانک ) قادر به پردازش درخواست نیست. لطفا لحظاتی بعد مجددا تلاش کنید',
# '-24':'شماره کارت باید بصورت 16 رقمی، لاتین و چسبیده بهم باشد',
# '-25':'امکان استفاده از سرویس در کشور مبدا شما وجود نداره',
# '-26':'امکان انجام تراکنش برای این درگاه وجود ندارد',
# '-27':'در انتظار تایید درگاه توسط شاپرک',
# '-28':'امکان تسهیم تراکنش برای این درگاه وجود ندارد',
# }