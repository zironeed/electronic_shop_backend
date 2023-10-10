from django.urls import path

from shop.views import SellerCreateView, SellerDestroyView, SellerUpdateView, SellerListView, SellerRetrieveView, \
    ContactCreateView, ContactUpdateView, ContactRetrieveView

from shop.apps import ShopConfig

app_name = ShopConfig.name

urlpatterns = [
    path('create/', SellerCreateView.as_view(), name='seller_create'),
    path('update/<int:pk>/', SellerUpdateView.as_view(), name='seller_update'),
    path('retrieve/<int:pk>/', SellerRetrieveView.as_view(), name='seller_retrieve'),
    path('destroy/<int:pk>/', SellerDestroyView.as_view(), name='seller_destroy'),
    path('list/', SellerListView.as_view(), name='seller_list'),

    path('create/contact/', ContactCreateView.as_view(), name='contact_create'),
    path('update/contact/<int:pk>/', ContactUpdateView.as_view(), name='contact_update'),
    path('retrieve/contact/<int:pk>/', ContactRetrieveView.as_view(), name='contact_retrieve'),
]
