def validate_inputs(symbol, side, order_type, quantity, price):
    # Normalize inputs
    side = side.upper()
    order_type = order_type.upper()
    symbol = symbol.upper()

    # Validate side
    if side not in ["BUY", "SELL"]:
        raise ValueError("❌ Side must be BUY or SELL")

    # Validate order type
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("❌ Order type must be MARKET or LIMIT")

    # Validate quantity
    if quantity <= 0:
        raise ValueError("❌ Quantity must be greater than 0")

    # Validate price for LIMIT
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("❌ Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("❌ Price must be greater than 0")

    return symbol, side, order_type, quantity, price

def validate_trade_logic(client, symbol, side, order_type, quantity, price):
    ticker = client.futures_mark_price(symbol=symbol)
    current_price = float(ticker['markPrice'])

    # Minimum order value check
    if quantity * current_price < 100:
        raise ValueError("❌ Order must be at least 100 USDT")

    # LIMIT order logic
    if order_type == "LIMIT":
        if side == "BUY" and price >= current_price:
            raise ValueError("❌ BUY price should be below market price")

        if side == "SELL" and price <= current_price:
            raise ValueError("❌ SELL price should be above market price")