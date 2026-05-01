import logging
import time


def get_min_price(client, symbol):
    info = client.futures_exchange_info()
    for s in info["symbols"]:
        if s["symbol"] == symbol:
            for f in s["filters"]:
                if f["filterType"] == "PRICE_FILTER":
                    return float(f["minPrice"])
    return None


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(
            f"Order request: {symbol} {side} {order_type} qty={quantity} price={price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        # LIMIT order
        if order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders.")
            min_price = get_min_price(client, symbol)
            if min_price is not None and price < min_price:
                raise ValueError(
                    f"Price {price} is below the minimum allowed price {min_price} for {symbol}."
                )
            params["price"] = price
            params["timeInForce"] = "GTC"

        # STOP_MARKET
        elif order_type == "STOP_MARKET":
            if price is None:
                raise ValueError("Stop price is required for STOP_MARKET orders.")
            min_price = get_min_price(client, symbol)
            if min_price is not None and price < min_price:
                raise ValueError(
                    f"Stop price {price} is below the minimum allowed price {min_price} for {symbol}."
                )
            params["stopPrice"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)
        logging.info(f"Initial response: {response}")

        
        order_id = response["orderId"]
        time.sleep(1)

        updated_order = client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )

        logging.info(f"Updated order: {updated_order}")

        return updated_order

    except Exception as e:
        logging.error(f"Order error: {str(e)}")
        raise