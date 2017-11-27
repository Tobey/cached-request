from .session import HTTPSession
from . import settings


class Client:
    def __init__(
            self,
            token=None,
            request_uri=settings.USER_AGENT,
            user_agent=settings.USER_AGENT,
            cache_request=settings.CACHE_REQUESTS,
            cache_expires=settings.CACHE_EXPIRES,
            auth_header=settings.AUTH_HEADER,
            auth_prefix=settings.AUTH_PREFIX,
            **kwargs
    ):

        self.session = HTTPSession(
            token=token,
            request_uri=request_uri,
            user_agent=user_agent,
            cache_request=cache_request,
            cache_expires=cache_expires,
            auth_header=auth_header,
            auth_prefix=auth_prefix,
            **kwargs
        )

    def __getattr__(self, item):
        return getattr(self.session, item)
