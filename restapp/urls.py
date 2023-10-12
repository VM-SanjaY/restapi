from django.urls import path
from . import views
urlpatterns = [
    path('api/product/',views.getProject),
    path('api/product/<int:pk>/',views.getproduct_id),
    path('api/post/',views.post_product),
    path('classapi/product/',views.ProductDetails.as_view(),name="prodetail"),
    path('classapi/product/<int:pk>/',views.ProductbyID.as_view(),name="prodddetail"),
    path('shoppy/',views.shopandproducts,name="shopproducts"),
    path('loginpage/',views.loginpage),
    path('onlyauthenticate/',views.onlyauth),
    path('logout/',views.logoutpage),


    path('gettokenSir/',views.gettokenSir),
    path('getproductbyID/<int:pk>/',views.getproductbyID),
    path('putproductbyID/<int:pk>/',views.putproductbyID),
    path('patchproductbyID/<int:pk>/',views.patchproductbyID),
    path('deleteproductbyID/<int:pk>/',views.deleteproductbyID),


    path('entertemp/',views.entertemp),
    path('entertempway/',views.entertempway),
    path('gettemp/',views.gettemp),
    path('getandposttemp/',views.getandposttemp),
    path('gettemp2/',views.gettemp2),

    path('get_your_token_here/',views.get_your_token_here),
    path('productvalue/<int:pk>/',views.productvalue),


    path('shopnameProget/<int:pk>/',views.shopnameProget),

    path('shopnamePropatch/<int:pk>/',views.shopnamePropatch),




]