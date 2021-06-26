from django_eSamudaay.settings import DELIVERY_FEE_CONFIG

def get_items_total_cost(order_items):
	prices = list(map(lambda item: item["price"]*item["quantity"], order_items))
	return sum(prices)

def get_delivery_cost(distance):
	for config_distance, delivery_fee in DELIVERY_FEE_CONFIG.items():
		if distance<=config_distance:
			return delivery_fee

def get_discount(total_before_discount, data):
	offer = data.get("offer")
	if not offer:
		return 0
	if offer["offer_type"]=="FLAT":
		return min(total_before_discount, offer['offer_val'])
	else:
		return get_delivery_cost(data["distance"])



