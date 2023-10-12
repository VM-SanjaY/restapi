from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from datetime import timedelta
from django.utils import timezone


# this class automatically get the token passed in the postman and deletes the token after a specified
# time limit and it also should be added in the settings.py file

# also check the token get function i have added few lines as well to delete after some time.

class TokenAuthentication(BaseTokenAuth):
    keyword ="Bearer"
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key = key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")      
        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")
        if token:
            tokencreated_time = token.created
            print(tokencreated_time)
            print(timezone.now(),"sdrdtdht")
            print(timezone.now()-tokencreated_time,"checking")
            compare = timezone.now()-tokencreated_time

            if compare > timedelta(hours = 1):
                token.delete()
                print("TOKEN IS deleted")
                raise AuthenticationFailed("The Token is expired")
        return (token.user, token) 


