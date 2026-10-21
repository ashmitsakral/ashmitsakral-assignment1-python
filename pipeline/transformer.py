def clean_data(records):
    return list(filter(lambda r: r.revenue > 0, records))


def total_sales(records):
    revenues = map(lambda r: r.revenue, records)
    return sum(revenues)


def get_customer_count(records, tier):
    return sum(1 for r in records if r.tier == tier)
