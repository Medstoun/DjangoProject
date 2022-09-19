from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

MIN_USER_AGE = 9
FORBIDDEN_DOMENS = ['rambler.ru']


def check_birth_date(value):
    diff = relativedelta(date.today(), value).years
    if diff < MIN_USER_AGE:
        raise ValidationError(f"{diff} is so small")


def check_email_adress(value):
    mail_domen = value.split('@')[-1]
    if mail_domen in FORBIDDEN_DOMENS:
        raise ValidationError(f"{mail_domen} error")


