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


if __name__ == '__main__':
    next_pay = NextPay('test')

    response = next_pay.payment_request(amount=1000, order_id='85NX85s427')   # ==> response {'code': -1, 'trans_id:'f7c07568-c6d1-4bee-87b1-4a9e5ed2e4c1'}
    '''* نکته : اگر پارامتر code در پاسخ دارای مقدار 1- باشد، یعنی توکن با موفقیت صادر شده است و trans_id همان توکن مورد نیاز برای مراحل بعدی است.'''

    input('generating payment url?')
    print(next_pay.generate_payment_url(response['trans_id']))

    # Redirect:==> http://127.0.0.1:8000/?trans_id=f7c07568-c6d1-4bee-87b1-4a9e5ed2e4c1&order_id=85NX85s427&amount=1000 /// https://Your-CallBack-URL?trans_id={transaction_id}&order_id={order_id}&amount={amount}

    input('check the payment...')
    print(next_pay.payment_verify(1000, response['trans_id']))
    '''* نکته : اگر پارامتر code در پاسخ دارای مقدار 0 باشد، یعنی تراکنش (( موفق )) بوده است . هر مقداری غیر از صفر به معنی ناموفق بودن تراکنش است.'''



#  کد های وضعیت و خطا

# در هنگام کار با وب سرویس ، هر درخواستی که ارسال میکنید ، در پاسخ یک کد دریافت میکنید که این کد نشان دهنده وضعیت یا خطای مربوطه است . لیست این کد ها و مفهوم آنها در زیر آمده است :

# کد	توضیح
# 0	پرداخت تکمیل و با موفقیت انجام شده است
# -1	منتظر ارسال تراکنش و ادامه پرداخت
# -2	پرداخت رد شده توسط کاربر یا بانک
# -3	پرداخت در حال انتظار جواب بانک
# -4	پرداخت لغو شده است
# -20	کد api_key ارسال نشده است
# -21	کد trans_id ارسال نشده است
# -22	مبلغ ارسال نشده
# -23	لینک ارسال نشده
# -24	مبلغ صحیح نیست
# -25	تراکنش قبلا انجام و قابل ارسال نیست
# -26	مقدار توکن ارسال نشده است
# -27	شماره سفارش صحیح نیست
# -28	مقدار فیلد سفارشی [custom_json_fields] از نوع json نیست
# -29	کد بازگشت مبلغ صحیح نیست
# -30	مبلغ کمتر از حداقل پرداختی است
# -31	صندوق کاربری موجود نیست
# -32	مسیر بازگشت صحیح نیست
# -33	کلید مجوز دهی صحیح نیست
# -34	کد تراکنش صحیح نیست
# -35	ساختار کلید مجوز دهی صحیح نیست
# -36	شماره سفارش ارسال نشد است
# -37	شماره تراکنش یافت نشد
# -38	توکن ارسالی موجود نیست
# -39	کلید مجوز دهی موجود نیست
# -40	کلید مجوزدهی مسدود شده است
# -41	خطا در دریافت پارامتر، شماره شناسایی صحت اعتبار که از بانک ارسال شده موجود نیست
# -42	سیستم پرداخت دچار مشکل شده است
# -43	درگاه پرداختی برای انجام درخواست یافت نشد
# -44	پاسخ دریاف شده از بانک نامعتبر است
# -45	سیستم پرداخت غیر فعال است
# -46	درخواست نامعتبر
# -47	کلید مجوز دهی یافت نشد [حذف شده]
# -48	نرخ کمیسیون تعیین نشده است
# -49	تراکنش مورد نظر تکراریست
# -50	حساب کاربری برای صندوق مالی یافت نشد
# -51	شناسه کاربری یافت نشد
# -52	حساب کاربری تایید نشده است
# -60	ایمیل صحیح نیست
# -61	کد ملی صحیح نیست
# -62	کد پستی صحیح نیست
# -63	آدرس پستی صحیح نیست و یا بیش از ۱۵۰ کارکتر است
# -64	توضیحات صحیح نیست و یا بیش از ۱۵۰ کارکتر است
# -65	نام و نام خانوادگی صحیح نیست و یا بیش از ۳۵ کاکتر است
# -66	تلفن صحیح نیست
# -67	نام کاربری صحیح نیست یا بیش از ۳۰ کارکتر است
# -68	نام محصول صحیح نیست و یا بیش از ۳۰ کارکتر است
# -69	آدرس ارسالی برای بازگشت موفق صحیح نیست و یا بیش از ۱۰۰ کارکتر است
# -70	آدرس ارسالی برای بازگشت ناموفق صحیح نیست و یا بیش از ۱۰۰ کارکتر است
# -71	موبایل صحیح نیست
# -72	بانک پاسخگو نبوده است لطفا با نکست پی تماس بگیرید
# -73	مسیر بازگشت دارای خطا میباشد یا بسیار طولانیست
# -90	بازگشت مبلغ بدرستی انجام شد
# -91	عملیات ناموفق در بازگشت مبلغ
# -92	در عملیات بازگشت مبلغ خطا رخ داده است
# -93	موجودی صندوق کاربری برای بازگشت مبلغ کافی نیست
# -94	کلید بازگشت مبلغ یافت نشد