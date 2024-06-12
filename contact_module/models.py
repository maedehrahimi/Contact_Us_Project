from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
import django_jalali.db.models as jmodels


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    phone = models.CharField(
        verbose_name='شماره تماس',
        max_length=13,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(14),
            RegexValidator(
                regex=r'^(?:\+98|0)?9\d{9}$',
                message='شماره تلفن وارد شده معتبر نیست. لطفاً یک شماره تلفن معتبر ایران وارد کنید.'
            )
        ]
    )
    message = models.TextField(null=True, blank=True, verbose_name='متن تماس با ما')
    timestamp = jmodels.jDateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    description = models.TextField(null=True, blank=True, verbose_name='پاسخ تماس با ما')
    is_called = models.BooleanField(default=False, verbose_name='تماس گرفته شده/نشده')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.full_name
