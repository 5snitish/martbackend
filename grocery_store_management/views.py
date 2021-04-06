from django.shortcuts import render
from rest_framework import viewsets
from .seriealizers import *
from .models import *
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
# creating views for seller
class SellerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        seller = Seller.objects.all() 
        serializer = SellerSerealizer(seller, many= True, context = {"request":request})
        responce_dict = {"error":False,"message":"All Seller List Data","data":serializer.data}
        return Response(responce_dict)

    def create (self,request):
        try:
            serializer = SellerSerealizer(data=request.data,context = {"request":request})
            serializer.is_valid() 
            serializer.save()
            dist_responce={"error":False,"message":"Seller Data Save Successfully"}
        except:
            dist_responce={"error":True,"message":"Saving Seller Data has been failed"}
        return Response (dist_responce)

    def update (self,request,pk=None):
        try:

            queryset = Seller.objects.all()
            seller = get_object_or_404 (queryset,pk=pk)
            serializer = SellerSerealizer(seller,data = request.data, context = {"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Sucessfulley  Updated Seller Data"}
            
        except:
            dict_responce={"error":True,"message":"Error During Updating Seller Data"}
        return Response(dict_responce)
    
    def retrieve(self,request,pk =None):
        queryset = Seller.objects.all()
        seller = get_object_or_404 (queryset,pk=pk)
        serializer = SellerSerealizer(seller,context = {"request":request})
        dist_responce = {"error":False,"message":"seller deta fetched", "data":serializer.data}
        return Response(dist_responce )

class SellerNameViewSet(generics.ListAPIView):
    serializer_class = SellerSerealizer
    def get_queryset(self):
        name = self.kwargs["name"]
        return Seller.objects.filter(seller_name=name)               
        
         

class ProductViewSet(viewsets.ViewSet):
     authentication_classes = [JWTAuthentication]
     permission_classes = [IsAuthenticated]

     def list(self,request):
        product =Product.objects.all() 
        serializer = ProductSerealizer(product, many= True, context = {"request":request})
        responce_dict = {"error":False,"message":"All Product List Data","data":serializer.data}
        return Response(responce_dict)


     def create (self,request):
        try: 
            serializer = ProductSerealizer(data=request.data,context = {"request":request})
            serializer.is_valid(raise_exception=True) 
            serializer.save()
            dist_response={"error":False,"message":"Product Data Save Successfully"}
        except:
            dist_response={"error":True,"message":"error while saving Product Data"}
        
        return Response (dist_responce)


     def retrieve(self,request,pk =None):
        queryset = Product.objects.all()
        product = get_object_or_404 (queryset,pk=pk)
        serializer = ProductSerealizer(product,context = {"request":request})
        dist_responce = {"error":False,"message":"product deta fetched", "data":serializer.data}
        return Response(dist_responce )    
   
     def update (self,request,pk=None):
        try:

            queryset = Product.objects.all()
            product = get_object_or_404 (queryset,pk=pk)
            serializer = ProductSerealizer(product,data = request.data, context = {"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Sucessfulley  Updated product Data"}
            
        except:
            dict_response={"error":True,"message":"Error During Updating product Data"}
        return Response(dict_responce)

class ProductNameViewSet(generics.ListAPIView):
    serializer_class = ProductSerealizer
    def get_queryset(self):
        name = self.kwargs["name"]
        return Product.objects.filter(product_name=name)

        


class CustomerViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list (slef,request):
        customer=Customer.objects.all() 
        serializer =CustomerSerealizer(customer, many= True, context = {"request":request})
        responce_dict = {"error":False,"message":"All Product List Data","data":serializer.data}
        return Response(responce_dict)



    def create (self,request):
        try: 
          serializer = CustomerSerealizer(data=request.data,context = {"request":request})
          serializer.is_valid(raise_exception=True) 
          serializer.save()

          dist_response={"error":False,"message":"customer Data Save Successfully"}
        except:
          dist_response={"error":True,"message":"error while saving customer Data"}
        
        return Response (dist_responce)
     
    def update (self,request,pk=None):
        try:

            queryset = Customer.objects.all()
            customer= get_object_or_404 (queryset,pk=pk)
            serializer = CustomerSerealizer(customer,data = request.data, context = {"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Sucessfulley  Updated customer Data"}
            
        except:
            dict_response={"error":True,"message":"Error During Updating customer Data"}
        return Response(dict_responce)      

    def retrieve(self,request,pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404 (queryset,pk=pk)
        serializer = CustomerSerealizer(customer,context = {"request":request})
        dist_responce = {"error":False,"message":"customer deta fetched", "data":serializer.data}
        return Response(dist_responce )


class CustomerNameViewSet(generics.ListAPIView):
    serializer_class = CustomerSerealizer
    def get_queryset(self):
        name = self.kwargs["name"]
        return Customer.objects.filter(customer_name=name)


class CustomerPhoneViewSet(generics.ListAPIView):
    serializer_class = CustomerSerealizer
    def get_queryset(self):
        phone = self.kwargs["phone"]
        return Customer.objects.filter(customer_phone=phone) 


class Product_catagoriesViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list (self,request):
        proc = product_catagories.objects.all()
        serializer = CategorySrealizers(proc, many = True, context = {"request":request})
        responce_dict = {"error":False,"message":"all categories has been fatched","data":serializer.data}
        return Response(responce_dict)

    def create (self,request):
        try: 
            serializer = CategorySrealizers(data=request.data,context = {"request":request})
            serializer.is_valid(raise_exception=True) 
            serializer.save()

            dist_response={"error":False,"message":"category Data Save Successfully"}
        except:
            dist_response={"error":True,"message":"error while saving category Data"}
            
        return Response (dist_response) 


    def update (self,request,pk=None):
        try:

            queryset =  product_catagories.objects.all()
            categories= get_object_or_404 (queryset,pk=pk)
            serializer = CategorySrealizers(categories,data = request.data, context = {"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Sucessfulley  Updated categories Data"}
            
        except:
            dict_response={"error":True,"message":"Error During Updating categories Data"}
        return Response(dict_response)


    def retrieve(self,request,pk=None):
        queryset = product_catagories.objects.all()
        cat = get_object_or_404 (queryset,pk=pk)
        serializer = CategorySrealizers(cat,context = {"request":request})
        dist_responce = {"error":False,"message":"categories deta fetched", "data":serializer.data}
        return Response(dist_responce) 

class product_categoriesViewSet(generics.ListAPIView):
    serializer_class =CategorySrealizers
    def get_queryset(self):
        name = self.kwargs["name"]
        return product_catagories.objects.filter(category_name=name) 
 
class Product_detailsViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def list (self,request):
        prod = Product_details.objects.all()
        serializer = Product_detailsSerealizer(prod, many = True, context = {"request":request})
        responce_dict = {"error":False,"message":"all product details has been fatched","data":serializer.data}
        return Response(responce_dict)


    def create (self,request):
        try: 
            serializer = Product_detailsSerealizer(data=request.data,context = {"request":request})
            serializer.is_valid(raise_exception=True) 
            serializer.save()

            dist_response={"error":False,"message":"product details Data Save Successfully"}
        except:
            dist_response={"error":True,"message":"error while saving product details Data"}
            
        return Response (dist_response) 

    def update (self,request,pk=None):
        try:

            queryset =  product_details.objects.all()
            prod= get_object_or_404 (queryset,pk=pk)
            serializer = Product_detailsSerealizer(prod,data = request.data, context = {"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Sucessfulley  Updated product details Data"}
            
        except:
            dict_response={"error":True,"message":"Error During Updating product details Data"}
        return Response(dict_response) 


    def retrieve(self,request,pk=None):
        queryset = Product_details.objects.all()
        cat = get_object_or_404 (queryset,pk=pk)
        serializer = Product_detailsSerealizer(cat,context = {"request":request})
        dist_responce = {"error":False,"message":"categories deta fetched", "data":serializer.data}
        return Response(dist_responce)      





seller_list = SellerViewSet.as_view({"get":"list"})
seller_create =SellerViewSet.as_view({"post":"create"}) 
seller_update = SellerViewSet.as_view({"put":"update"})