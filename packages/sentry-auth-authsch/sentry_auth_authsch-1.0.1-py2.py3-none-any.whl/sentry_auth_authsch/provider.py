from __future__ import absolute_import, print_function

from sentry.auth.providers.oauth2 import OAuth2Callback, OAuth2Provider, OAuth2Login

from .constants import ACCESS_TOKEN_URL, AUTHSCH_CLIENT_ID, AUTHSCH_CLIENT_SECRET, AUTHORIZE_URL, SCOPE
from .views import FetchUser, AuthSCHConfigureView


DATA_VERSION = "1"


class AuthSCHProvider(OAuth2Provider):
    name = "AuthSCH"
    authorize_url = AUTHORIZE_URL
    access_token_url = ACCESS_TOKEN_URL
    client_id = AUTHSCH_CLIENT_ID
    client_secret = AUTHSCH_CLIENT_SECRET
    scope = SCOPE

    def __init__(self, version=None, **config):
        self.version = version
        super(AuthSCHProvider, self).__init__(**config)

    def get_client_id(self):
        return self.client_id

    def get_client_secret(self):
        return self.client_secret

    def get_auth_pipeline(self):
        return [
            OAuth2Login(
                client_id=self.get_client_id(),
                authorize_url=self.authorize_url,
                scope=self.scope
            ),
            OAuth2Callback(
                access_token_url=self.access_token_url,
                client_id=self.get_client_id(),
                client_secret=self.get_client_secret(),
            ),
            FetchUser(
                version=self.version
            )
        ]

    def get_refresh_token_url(self):
        return self.access_token_url

    def build_identity(self, state):
        data = state["data"]
        user_data = state["user"]
        schacc = user_data["schacc"]

        return {
            "id": user_data["iid"],
            "email": user_data['schmail'],
            "email_verified": True,
            "name": user_data["full_name"],
            "nickname": schacc,
            "data": self.get_oauth_data(data),
        }

    def get_configure_view(self):
        return AuthSCHConfigureView.as_view()

    def build_config(self, state):
        return {"version": DATA_VERSION}
