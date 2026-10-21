from pipeline.validator import validate
from pipeline.transformer import total_sales

data = {
    "branch": "A",
    "date": "2026-10-01",
    "tier": "Gold",
    "items": 2,
    "revenue": 100
}

# Test 1: Valid transaction
assert validate(data) is not None
print("Test 1 passed: Valid transaction")

# Test 2: Negative revenue
bad_data = {**data, "revenue": -10}
assert validate(bad_data) is None
print("Test 2 passed: Negative revenue rejected")

# Test 3: Total sales
record = validate(data)
assert total_sales([record]) == 100
print("Test 3 passed: Total sales calculated")

print("\nAll tests passed!")
