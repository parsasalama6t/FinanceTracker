# 💰 Personal Finance Tracker

A command-line application built in Python to track income and expenses,
categorize spending, and generate financial summaries — with persistent 
storage powered by SQLite.

## Features
- Add income and expense transactions
- View current balance in real time
- Spending summary broken down by category
- Persistent data storage with SQLite (data saved between sessions)
- Clean CLI menu interface

## Tech Stack
- **Language:** Python 3
- **Database:** SQLite3 (built-in)
- **Architecture:** OOP with separated modules

## Project Structures
finance_tracker/
├── main.py        # Entry point and CLI menu
├── tracker.py     # Transaction and FinanceTracker classes
├── database.py    # SQLite connection and queries
├── finance.db     # Local database (auto-generated)
└── test.py        # Manual testing script

## How to Run
1. Clone the repository
   git clone https://github.com/parsasalama6t/FinanceTracker.git

2. Navigate into the folder
   cd FinanceTracker

3. Run the app
   python3 main.py

## What I Learned
- Designing a multi-class OOP architecture in Python
- Working with SQLite databases using Python's sqlite3 module
- Separating business logic from data persistence layers
- Building a user-friendly CLI menu with persistent state