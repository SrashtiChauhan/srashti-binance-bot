import sys
import uuid
from datetime import datetime

from src.utils.logger import logger
from src.utils.validator import (
    validate_symbol,
    validate_quantity,
    validate_price,
)
from src.config import TEST_MODE


def simulate_grid(symbol, lower_price, upper_price, grids, quantity):
    """
    Simulates grid strategy by generating price levels
    between lower and upper range.
    """

    if lower_price >= upper_price:
        raise ValueError("Lower price must be less than upper price")

    grid_size = (upper_price - lower_price) / grids
    orders = []

    logger.info(
        f"Starting Grid Strategy | Range: {lower_price} - {upper_price} | Grids: {grids}"
    )

    for i in range(grids + 1):
        price_level = lower_price + (i * grid_size)

        order_type = "BUY" if price_level < (lower_price + upper_price) / 2 else "SELL"

        order = {
            "order_id": str(uuid.uuid4()),
            "symbol": symbol,
            "side": order_type,
            "price": round(price_level, 2),
            "quantity": quantity,
            "timestamp": datetime.utcnow().isoformat(),
            "mode": "SIMULATION",
        }

        logger.info(f"[GRID] Created order: {order}")
        orders.append(order)

    return {
        "strategy": "GRID",
        "range": [lower_price, upper_price],
        "grids": grids,
        "total_orders": len(orders),
        "orders": orders,
        "status": "INITIALIZED",
    }


def place_grid_order(symbol, lower_price, upper_price, grids, quantity):
    try:
        validate_symbol(symbol)
        validate_price(lower_price)
        validate_price(upper_price)
        validate_quantity(quantity)

        if grids <= 0:
            raise ValueError("Grids must be greater than 0")

        logger.info(
            f"Placing GRID | Symbol: {symbol} | Range: {lower_price}-{upper_price} | Grids: {grids}"
        )

        if TEST_MODE:
            result = simulate_grid(symbol, lower_price, upper_price, grids, quantity)
        else:
            raise NotImplementedError("Live API mode not enabled.")

        print(" Grid strategy initialized!")
        print(result)

    except Exception as e:
        logger.error(f"Grid strategy failed: {str(e)}")
        print(" Grid failed:", str(e))


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python -m src.advanced.grid_strategy SYMBOL LOWER_PRICE UPPER_PRICE GRIDS QUANTITY")
        sys.exit(1)

    symbol = sys.argv[1]
    lower_price = float(sys.argv[2])
    upper_price = float(sys.argv[3])
    grids = int(sys.argv[4])
    quantity = float(sys.argv[5])

    place_grid_order(symbol, lower_price, upper_price, grids, quantity)