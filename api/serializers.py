from rest_framework import serializers
from restapp.models import Product,Soldat,Temp,MoveTemphere



class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soldat
        fields = ['id', 'shop_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'prod_name', 'prod_image', 'prod_price', 'description', 'soldat']
        # depth = 1    # this shows all the details with in the foriegn key instead of just the id.

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# this is similar to depth = 1 but in this we can filter what you want by mention the field in the other 
# serializer and mention below.

class ProductSoldatSerializer(serializers.ModelSerializer):
    soldat = ShopSerializer() # mentioned here
    class Meta:
        model = Product
        fields = ['id', 'prod_name', 'prod_image', 'prod_price', 'description', 'soldat']
      



# -----------------------------------------------------------------------------------------------------------------------------------------------



class ShopnameProductSerializer(serializers.ModelSerializer):
    shop_name = serializers.CharField(source='soldat.shop_name', read_only=True)  # Use source to get shop_name from Soldat model
    class Meta:
        model = Product
        fields = ['id', 'prod_name', 'prod_image', 'prod_price', 'description', 'shop_name']






# --------------------------------------------------------------------------------------------------------------------




class PatchProductSerializer(serializers.ModelSerializer):
     class Meta:
        model = Product
        fields = ['id', 'prod_name', 'prod_image', 'prod_price', 'description', 'soldat']



class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ['id','name','place','buka','muka','maka']

class MovedTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoveTemphere
        fields = ['id','temp_id','name','place','buka','muka','maka']
