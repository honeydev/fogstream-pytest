from rest_framework_jwt.settings import api_settings

class JWT:

    def __init__(self, user):
        '''
        :param user:
        '''
        self.user = user


    def generate(self):
        '''
        :return: string
        '''
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(self.user)
        return jwt_encode_handler(payload)

