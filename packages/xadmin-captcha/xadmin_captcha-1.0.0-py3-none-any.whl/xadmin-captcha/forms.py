from django.conf import settings
from xadmin.forms import AdminAuthenticationForm

def get_captcha_field():
    engine = settings.MULTI_CAPTCHA_ADMIN['engine']

    if engine == 'simple-captcha':
        from captcha.fields import CaptchaField
        return CaptchaField()


class MultiCaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MultiCaptchaAdminAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = get_captcha_field()
