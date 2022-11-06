# ### contains the class for authenticating requests to the api
# from rest_framework import authentication
# from rest_framework import exceptions
# from config.settings import SECRET_KEY
# from users.services import get_email, get_user_business
# from users.models import User
# from business.models import Business
# import jwt


# class TokenAuth(authentication.TokenAuthentication):
    
#     def authenticate(self, request):
#         bearer = request.META.get('HTTP_AUTHORIZATION')
#         if not bearer:
#             raise exceptions.NotAuthenticated()

#         try:
#             payload = jwt.decode(bearer.split()[1], key=SECRET_KEY, algorithms=['HS256',])
            
#             try:
#                 user = get_email(payload['user_email'])
#                 try:
#                     business = get_user_business(user.key)
#                     if str(business.id) != str(payload['business_id']):
#                         raise exceptions.PermissionDenied('You do not have the rights to do that!')
                    
#                     request.data['business_id'] = str(business.id)

#                 except Business.DoesNotExist:
#                     raise exceptions.AuthenticationFailed('Invalid Business Credentials')

#             except User.DoesNotExist:
#                 raise exceptions.AuthenticationFailed('Invalid User Credentials')

#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('Expired Token')
#         except jwt.InvalidTokenError:
#             raise exceptions.AuthenticationFailed('Invalid Token')
            
#         return None
