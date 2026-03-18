from loguru import logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing order → {symbol} | {side} | {order_type} | Qty: {quantity} | Price: {price}")

        # MARKET ORDER
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        # LIMIT ORDER
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logger.success(f"Order placed successfully: {order}")
        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        return None