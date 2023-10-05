from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import MenuItem 
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST']) 
def menu_items(request): 
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all() 
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search:
            # items = items.filter(title__startswith=search)
            items = items.filter(title__contains=search)
        serialized_item = MenuItemSerializer(items, many=True) 
        return Response(serialized_item.data)
    if request.method == 'POST': 
        serialized_item = MenuItemSerializer(data=request.data) 
        serialized_item.is_valid(raise_exception=True) 
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view() 
def single_item(request, id): 
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item) 
    return Response(serialized_item.data)


# # Create your views here.
# class MenuItemsView(generics.ListCreateAPIView): 
#     queryset = MenuItem.objects.all() 
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView): 
#     queryset = MenuItem.objects.all() 
#     serializer_class = MenuItemSerializer 