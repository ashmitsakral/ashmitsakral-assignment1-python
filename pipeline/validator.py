from datetime import datetime
from pipeline.schema import TransactionRecord


def validate(data):
    try:
        branch = data["branch"]
        date = data["date"]
        tier = data["tier"]
        items = int(data["items"])
        revenue = float(data["revenue"])

        datetime.strptime(date, "%Y-%m-%d")

        if not branch or not tier:
            return None

        if items < 0 or revenue < 0:
            return None

        return TransactionRecord(branch, date, tier, items, revenue)

    except (KeyError, ValueError, TypeError):
        return None
