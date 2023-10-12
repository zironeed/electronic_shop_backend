from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from shop.models import Seller, Contact, Product
from shop.serializers import SellerSerializer, ContactSerializer, ProductCreateSerializer, SellerCreateSerializer, \
    SellerProductSerializer


class SellerListView(ListAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class SellerCreateView(CreateAPIView):
    serializer_class = SellerCreateSerializer
    queryset = Seller.objects.all()


class SellerRetrieveView(RetrieveAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()


class SellerUpdateView(UpdateAPIView):
    serializer_class = SellerCreateSerializer
    queryset = Seller.objects.all()


class SellerDestroyView(DestroyAPIView):
    serializer_class = SellerCreateSerializer
    queryset = Seller.objects.all()


class ContactCreateView(CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactUpdateView(UpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


class ProductDestroyView(DestroyAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


class ProductListView(ListAPIView):
    serializer_class = SellerProductSerializer
    queryset = Seller.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
