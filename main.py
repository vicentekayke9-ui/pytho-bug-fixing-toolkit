import logging
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def calculate_total(price: float, quantity: int) -> float:
    """Calculate the total price safely."""

    if price < 0:
        raise ValueError("Price cannot be negative.")

    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    return round(price * quantity, 2)


def process_order(order: dict[str, Any]) -> float:
    """Validate an order and calculate its total."""

    required_fields = {"price", "quantity"}

    missing_fields = required_fields - order.keys()

    if missing_fields:
        raise ValueError(
            f"Missing fields: {', '.join(sorted(missing_fields))}"
        )

    try:
        price = float(order["price"])
        quantity = int(order["quantity"])
    except (TypeError, ValueError) as error:
        raise ValueError("Price and quantity must be valid numbers.") from error

    total = calculate_total(price, quantity)

    logging.info(
        "Order processed successfully: price=%s quantity=%s total=%s",
        price,
        quantity,
        total
    )

    return total


if __name__ == "__main__":
    example_order = {
        "price": 19.99,
        "quantity": 3
    }

    try:
        total = process_order(example_order)
        print(f"Total: ${total:.2f}")
    except ValueError as error:
        logging.error("Could not process order: %s", error)
