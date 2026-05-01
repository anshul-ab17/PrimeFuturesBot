import typer
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_price
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

        typer.echo("\n Order Request:")
        typer.echo(f"{side} {quantity} {symbol} ({order_type})")

        confirm = typer.confirm("Proceed with order?")
        if not confirm:
            typer.echo("Cancelled ")
            raise typer.Exit()

        response = place_order(client, symbol, side, order_type, quantity, price)

        typer.secho("\n Order Response:", fg=typer.colors.GREEN)
        typer.echo(f"Order ID: {response.get('orderId')}")
        typer.echo(f"Status: {response.get('status')}")
        typer.echo(f"Executed Qty: {response.get('executedQty')}")
        typer.echo(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        typer.secho(f"\n Error: {str(e)}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()