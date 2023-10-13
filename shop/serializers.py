from django.db.models import Q
from rest_framework import serializers
from shop.models import Seller, Contact, Product, Types


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class SellerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        exclude = ('creation_date', )

    def validate(self, attrs):
        if attrs['type'] == Types.factory and attrs['provider']:
            raise serializers.ValidationError('Factories cannot have providers')
        return attrs

    def update(self, instance, validated_data):
        validated_data.pop('credit', None)
        return super().update(instance, validated_data)


class SellerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Seller
        exclude = ('creation_date', )


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('seller', )


class SellerProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, seller):
        products = Product.objects.filter(Q(seller=seller) | Q(seller__provider=seller) | Q(seller__provider__provider=seller))
        serializer = ProductSerializer(products, many=True)
        return serializer.data

    class Meta:
        model = Seller
        fields = '__all__'

