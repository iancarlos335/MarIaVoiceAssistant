from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    my_sale_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'my_sale_price',
            'my_discount',
        ]

    def get_my_discount(self, obj):
        print(obj.id)
        return obj.get_discount()

    def get_my_sale_price(self, obj):
        return obj.sale_price
