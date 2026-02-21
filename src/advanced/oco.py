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


def simulate_market_price():
    """
    Simulate market price movement.
    Change this value to test different scenarios.
    """
    return 61000  


def simulate_oco_order(symbol, side, quantity, take_profit, stop_loss):
    current_price = simulate_market_price()

    logger.info(f"Current simulated market price: {current_price}")

    tp_order_id = str(uuid.uuid4())
    sl_order_id = str(uuid.uuid4())

    result = {
        "symbol": symbol,
        "side": side,
        "quantity": quantity,
        "take_profit": take_profit,
        "stop_loss": stop_loss,
        "timestamp": datetime.utcnow().isoformat(),
        "mode": "SIMULATION",
    }

    if side == "BUY":
        if current_price >= take_profit:
            result["status"] = "TAKE_PROFIT_EXECUTED"
            result["executed_order_id"] = tp_order_id
            result["cancelled_order_id"] = sl_order_id
        elif current_price <= stop_loss:
            result["status"] = "STOP_LOSS_EXECUTED"
            result["executed_order_id"] = sl_order_id
            result["cancelled_order_id"] = tp_order_id
        else:
            result["status"] = "PENDING"

    elif side == "SELL":
        if current_price <= take_profit:
            result["status"] = "TAKE_PROFIT_EXECUTED"
            result["executed_order_id"] = tp_order_id
            result["cancelled_order_id"] = sl_order_id
        elif current_price >= stop_loss:
            result["status"] = "STOP_LOSS_EXECUTED"
            result["executed_order_id"] = sl_order_id
            result["cancelled_order_id"] = tp_order_id
        else:
            result["status"] = "PENDING"

    logger.info(f"[SIMULATION] OCO result: {result}")
    return result


def place_oco_order(symbol, side, quantity, take_profit, stop_loss):
    try:
        validate_symbol(symbol)
        validate_side(side)
        validate_quantity(quantity)
        validate_price(take_profit)
        validate_price(stop_loss)

        logger.info(
            f"Placing OCO | Symbol: {symbol} | Side: {side} | Qty: {quantity} | TP: {take_profit} | SL: {stop_loss}"
        )

        if TEST_MODE:
            order = simulate_oco_order(
                symbol, side, quantity, take_profit, stop_loss
            )
        else:
            raise NotImplementedError("Live API mode not enabled.")

        print(" OCO order processed!")
        print(order)

    except Exception as e:
        logger.error(f"OCO order failed: {str(e)}")
        print(" Order failed:", str(e))


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python -m src.advanced.oco SYMBOL SIDE QUANTITY TAKE_PROFIT STOP_LOSS")
        sys.exit(1)

    symbol = sys.argv[1]
    side = sys.argv[2]
    quantity = float(sys.argv[3])
    take_profit = float(sys.argv[4])
    stop_loss = float(sys.argv[5])

    place_oco_order(symbol, side, quantity, take_profit, stop_loss)