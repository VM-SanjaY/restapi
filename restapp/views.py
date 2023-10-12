from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api.serializers import *
import requests
from rest_framework.response import Response
from .models import Product, Soldat, Temp, MoveTemphere
from learnrestv2.decorators import bearertokensystem,iwanttokenSir
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.db import connection
from django.utils import timezone

# Create your views here.

# -----------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------  Function method -----------------------------------------------------


@api_view(['GET'])
@iwanttokenSir()
def getProject(request):  
    product = Product.objects.all()
    for prod in product:
        print(prod.prod_name)
    serializer = ProductSerializer(product,many=True)
    return Response({"status":True,"data":serializer.data},status=200)

@api_view(['GET'])
@iwanttokenSir()
def getproduct_id(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,many=False)
    except:
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True) 

    return Response({"status":True,"data":serializer.data},status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def post_product(request):
    serilizer = ProductSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serilizer.data,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @iwanttokenSir()
# def post_product(request):
#     prod_name = request.POST.get('prod_name')
#     prod_price = request.POST.get('prod_price')
#     description = request.POST.get('description')
#     prod_image = request.FILES.get('prod_image')
#     if prod_name:
#         data = Product(
#             prod_name=prod_name,
#             prod_price=prod_price,
#             description = description,
#             prod_image=prod_image,
#         )
#         data.save()
#     product = Product.objects.all()
#     for prod in product:
#         print(prod.prod_name)
#     serializer = ProductSerializer(product,many=True)
#     return Response({"status":True,"data":serializer.data},status=200)


@api_view(['GET'])
@iwanttokenSir()
def shopandproducts(request):
    prod = Product.objects.all()
    print("shoppy - ", prod)
    serializer = ProductSerializer(prod,many=True)
    return Response({"status":True,"data":serializer.data},status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def loginpage(request):
    print("xdrthdrjtft")
    print(request.data.get)
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password,"esseyuseyey")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            try:
                token = Token.objects.get(user_id=user.id)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            print(token.key)
        return Response({"status":True,"Token ":token.key},status=200)

@api_view(['POST'])
@iwanttokenSir()
def logoutpage(request):
    if request.method == 'POST':
        delete = request.data.get('delete')
        if delete == "yes":
            user = request.user
            token = Token.objects.get(user_id=user.id)
            token.delete()
            logout(request)
            return Response({"status":True,"Message ":"user logged out"},status=200)


@api_view(['GET'])
@iwanttokenSir()
def onlyauth(request):
    prod = Product.objects.all()
    print("shoppy - ", prod)
    serializer = ProductSerializer(prod,many=True)
    return Response({"status":True,"data":serializer.data},status=200)



@api_view(['POST'])
@permission_classes([AllowAny])
def gettokenSir(request):
    if request.method == 'POST':
        global username
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            if username == 'apiuser':
                user = User.objects.get(username=username)
                try:
                    token = Token.objects.get(user_id=user.id)
                    if token:
                        tokencreated_time = token.created
                        print(tokencreated_time)
                        print(timezone.now(),"sdrdtdht")
                        print(timezone.now()-tokencreated_time,"checking")
                        compare = timezone.now()-tokencreated_time
                        if compare > timedelta(hours = 1):
                            token.delete()
                            token = Token.objects.create(user_id=user.id)
                except Token.DoesNotExist:
                    token = Token.objects.create(user_id=user.id)
                
                return Response({"status":True,"Token ":token.key},status=200)




            

@api_view(['GET'])
# @iwanttokenSir()
def getproductbyID(request,pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response({"status":True,"data":serializer.data},status=200)


@api_view(['PUT'])
def putproductbyID(request,pk):
    print("dsrsdhsdhsdrhsdsdrh")
    product = Product.objects.get(pk=pk)  
    serilizer = ProductSerializer(product,data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response({"status":True,"data":serilizer.data},status=204)
    

@api_view(['PATCH'])  
def patchproductbyID(request,pk):
    print("dsrsdhsdhsdrhsdsdrh")
    product = Product.objects.get(pk=pk)  
    serilizer = PatchProductSerializer(product,data=request.data,partial=True)
    if serilizer.is_valid():
        serilizer.save()
        return Response({"status":True,"data":serilizer.data},status=204)
    

@api_view(['DELETE'])
# @iwanttokenSir()
def deleteproductbyID(request,pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    msg = {"messsage":"Product is deleted"}
    return Response(msg,status=status.HTTP_204_NO_CONTENT)







@api_view(['POST'])
def entertemp(request):
    serilizer = TempSerializer(data=request.data)
    serilizer2 = MovedTempSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        if serilizer2.is_valid():
            serilizer2.save()
        return Response(serilizer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serilizer.data,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def entertempway(request):
    serilizer = TempSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
        return Response(serilizer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serilizer.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def gettemp(request):
    tempa = Temp.objects.all()
    serilizer = TempSerializer(tempa,many=True)
    return Response(serilizer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
def getandposttemp(request):
    tempa = Temp.objects.all()
    serilizer = TempSerializer(tempa,many=True)
    # Temp.objects.raw('insert into MoveTemphere select * from Temp')
    with connection.cursor() as cursor:
        cursor.execute('insert into restapp_movetemphere(name, place, buka, muka, maka) select name, place, buka, muka, maka from restapp_temp')

    return Response(serilizer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny])
def gettemp2(request):
    with connection.cursor() as cursor:
        cursor.execute('insert into restapp_movetemphere(name, place, buka, muka, maka) select name, place, buka, muka, maka from restapp_temp')
    with connection.cursor() as cursor:
        cursor.execute('TRUNCATE TABLE restapp_temp;')    
    tempa = MoveTemphere.objects.all()
    serilizer = MovedTempSerializer(tempa,many=True)
    return Response(serilizer.data,status=status.HTTP_200_OK)


# ----------------------------------------------------------------------------------------------------------------

# Get and patch

@api_view(['GET'])
def shopnameProget(request,pk):
    prod = Product.objects.get(pk=pk) 
    serilizer = ShopnameProductSerializer(prod)
    return Response(serilizer.data,status=status.HTTP_200_OK)



@api_view(['PATCH'])
def shopnamePropatch(request,pk):
    print("dsrsdhsdhsdrhsdsdrh")
    product = Product.objects.get(pk=pk)
    shop = request.data.get('shop_name')
    if shop:
        soldshop = Soldat.objects.get(id=product.soldat.id)
        soldshop.shop_name = shop
        soldshop.save()
    mooo = Product.objects.get(pk=pk)
    serilizer = ShopnameProductSerializer(mooo,data=request.data,partial=True)
    if serilizer.is_valid():
        serilizer.save()
        return Response({"status":True,"data":serilizer.data},status=204)


@api_view(['PATCH'])
def shopnamePropatchdept(request,pk):
    print("dsrsdhsdhsdrhsdsdrh")
    product = Product.objects.get(pk=pk)
    serilizer = ProductSoldatSerializer(product,data=request.data,partial=True) # similar to depth
    if serilizer.is_valid():
        serilizer.save()
        return Response({"status":True,"data":serilizer.data},status=204)





@api_view(['GET'])
@permission_classes([AllowAny])
def get_your_token_here(request):
    user = User.objects.get(username='apiuser')
    try:
        token = Token.objects.get(user_id=user.id)
        if token:
            tokencreated_time = token.created
            print(tokencreated_time)
            print(timezone.now(),"sdrdtdht")
            print(timezone.now()-tokencreated_time,"checking")
            compare = timezone.now()-tokencreated_time
            if compare > timedelta(hours = 1):
                token.delete()
                token = Token.objects.create(user_id=user.id)
    except Token.DoesNotExist:
        token = Token.objects.create(user_id=user.id)
    print(token.key)
    return Response({"status":True,"Token ":token.key},status=200)
    # dota = token.key
    # return dota





@api_view(['GET'])
@permission_classes([AllowAny])
def productvalue(request,pk):

    url = "http://localhost:8000/getproductbyID/"+str(pk)+"/"

    payload = {}
    headers = {
    'Authorization': 'Bearer '+get_your_token_here(request)
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print("sdreyreererferstrthrrurueyeryer6",response.text)
    product = Product.objects.get(pk=pk)
    serilizer = ProductSoldatSerializer(product)
    # if serilizer.is_valid():
    return Response({"status":True,"response":serilizer.data},status=200)

    





















# ------------------------------------------------------------------------------------------------------------------------------------------------

# --------------------------------------- class method ---------------------------------------------------------------------------


class ProductDetails(APIView):
    @iwanttokenSir()
    def get(self,request):
        prod = Product.objects.all()
        serilizer = ProductSerializer(prod,many=True)
        return Response(serilizer.data,status=status.HTTP_200_OK)
    @iwanttokenSir()
    def post(self,request):
        serilizer = ProductSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serilizer.data,status=status.HTTP_400_BAD_REQUEST)




class ProductbyID(APIView):
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product,many=False) 
            return Response({"status":True,"data":serializer.data},status=200)
        except:
            msg = {"message":"Product does not exist"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        
    def put(self,request,pk):
        print("dsrsdhsdhsdrhsdsdrh")
        product = Product.objects.get(pk=pk)  
        serilizer = ProductSerializer(product,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"status":True,"data":serilizer.data},status=204)
  
    def patch(self,request,pk):
        print("dsrsdhsdhsdrhsdsdrh")
        product = Product.objects.get(pk=pk)  
        serilizer = ProductSerializer(product,data=request.data,partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({"status":True,"data":serilizer.data},status=204)
        

    def delete(self,request,pk):
        print(pk,"sxdhdhdh")
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            msg = {"messsage":"Product is deleted"}
            return Response(msg,status=status.HTTP_204_NO_CONTENT)
        except product.DoesNotExist:
            msg = {"messsage":"Product does not exist"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)

     


    # def put(self,request,pk):
    #     print("dsrsdhsdhsdrhsdsdrh")
    #     try:
    #         product = Product.objects.get(pk=pk)
    #         prod_name = request.POST.get('name')
    #         prod_price = request.POST.get('price')
    #         desp = request.POST.get('description')
    #         image = request.FILES.get('image')
    #         if prod_name:
    #             product.prod_name=prod_name
    #             product.prod_price=prod_price
    #             product.description = desp
    #             product.prod_image=image
    #             product.save()
    #             serilizer = ProductSerializer(product,many=False)
    #             return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
    #     except product.DoesNotExist:
    #         msg = {"messsage":"Product does not exist"}
    #         return Response(msg,status=status.HTTP_404_NOT_FOUND)



    # def patch(self,request,pk):
    #     try:
    #         product = Product.objects.get(pk=pk)
    #         prod_name = request.POST.get('name')
    #         prod_price = request.POST.get('price')
    #         desp = request.POST.get('description')
    #         image = request.FILES.get('image')
    #         if prod_name:
    #             product.prod_name=prod_name
    #         if prod_price:
    #             product.prod_price=prod_price
    #         if desp:                
    #             product.description = desp
    #         if image:
    #             product.prod_image=image    
    #         product.save()
    #         serilizer = ProductSerializer(product,many=False,partial=True)
    #         return Response(serilizer.data,status=status.HTTP_205_RESET_CONTENT)
    #     except product.DoesNotExist:
    #         msg = {"messsage":"Product does not exist"}
    #         return Response(msg,status=status.HTTP_404_NOT_FOUND)
    




# -----------------------------------------------------------------------------------------------------------------------























































































































