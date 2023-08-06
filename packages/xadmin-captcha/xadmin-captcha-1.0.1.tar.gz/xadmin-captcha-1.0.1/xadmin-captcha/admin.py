from xadmin.sites import AdminSite
from multi_captcha_admin.forms import MultiCaptchaAdminAuthenticationForm

AdminSite.login_view = MultiCaptchaAdminAuthenticationForm
