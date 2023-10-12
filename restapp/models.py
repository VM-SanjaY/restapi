from django.db import models

# Create your models here.

class Soldat(models.Model):
    shop_name = models.CharField(max_length=250,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.shop_name
  

class Product(models.Model):
    prod_name = models.CharField(max_length=250,blank=True,null=True)
    prod_image = models.ImageField(upload_to='product/',null=True,blank=True)
    prod_price = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    soldat = models.ForeignKey(Soldat, related_name='shop', null=True,on_delete=models.CASCADE)



class Temp(models.Model):
    name = models.CharField(max_length=250,blank=True,null=True)
    place = models.CharField(max_length=250,blank=True,null=True)
    buka = models.CharField(max_length=250,blank=True,null=True)
    muka = models.CharField(max_length=250,blank=True,null=True)
    maka = models.CharField(max_length=250,blank=True,null=True)


class MoveTemphere(models.Model):
    # temp_id = models.SmallIntegerField(default=0,blank=True,null=True)
    name = models.CharField(max_length=250,blank=True,null=True)
    place = models.CharField(max_length=250,blank=True,null=True)
    buka = models.CharField(max_length=250,blank=True,null=True)
    muka = models.CharField(max_length=250,blank=True,null=True)
    maka = models.CharField(max_length=250,blank=True,null=True)



