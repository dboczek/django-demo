from django.conf import settings
# Password your users have to provide to access demo project
ACCESS_PASSWORD = getattr(settings, 'DEMO_ACCESS_PASSWORD', 'demo')
# You don't have to remove middleware on production just set DEMO_REQUIRE_PASSWORD to False
REQUIRE_PASSWORD = getattr(settings, 'DEMO_REQUIRE_PASSWORD', True)
# Change it if you want to use other url to avoid confusion with your urls.
# Note that you dont add any urls to your urls.py to make demo login work
LOGIN_URL = getattr(settings, 'DEMO_LOGIN_URL', '/demo-login/')
# Change if you already use this name elsewhere
COOKIE_NAME = getattr(settings, 'DEMO_COOKIE_NAME', 'demo_session')
# Choose from META keys available in META of Django's HttpRequest object.
# This make unauthorized use of cookie much harder.
SALT_REQUEST_META_KEYS = getattr(
    settings, 'DEMO_SALT_REQUEST_META_KEYS', ['REMOTE_ADDR', 'HTTP_USER_AGENT'])
UNPROTECTED_PATHS = getattr(settings, 'DEMO_UNPROTECTED_PATHS', [])
