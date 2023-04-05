import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

class Auth0JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')

        if not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]
        try:
            payload = jwt.decode(token, options={
                'verify_signature': False,
                'verify_aud': False,
                'verify_iss': False,
            })

            if payload['iss'] != settings.SIMPLE_JWT['JWT_ISSUER']:
                raise exceptions.AuthenticationFailed('Invalid issuer')
            if payload['aud'] != settings.SIMPLE_JWT['JWT_AUDIENCE']:
                raise exceptions.AuthenticationFailed('Invalid audience')

            # Replace this with your public key or JWKs URL
            public_key = '-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----'
            jwt.decode(token, public_key, algorithms=settings.SIMPLE_JWT['JWT_ALGORITHM'])

        except jwt.InvalidTokenError as e:
            raise exceptions.AuthenticationFailed(str(e))

        return (payload, token)
