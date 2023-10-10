from django.urls import path

from shop.views import SellerCreateView, SellerDestroyView, SellerUpdateView, SellerListView, SellerRetrieveView, \
    ContactCreateView, ContactUpdateView, ContactRetrieveView

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('create/', SellerCreateView.as_view(), name='seller_create'),
    path('update/', SellerUpdateView.as_view(), name='seller_update'),
    path('retrieve/', SellerRetrieveView.as_view(), name='seller_retrieve'),
    path('destroy/', SellerDestroyView.as_view(), name='seller_destroy'),
    path('list/', SellerListView.as_view(), name='seller_list'),

    path('create/contact/', ContactCreateView.as_view(), name='contact_create'),
    path('update/contact/', ContactUpdateView.as_view(), name='contact_update'),
    path('retrieve/contact/', ContactRetrieveView.as_view(), name='contact_retrieve'),
]
