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
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.filter(type=Types.factory))

    class Meta:
        model = Product
        fields = '__all__'

    def validate_seller(self, value):
        if value.type != Types.factory:
            raise serializers.ValidationError('Only Sellers of type "Factory" can be assigned to a Product.')
        return value

    def create(self, validated_data):
        seller = validated_data['seller']
        provider = seller.provider
        products = seller.products.all()

        validated_data.pop('seller')

        for lower_seller in Seller.objects.filter(Q(provider=seller) | Q(provider=provider)):
            if lower_seller.products.filter(id__in=products.values_list('id', flat=True)).count() == 0:
                product = Product.objects.create(seller=lower_seller, **validated_data)
                product.seller = seller
                product.save()

        return super().create(validated_data)


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

