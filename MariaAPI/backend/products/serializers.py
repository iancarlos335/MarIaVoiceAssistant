from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    my_sale_price = serializers.DecimalField(read_only=True, max_digits=15, decimal_places=2, default=99.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'my_sale_price',
        ]

    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None

    def get_my_sale_price(self, obj):
        return obj.sale_price
