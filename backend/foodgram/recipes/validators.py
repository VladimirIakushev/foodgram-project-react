from django.core.validators import MinValueValidator
from api.exeptions import MyError


class CustomMinValueIntValidator(MinValueValidator):

    def validate_even(self, value):
        if int(value) != value:
            raise MyError('Введите целое, положительное число')
