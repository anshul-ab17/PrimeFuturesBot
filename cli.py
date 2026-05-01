import typer
from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logger

app = typer.Typer()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    setup_logger()

    try:
        validate_side(side)
        validate_order_type(order_type)
        validate_price(order_type, price)

        client = get_client()

        print("\n Order Request:")
        print(f"{side} {quantity} {symbol} ({order_type})")

        response = place_order(client, symbol, side, order_type, quantity, price)

        print("\n Order Response:")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print(f"\n Error: {str(e)}")

if __name__ == "__main__":
    app()