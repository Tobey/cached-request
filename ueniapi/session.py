import requests
import requests_cache

from . import settings

class HTTPSession(requests.Session):

    def __init__(
            self,
            token=None,
            request_uri=None,
            user_agent=None,
            cache_request=None,
            cache_expires=None,
            auth_header=None,
            auth_prefix=None,
            **kwargs
    ):

        super().__init__()

        if cache_request:
            requests_cache.install_cache()

        trailing_slash = request_uri.endswith("/")
        self.request_uri = f'{request_uri}{"/" if  not trailing_slash else ""}'
        self.headers = {
            f'{auth_header}': f'{auth_prefix}{token}',
            'User-Agent': user_agent,
        }

    def request(self, method, endpoint, params=None, data=None, **kwargs):
        headers = kwargs.pop('headers', {})
        headers.update(self.headers)
        response = super().request(
            method,
            self.request_uri + endpoint,
            params=params,
            data=data,
            headers=headers,
            **kwargs
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            raise UeniAPIError(f'{e}\n{response.text}')

        return response


class UeniAPIError(Exception):
    pass
