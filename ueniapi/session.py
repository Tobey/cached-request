import requests
import requests_cache

from .errors import UeniAPIError


class HTTPSession(requests.Session):

    def __init__(self, token=None, request_uri=None, user_agent=None, cache_request=None,
                 cache_expires=None,  **kwargs ):
        super().__init__()

        if cache_request:
            requests_cache.install_cache()

        self.request_uri = request_uri
        self.headers = {
            'X_UENI_TOKEN': UeniAPIError.check_token(token),
            'User-Agent': user_agent,
        }

    def request(self, method, endpoint, params=None, data=None, **kwargs):

        response = super().request(
            method,
            self.request_uri + endpoint,
            params=params,
            data=data,
            **kwargs
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise UeniAPIError('{exception}\n{message}'.format(exception=str(e),
                                                               message=response.text))

        return response
