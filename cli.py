import typer
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs, validate_trade_logic
from bot.logging_config import setup_logger

app = typer.Typer()
logger = setup_logger()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):
    try:
        # ✅ Basic validation
        symbol, side, order_type, quantity, price = validate_inputs(
            symbol, side, order_type, quantity, price
        )

        # ✅ Create client
        client = get_client()

        # 🔥 Advanced validation (NEW)
        validate_trade_logic(client, symbol, side, order_type, quantity, price)

        # 📊 Print summary
        print("\n📊 Order Summary:")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print(f"Price: {price}")

        # 🚀 Place order
        order = place_order(client, symbol, side, order_type, quantity, price)

        if order:
            print("\n✅ Order Successful!")
            print(f"Order ID: {order.get('orderId')}")
            print(f"Status: {order.get('status')}")
            print(f"Executed Qty: {order.get('executedQty')}")
            print(f"Avg Price: {order.get('avgPrice')}")
        else:
            print("\n❌ Order Failed!")

    except Exception as e:
        logger.error(str(e))
        print(f"\n⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app()