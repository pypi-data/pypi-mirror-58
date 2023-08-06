AuthSCH SSO provider for Sentry
===============================

An SSO provider for Sentry which enables `AuthSCH <https://auth.sch.bme.hu/>`_  authentication.

This work is relying on `sentry's internal OAuth2 implementation <https://github.com/getsentry/sentry/blob/master/src/sentry/auth/providers/oauth2.py>`_
and inspired by `Google SSO provider for Sentry <https://github.com/getsentry/sentry/blob/master/src/sentry/auth/providers/google>`_.

Install
-------

::

    $ pip install sentry-auth-authsch

Setup
-----

Create a new OAuth Client on the `developer console of AuthSCH <https://auth.sch.bme.hu/console/index>`_.

For redirect uri, add the SSO endpoint of your installation::

    https://sentry.example.com/auth/sso/

Put your client id and secret into your ``sentry.conf.py``:

.. code-block:: python

    AUTHSCH_CLIENT_ID = ""

    AUTHSCH_CLIENT_SECRET = ""
