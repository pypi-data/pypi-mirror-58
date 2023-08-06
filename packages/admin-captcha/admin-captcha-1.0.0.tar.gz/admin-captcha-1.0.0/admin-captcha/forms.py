from django.contrib.admin.forms import AdminAuthenticationForm


def get_captcha_field():
    from captcha.fields import CaptchaField
    return CaptchaField()


class MultiCaptchaAdminAuthenticationForm(AdminAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MultiCaptchaAdminAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['captcha'] = get_captcha_field()
