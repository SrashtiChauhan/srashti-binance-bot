import sys
import uuid
from datetime import datetime

from src.utils.logger import logger
from src.utils.validator import (
    validate_symbol,
    validate_side,
    validate_quantity,
    validate_price,
)
from src.config import TEST_MODE


def simulate_limit_order(symbol, side, quantity, price):
    simulated_order = {
        "orderId": str(uuid.uuid4()),
        "symbol": symbol,
        "side": side,
        "type": "LIMIT",
        "quantity": quantity,
        "price": price,
        "status": "NEW",
        "timestamp": datetime.utcnow().isoformat(),
        "mode": "SIMULATION",
    }

    logger.info(f"[SIMULATION] Limit order placed: {simulated_order}")
    return simulated_order


def place_limit_order(symbol, side, quantity, price):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(quantity)
        validate_price(price)

        logger.info(
            f"Placing LIMIT order | Symbol: {symbol} | Side: {side} | Qty: {quantity} | Price: {price}"
        )

        if TEST_MODE:
            order = simulate_limit_order(symbol, side, quantity, price)
        else:
            raise NotImplementedError("Live API mode not enabled.")

        print(" Limit order placed successfully!")
        # print(order)
        return

    except Exception as e:
        logger.error(f"Limit order failed: {str(e)}")
        # print(" Order failed:", str(e))
        return {"error": str(e)}


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python src/limit_orders.py SYMBOL SIDE QUANTITY PRICE")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    price = float(sys.argv[4])

    place_limit_order(symbol, side, quantity, price)