from __future__ import absolute_import, print_function

import re
import logging
import requests

from sentry.auth.view import AuthView, ConfigureView
from .constants import ERR_INVALID_RESPONSE, PROFILE_ENDPOINT

logger = logging.getLogger("sentry.auth.authsch")


class FetchUser(AuthView):
    def __init__(self, version, *args, **kwargs):
        self.version = version
        super(FetchUser, self).__init__(*args, **kwargs)

    def get_user_profile(self, token):
        return requests.get(
            PROFILE_ENDPOINT,
            params={'access_token': token},
            timeout=5
        ).json()

    def dispatch(self, request, helper):
        data = helper.fetch_state("data")

        try:
            # call /api/profile/?access_token=<access_token>
            # repsponse:
            # {
            #     "internal_id":"{9DA3D9BE-04CD-FD26-CB87-BAF34B0367F8}",
            #     "displayName":"Teszt Bela", "sn":"Teszt", "givenName":"Bela",
            #     "mail":"bela@tesztel.ek",
            #     "linkedAccounts": {
            #         "bme":"2214@bme.hu",
            #         "schacc":"belavagyok",
            #         "vir":"belaateszter"
            #     },
            #     "eduPersonEntitlement":[
            #         {"id":16,"name":"Simonyi K\u00e1roly Szakkoll\u00e9gium","status":"tag"},
            #         {"id":47,"name":"Koll\u00e9giumi Sz\u00e1m\u00edt\u00e1stechnikai K\u00f6r","status":"tag"},
            #         {"id":363,"name":"Buksi","status":"tag"}
            #     ]
            # }

            token = data['access_token']
            raw = self.get_user_profile(token=token)

        except Exception as exc:
            logger.exception(exc)
            return helper.error(ERR_INVALID_RESPONSE)

        try:
            userdata = self.populate_userdata(raw)
        except Exception as exc:
            logger.exception(exc)
            return helper.error(ERR_INVALID_RESPONSE)

        helper.bind_state('user', userdata)

        return helper.next_step()

    def populate_userdata(self, raw):
        userdata = dict()

        # cleaning up internal id from `{`, `}`, and `-` chars, because its unnecessary
        userdata['iid'] = re.sub('[-{}]', '', raw['internal_id'])
        userdata['schacc'] = raw['linkedAccounts']['schacc']
        userdata['full_name'] = raw['displayName']
        userdata['schmail'] = "{}@sch.bme.hu".format(userdata['schacc'])
        userdata['secondary_mail'] = raw.get('mail', None)
        userdata['raw_profile'] = raw

        return userdata.copy()


class AuthSCHConfigureView(ConfigureView):
    def dispatch(self, request, organization, auth_provider):
        return self.render('sentry_auth_authsch/configure.html')
