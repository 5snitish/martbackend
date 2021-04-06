from rest_framework import serializers
from .models import Product,Seller, product_catagories, Customer, Orders,Purchased_product,Product_details



class CustomerSerealizer(serializers.ModelSerializer):
    class Meta:
         model=Customer
         fields="__all__"



class OrdersSerealizer(serializers.ModelSerializer):
    class Meta:
         model =Orders
         fields="__all__"



class Purchased_ProductSerealizer(serializers.ModelSerializer):
    class Meta:
        model:Purchased_product
        fields:"__all__"




class CategorySrealizers(serializers.ModelSerializer):
    class Meta:
        model=product_catagories
        fields = "__all__"

class SellerSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields = "__all__"



class ProductSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance ) :
        responce = super().to_representation(instance)
        responce ['product_seller'] = SellerSerealizer(instance.product_seller).data
        return responce      

class Product_detailsSerealizer(serializers.ModelSerializer):
    class Meta:
        model=Product_details
        fields="__all__"
    
    def to_representation(self, instance ) :
        responce = super().to_representation(instance)
        responce ['product_id'] = ProductSerealizer(instance.product_id).data
        return responce