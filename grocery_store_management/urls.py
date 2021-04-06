from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




router = routers.DefaultRouter()
router.register("seller",SellerViewSet, basename="Seller")
router.register("product",ProductViewSet,basename  = "product")
router.register("customer",CustomerViewSet,basename = "customer")
router.register("categories",Product_catagoriesViewSet,basename="categories")
router.register("product_details", Product_detailsViewSet, basename="product_details")




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name = 'gettoken'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name = 'refresh_token'),
    path('api/seller_by_name/<str:name>',SellerNameViewSet.as_view(), name = 'seller_by_name'),
    path ('api/Customer_by_name/<str:name>',CustomerNameViewSet.as_view(),name = 'Customer'),
    path ('api/Customer_by_phone/<int:phone>',CustomerPhoneViewSet.as_view(),name = 'Phone'), 
    path ('api/Product_by_name/<str:name>',ProductNameViewSet.as_view(),name = 'Product'),
    path ('api/Product_category_byname/<str:name>',product_categoriesViewSet.as_view(),name = 'Product_category'),
]