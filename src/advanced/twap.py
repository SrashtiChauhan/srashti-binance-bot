import sys
import uuid
import time
from datetime import datetime

from src.utils.logger import logger
from src.utils.validator import (
    validate_symbol,
    validate_side,
    validate_quantity,
)
from src.config import TEST_MODE


def simulate_twap(symbol, side, total_quantity, slices, interval):
    """
    Simulate TWAP execution by splitting order into equal parts.
    """

    slice_quantity = total_quantity / slices
    executed_orders = []

    logger.info(f"Starting TWAP execution: {slices} slices, {interval}s interval")

    for i in range(slices):
        order = {
            "order_id": str(uuid.uuid4()),
            "symbol": symbol,
            "side": side,
            "quantity": slice_quantity,
            "status": "FILLED",
            "slice_number": i + 1,
            "timestamp": datetime.utcnow().isoformat(),
            "mode": "SIMULATION",
        }

        logger.info(f"[TWAP] Executed slice {i+1}: {order}")
        executed_orders.append(order)

        time.sleep(interval)

    return {
        "strategy": "TWAP",
        "total_quantity": total_quantity,
        "slices": slices,
        "interval_seconds": interval,
        "orders_executed": executed_orders,
        "status": "COMPLETED",
    }


def place_twap_order(symbol, side, quantity, slices, interval):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(quantity)

        if slices <= 0 or interval < 0:
            raise ValueError("Slices must be > 0 and interval >= 0")

        logger.info(
            f"Placing TWAP | Symbol: {symbol} | Side: {side} | Qty: {quantity} | Slices: {slices} | Interval: {interval}"
        )

        if TEST_MODE:
            result = simulate_twap(symbol, side, quantity, slices, interval)
        else:
            raise NotImplementedError("Live API mode not enabled.")

        print("TWAP execution completed!")
        print(result)

    except Exception as e:
        logger.error(f"TWAP execution failed: {str(e)}")
        print(" TWAP failed:", str(e))


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python -m src.advanced.twap SYMBOL SIDE QUANTITY SLICES INTERVAL")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    slices = int(sys.argv[4])
    interval = int(sys.argv[5])

    place_twap_order(symbol, side, quantity, slices, interval)