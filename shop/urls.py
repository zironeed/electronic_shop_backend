from django.urls import path

from shop.views import SellerCreateView, SellerDestroyView, SellerUpdateView, SellerListView, SellerRetrieveView

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('create/', SellerCreateView.as_view(), name='seller_create'),
    path('update/', SellerUpdateView.as_view(), name='seller_update'),
    path('retrieve/', SellerRetrieveView.as_view(), name='seller_retrieve'),
    path('destroy/', SellerDestroyView.as_view(), name='seller_destroy'),
    path('list/', SellerListView.as_view(), name='seller_list'),
]
