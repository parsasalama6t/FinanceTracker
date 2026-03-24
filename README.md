# 💰 Personal Finance Tracker

A command-line application built in Python to track income and expenses,
categorize spending, calculate Canadian taxes, and generate financial 
summaries — with persistent storage powered by SQLite.

## Features
- Add income and expense transactions
- View current balance in real time
- Spending summary broken down by category
- Persistent data storage with SQLite (data saved between sessions)
- Ontario income tax calculator using 2024 federal + provincial brackets
- After-tax take-home income calculation with effective tax rate
- HST (13%) calculator for expense amounts
- Clean CLI menu interface

## Tech Stack
- **Language:** Python 3
- **Database:** SQLite3 (built-in)
- **Architecture:** OOP with separated modules
- **Tax Logic:** 2024 Canada Revenue Agency + Ontario brackets

## Project Structure
finance_tracker/
├── main.py        # Entry point and CLI menu
├── tracker.py     # Transaction and FinanceTracker classes
├── database.py    # SQLite connection and queries
├── tax.py         # Ontario income tax and HST calculators
├── finance.db     # Local database (auto-generated)
└── test.py        # Manual testing script

## How to Run
1. Clone the repository
   git clone https://github.com/parsasalama6t/FinanceTracker.git

2. Navigate into the folder
   cd FinanceTracker

3. Run the app
   python3 main.py

## Tax Calculations
### Income Tax (Option 5)
Enter your annual gross salary and get a full breakdown:
- Federal tax (2024 brackets)
- Ontario provincial tax (2024 brackets)
- Total tax owed
- After-tax take-home income
- Effective tax rate (%)

### HST (Option 6)
Enter any pre-tax expense amount and instantly see:
- HST amount (13%)
- Total after-tax cost

## What I Learned
- Designing a multi-class OOP architecture in Python
- Working with SQLite databases using Python's sqlite3 module
- Separating business logic from data persistence layers
- Implementing real-world Canadian tax bracket logic
- Building a user-friendly CLI menu with persistent state
```
