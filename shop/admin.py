from django.contrib import admin
from shop.models import Contact, Seller, Product


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ('name', 'type', 'provider_url', 'credit', 'creation_date')
    list_filter = ('contacts__city',)
    actions = ['clean_credit']

    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj))
        fields.append('provider_url')
        return fields

    def provider_url(self, obj):
        return f'http://127.0.0.1:8000/shop/retrieve/{obj.provider_id}/'

    @admin.action
    def clean_credit(self, request, queryset):
        queryset.update(credit=0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'city', 'seller')
    list_filter = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'date', 'seller', )
