from datetime import datetime

CURRENCY_MAP = {
    "₹": "INR",
    "$": "USD",
    "€": "EUR",
    "£": "GBP",
}


def normalize_currency(value):
    if value is None:
        return None

    value = str(value).strip()

    if value in CURRENCY_MAP:
        return CURRENCY_MAP[value]

    return value.upper()


def normalize_date(value):
    if value is None:
        return None

    formats = [
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%d %B %Y",
        "%Y-%m-%d",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass

    return value