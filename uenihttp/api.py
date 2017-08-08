from .session import HTTPSession
from .settings import *


class Client:
    def __init__(
            self,
            token=X_UENI_TOKEN,
            request_uri=REQUEST_URI,
            user_agent=USER_AGENT,
            cache_request=CACHE_REQUESTS,
            cache_expires=CACHE_EXPIRES,
            **kwargs
    ):
        """

        :param token:
        :param request_uri:
        :param user_agent:
        :param cache_request:
        :param cache_expires:
        :param kwargs:
        """

        self.session = HTTPSession(
            token, request_uri, user_agent, cache_request, cache_expires, **kwargs
        )

    def get(self, endpoint, params=None):
        return self.session.get(
                endpoint,
                params=params
        )

    def post(self,endpoint, params=None, data=None):
        return self.session.post(
                endpoint,
                params=params,
                data=data
        )
