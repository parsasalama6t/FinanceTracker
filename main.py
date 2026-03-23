from tracker import Transaction, FinanceTracker
from database import Database

def main():
    db = Database()
    tracker = FinanceTracker()

    # Load existing transactions from DB on startup
    for row in db.fetch_all():
        t = Transaction(row[1], row[2], row[3], row[4])
        t.date = row[5]
        tracker.add_transaction(t)

    while True:
        print("\n===== Finance Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Summary by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount: $"))
            category = input("Category (e.g. Salary, Freelance): ")
            desc = input("Description (optional): ")
            t = Transaction(amount, category, "income", desc)
            tracker.add_transaction(t)
            db.insert(t)
            print("✅ Income added.")

        elif choice == "2":
            amount = float(input("Amount: $"))
            category = input("Category (e.g. Food, Rent, Transport): ")
            desc = input("Description (optional): ")
            t = Transaction(amount, category, "expense", desc)
            tracker.add_transaction(t)
            db.insert(t)
            print("✅ Expense added.")

        elif choice == "3":
            print(f"\n💰 Current Balance: ${tracker.get_balance():.2f}")

        elif choice == "4":
            summary = tracker.get_summary()
            print("\n📊 Spending by Category:")
            for cat, total in summary.items():
                print(f"  {cat}: ${total:.2f}")

        elif choice == "5":
            db.close()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()