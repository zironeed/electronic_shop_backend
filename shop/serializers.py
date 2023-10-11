from rest_framework import serializers
from shop.models import Seller, Contact, Product, Types


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class SellerCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        new_seller = Seller.objects.create(**validated_data)

        if new_seller.type == Types.factory and new_seller.provider:
            raise serializers.ValidationError('Factories can not have providers')

    class Meta:
        model = Seller
        exclude = ('creation_date', )


class SellerSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Seller
        exclude = ('creation_date', )


class ProductCreateSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.filter(type=Types.factory))

    class Meta:
        model = Product
        fields = '__all__'

    def validate_seller(self, value):
        if value.type != Types.factory:
            raise serializers.ValidationError('Only Sellers of type "Factory" can be assigned to a Product.')
        return value


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('seller', )


class SellerProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Seller
        fields = '__all__'

