from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from myApp.serializers import ItemSerializer
from myApp.models import Item
import datetime
# Create your views here.
class ItemListApiView(APIView):
    def get(self,request):
        qs=Item.objects.all()
        eserializer=ItemSerializer(qs,many=True)
        data=eserializer.data
        for item_data in data:
            if item_data['itemCategory']=='Medicine':
                item_data['price']=(item_data['price']*(5/100)+item_data['price'])*item_data['quantity']
            elif item_data['itemCategory']=='Food':
                item_data['price']=(item_data['price']*(5/100)+item_data['price'])*item_data['quantity']
            elif item_data['itemCategory']=='Imported':
                item_data['price']=(item_data['price']*(18/100)+item_data['price'])*item_data['quantity']
            elif item_data['itemCategory']=='Music':
                if item_data['price'] <=1000:
                    item_data['price']=(item_data['price']*(5/100)+item_data['price'])*item_data['quantity']
                elif item_data['price'] >=1000:
                    item_data['price']=(item_data['price']*(12/100)+item_data['price'])*item_data['quantity']
        final_price = {'total_price': 0,'date':None}
        for item_data_1 in data:
            final_price['total_price'] += item_data_1['price']
        if final_price['total_price'] >= 2000:
            final_price['total_price']=final_price['total_price']*(5/100)+final_price['total_price']
        date = datetime.date.today()
        final_price['date']=date
        data.append(final_price)
        return Response(data)
class ItemCreateAPIView(generics.CreateAPIView):
        queryset=Item.objects.all()
        serializer_class=ItemSerializer