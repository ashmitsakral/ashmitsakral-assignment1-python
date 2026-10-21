class TransactionRecord:
    def __init__(self, branch, date, tier, items, revenue):
        self.branch = branch
        self.date = date
        self.tier = tier
        self.items = items
        self.revenue = revenue


class TransactionBatch:
    def __init__(self, records):
        self.records = records

    def get_records(self):
        return self.records
