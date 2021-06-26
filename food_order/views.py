from django.shortcuts import render

from .serializers import EntityWithIdSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import *
# Create your views here.

@api_view(['POST'])
def order(request):
	serializer = EntityWithIdSerializer(data=request.data)
	if serializer.is_valid():
		data= serializer.data
		total_before_discount = get_items_total_cost(data.get("order_items")) + get_delivery_cost(data.get("distance"))
		total_after_discount = total_before_discount - get_discount(total_before_discount, data)
		return  Response({"order_total":total_after_discount}, status=status.HTTP_200_OK)
	else:
		return  Response({"errors": dict(serializer.errors.items())}, status=status.HTTP_400_BAD_REQUEST)