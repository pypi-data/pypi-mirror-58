from __future__ import absolute_import

from django.apps import AppConfig


class Config(AppConfig):
    name = "sentry_auth_authsch"

    def ready(self):
        from sentry import auth

        from .provider import AuthSCHProvider

        auth.register("authsch", AuthSCHProvider)
