from tracker import Transaction, FinanceTracker

tracker = FinanceTracker()

tracker.add_transaction(Transaction(2000, "Salary", "income", "Monthly pay"))
tracker.add_transaction(Transaction(500, "Rent", "expense", "Monthly rent"))
tracker.add_transaction(Transaction(100, "Food", "expense", "Groceries"))

print(tracker.get_balance())
print(tracker.get_summary())

