from datetime import datetime

class Transaction:
    def __init__(self, amount, category, t_type, description=""):
        self.amount = amount
        self.category = category       # e.g. "Food", "Rent", "Salary"
        self.t_type = t_type           # "income" or "expense"
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.t_type == "income")
        expenses = sum(t.amount for t in self.transactions if t.t_type == "expense")
        return income - expenses

    def get_summary(self):
        # Group expenses by category
        summary = {}
        for t in self.transactions:
            summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary