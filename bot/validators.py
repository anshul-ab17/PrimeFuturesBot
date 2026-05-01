def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_MARKET")

def validate_price(order_type, price):
    if order_type in ["LIMIT", "STOP_MARKET"] and price is None:
        raise ValueError("Price is required for LIMIT and STOP_MARKET orders")