from demoapp import app_settings
from demoapp.views import login_view
from django.shortcuts import redirect
from demoapp.utils import get_salt


class PasswordMiddleware(object):
    def process_request(self, request):
        if request.path in app_settings.UNPROTECTED_PATHS:
            return None
        if not app_settings.REQUIRE_PASSWORD or \
                request.get_signed_cookie(app_settings.COOKIE_NAME, default=False, salt=get_salt(request)):
            if request.path == app_settings.LOGIN_URL:
                return redirect('/')
            return None
        if request.path == app_settings.LOGIN_URL:
            return login_view(request)
        return redirect(app_settings.LOGIN_URL)
