from tracker import Transaction, FinanceTracker
from database import Database
from tax import calculate_ontario_income_tax, calculate_hst

def main():
    db = Database()
    tracker = FinanceTracker()

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
        print("5. Calculate Ontario Income Tax")
        print("6. Calculate HST on Expense")
        print("7. Exit")

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
            income = float(input("\nEnter your annual gross income: $"))
            result = calculate_ontario_income_tax(income)
            print(f"\n📋 Tax Breakdown for ${income:,.2f}")
            print(f"  Federal Tax:       ${result['federal_tax']:,.2f}")
            print(f"  Ontario Tax:       ${result['ontario_tax']:,.2f}")
            print(f"  Total Tax:         ${result['total_tax']:,.2f}")
            print(f"  After-Tax Income:  ${result['after_tax']:,.2f}")
            print(f"  Effective Rate:    {result['effective_rate']}%")

        elif choice == "6":
            amount = float(input("\nEnter expense amount (before HST): $"))
            result = calculate_hst(amount)
            print(f"\n🧾 HST Breakdown")
            print(f"  Pre-tax Amount:  ${result['pre_tax']:,.2f}")
            print(f"  HST (13%):       ${result['hst']:,.2f}")
            print(f"  Total:           ${result['total']:,.2f}")

        elif choice == "7":
            db.close()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
