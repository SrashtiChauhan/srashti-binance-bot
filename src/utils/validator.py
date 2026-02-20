import re
from utils.logger import logger

def validate_symbol(symbol: str):
    pattern = r"^[A-Z]{3,}USDT$"
    if not re.match(pattern, symbol):
        logger.error(f"Invalid symbol format: {symbol}")
        raise ValueError("Invalid symbol. Example valid format: BTCUSDT")
    
def validate_side(side: str):
        if side not in ["BUY", "SELL"]:
            logger.error(f"Invalid side: {side}")
            raise ValueError("Side must be BUY or SELL")
    
def validate_quantity(quantity: float):
        if quantity <= 0:
            logger.error(f"Invalid quantity: {quantity}")
            raise ValueError("Quantity must be greater than 0")
    
def validate_price(price: float):
        if price <= 0:
            logger.error(f"Invalid price: {price}")
            raise ValueError("Price must be greater than 0")
    