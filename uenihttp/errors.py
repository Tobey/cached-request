
class UeniAPIError(Exception):

    @classmethod
    def check_token(cls, token):
        if token is None:
            raise cls('Token cannot be None')
        return token
