# ساخت سیگنال سفارشی

ایجاد سیگنال های سفارشی در جنگو به شما امکان می دهد رویدادهای خاصی را تعریف کنید که برنامه شما می تواند به آنها پاسخ دهد

1- تعریف سگنال سفارشی:

داخل فایل پروژه و اپی که میخواهید سگینال در آن اجرا شود فایل singals.py را ایجاد کنید و مدل Singal را فراخوانی میکنیم سیگنال سفارشی خود را از آن میسازیم

```python
# singals.py

from django.dispatch import Signal

name_of_custom_signal = Signal()
```
2- ایجاد گیرنده ها

توابعی را تعریف میکنیم که به عنوان گیرنده 
سیگنال‌های سفارشی عمل می‌کنند. 

```python
from django.dispatch import Signal, receiver
name_of_custom_signal = Signal()

@receiver(name_of_custom_signal)
def handle_custom_signal(sender, **kwargs):
  ...
  # Custom Logic
```
سپس سیگنال را داخل app ریجیستر میکنیم

```python
# apps.py

class YourAppConfig(AppConfig): 
    name = 'your_app' 


    def ready(self): 
        import your_app.signals
        super().ready()
```

3- فعال سازی سگینال:

سیگنال میتواند از داخل ویو یا هر جایی دیگر کد فرستاده شود
برای فرستادن سیگنال از متد send() استفاده میکنیم و sender و آرگومان هایی که لازم است را میفرسیتم

```python
# views

def your_view(request):
  # view login
  name_of_custom_signal(sender=your_model_instance, arg1=value1, arg2=value2)
```


