import re
from django.utils.translation import gettext_lazy as _


def phone_validator(phone):
    """Validation Iranian phone number for all operators"""
    pattern = r'((0?9)|(\+?989))((14)|(13)|(12)|(19)|(18)|(17)|(15)|(16)|(11)|(10)|(90)|(91)|(92)|(93)|(94)|(95)|(96)|(32)|(30)|(33)|(35)|(36)|(37)|(38)|(39)|(00)|(01)|(02)|(03)|(04)|(05)|(41)|(20)|(21)|(22)|(23)|(31)|(34)|(9910)|(9911)|(9913)|(9914)|(9999)|(999)|(990)|(9810)|(9811)|(9812)|(9813)|(9814)|(9815)|(9816)|(9817)|(998))\W?\d{3}\W?\d{4}$'
    if re.match(pattern, phone):
        return True
    raise ValueError(_('Phone Number is not valid.'))



def national_code_validator(code):
    """Validation Iranian national code"""

    pattern = r"^\d{10}$"
    if re.match(pattern, code):
        check = int(code[9])
        sum = 0
        for i in range(9):
            sum += int(code[i]) * (10 - i)

        if re.match(r"^[0-6]", str(sum % 11)) and check == sum % 11 or re.match(r"^[7-9]", str(sum % 11)) and check == 11 - (sum % 11):
            return code

    raise ValueError(_('National code is not correct.'))



def name_validator(name):
    pattern = r'^[a-zA-Z]+$'

    if re.match((pattern, name)):
        return True

    raise ValueError(_('Please enter a valid name'))
