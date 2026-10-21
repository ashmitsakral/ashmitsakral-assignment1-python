from pipeline.transformer import total_sales

def show_report(records, total_input):
    print("\nRETAIL ANALYTICS REPORT")

    sales = total_sales(records)

    retention = (
        len(records) / total_input * 100
        if total_input else 0
    )

    print("Valid transactions:", len(records))
    print("Total sales: $", round(sales, 2))
    print("Retention rate:", round(retention, 1), "%")

    branch_sales = {}

    for record in records:
        branch = record.branch
        branch_sales[branch] = (
            branch_sales.get(branch, 0) + record.revenue
        )

    if branch_sales:
        best_branch = max(branch_sales, key=branch_sales.get)
        print("Best branch:", best_branch)

    print("\nCustomer tier breakdown:")

    for tier in sorted(set(r.tier for r in records)):
        count = sum(1 for r in records if r.tier == tier)
        print(tier + ":", count)
