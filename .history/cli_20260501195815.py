import argparse
import logging

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True, help="Symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, required=False)

    args = parser.parse_args()

    try:
        validate_order(
            args.symbol,
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        client = get_client()

        order = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\n=== ORDER SUMMARY ===")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        print("\n=== RESPONSE ===")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

        print("\n✅ SUCCESS")

    except Exception as e:
        print("\n❌ FAILED:", str(e))
        logging.error(f"CLI Error: {str(e)}")


if __name__ == "__main__":
    main()