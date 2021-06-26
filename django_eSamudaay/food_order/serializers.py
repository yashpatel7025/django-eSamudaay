from rest_framework import serializers 

class OrderItemSerializer(serializers.Serializer):
  name = serializers.CharField(required=True)
  quantity =serializers.IntegerField(required=True)
  price = serializers.IntegerField(required=True)

class OfferSerializer(serializers.Serializer):
  offer_type = serializers.CharField(required=True)
  offer_val = serializers.IntegerField(required=True)

  def validate(self, data):
    if data["offer_type"] not in ["FLAT","DELIVERY"]:
      raise serializers.ValidationError("offer type can be FLAT or DELIVERY")
    return data

class EntityWithIdSerializer(serializers.Serializer):
  order_items = serializers.ListField(child=OrderItemSerializer(required=True)) 
  distance = serializers.IntegerField(required=True, min_value=0, max_value=500000)
  offer = OfferSerializer(required=False)

