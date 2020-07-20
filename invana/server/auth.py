from base64 import b64encode
import logging


class InvanaBasicAuth:
    """


    """
    headers = {}

    def __init__(self, username=None, password=None):
        encoded_token = b64encode(bytes(f"{username}:{password}", "utf-8")).decode("ascii")
        self.headers = {'Authorization': 'Basic %s' % encoded_token}


class InvanaTokenAuth:
    """


    """
    headers = {}
    token = None

    def __init__(self, auth_data=None):
        try:
            self.token = auth_data.split("Bearer ")[1]
        except Exception as e:
            logging.error(e)
            self.token = None
        self.headers = {'Authorization': 'Bearer %s' % self.token}

    @staticmethod
    def check_is_validate():
        # TODO - write some logics to validate this token
        return True

