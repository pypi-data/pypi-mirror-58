from __future__ import absolute_import, print_function

from django.conf import settings

AUTHSCH_CLIENT_ID = getattr(settings, 'AUTHSCH_CLIENT_ID', None)
AUTHSCH_CLIENT_SECRET = getattr(settings, 'AUTHSCH_CLIENT_SECRET', None)

SCOPE = "basic displayName mail admembership linkedAccounts eduPersonEntitlement"
AUTHORIZE_URL = getattr(settings, 'AUTHSCH_AUTHORIZE_URL', "https://auth.sch.bme.hu/site/login")
ACCESS_TOKEN_URL = getattr(settings, 'ACCESS_TOKEN_URL', "https://auth.sch.bme.hu/oauth2/token")
PROFILE_ENDPOINT = getattr(settings, 'PROFILE_ENDPOINT', "https://auth.sch.bme.hu/api/profile/")

ERR_INVALID_RESPONSE = "Unable to fetch user information from AuthSCH.  Please check the log."

DATA_VERSION = "1"
