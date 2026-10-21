from pipeline.validator import validate
from pipeline.schema import TransactionBatch
from pipeline.transformer import clean_data
from pipeline.reporter import show_report


data = [
    {"branch": "A", "date": "2026-10-01",
     "tier": "Gold", "items": 2, "revenue": 100},

    {"branch": "B", "date": "2026-10-02",
     "tier": "Silver", "items": 3, "revenue": 150},

    {"branch": "A", "date": "2026-10-03",
     "tier": "Gold", "items": 1, "revenue": 50},

    {"branch": "C", "date": "2026-10-04",
     "tier": "Bronze", "items": 1, "revenue": -20},

    {"branch": "", "date": "2026-10-05",
     "tier": "Silver", "items": 2, "revenue": 80}
]

valid_records = [validate(item) for item in data]
valid_records = [r for r in valid_records if r is not None]

batch = TransactionBatch(valid_records)
clean_records = clean_data(batch.get_records())

show_report(clean_records, len(data))
