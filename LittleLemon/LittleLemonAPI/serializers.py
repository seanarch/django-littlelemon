from rest_framework import serializers 
# from .models import MenuItem 

class MenuItemSerializer(serializers.Serializer): 
    # class Meta:
    #     model = MenuItem 
    #     fields = ['id', 'title', 'price', 'inventory']
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2) 
    inventory = serializers.IntegerField()