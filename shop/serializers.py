from rest_framework import serializers
from shop.models import Seller, Contact, Product


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class SellerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        exclude = ('creation_date', )


class SellerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Seller
        exclude = ('creation_date', )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
