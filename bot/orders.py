import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Order request: {symbol} {side} {order_type} qty={quantity} price={price}")

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # LIMIT
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        # STOP_MARKET
        elif order_type == "STOP_MARKET":
            params["stopPrice"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logging.info(f"Order response: {response}")
        return response

    except Exception as e:
        logging.error(f"Order error: {str(e)}")
        raise