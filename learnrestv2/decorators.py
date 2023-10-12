from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

def bearertokensystem():
    def decorator(func):
        def wrap(request,*args,**kwargs):
            if request.user.is_superuser == 1:
                authorization_header = request.META.get('HTTP_AUTHORIZATION')
                if authorization_header:
                    token = authorization_header.split(' ')[1]
                    print(type(token)," - data type")
                    print("Token:", token)
                    token2 = Token.objects.get(user_id=request.user.id)
                    token2 = str(token2)
                    print("Token2:", token2)
                    if token == token2:
                        print("Both are the same yeaaaaaa.....!!")
                        return func(request,*args,**kwargs)
            else:
                return Response({"status":True,"message ":"Must be a admin"},status=200)
        return wrap
    return decorator


def bearertokenuser():
    def decorator(func):
        def wrap(request,*args,**kwargs):
            if request.user.is_authenticated:
                authorization_header = request.META.get('HTTP_AUTHORIZATION')
                if authorization_header:
                    token = authorization_header.split(' ')[1]
                    print(type(token)," - data type")
                    print("Token:", token)
                    token2 = Token.objects.get(user_id=request.user.id)
                    token2 = str(token2)
                    print("Token2:", token2)
                    if token == token2:
                        print("Both are the same yeaaaaaa.....!!")
                        return func(request,*args,**kwargs)
            else:
                return Response({"status":True,"message ":"Must be a admin"},status=200)
        return wrap
    return decorator


def iwanttokenSir():
    def decorator(func):
        def wrap(request,*args,**kwargs):
            authorization_header = request.META.get('HTTP_AUTHORIZATION')
            print(authorization_header)
            if authorization_header:
                token = authorization_header.split(' ')[1]
                print(type(token)," - data type")
                print("Token:", token)
                token2 = Token.objects.get(user=2)
                token2 = str(token2)
                print("Token2:", token2)
                if token == token2:
                    print("Both are the same yeaaaaaa.....!!")
                    return func(request,*args,**kwargs)
                else:
                    return Response({"status":False,"message ":"Token Does not match"},status=status.HTTP_400_BAD_REQUEST)
            else:
                print("seserysderdd")
                return Response({"message ":"Please enter Token"},status=status.HTTP_400_BAD_REQUEST)
               
        return wrap
    return decorator