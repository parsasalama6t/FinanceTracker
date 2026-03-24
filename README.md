# 💰 Personal Finance Tracker

A full stack web application built with Python and Flask to track income
and expenses, categorize spending, calculate Canadian taxes, and visualize
financial summaries — with persistent storage powered by SQLite.

## Features
- Add income and expense transactions through a clean web interface
- Real-time balance, income, and expense summary cards
- Spending breakdown by category with visual progress bars
- Recent transactions list with income/expense badges
- Ontario income tax calculator using 2024 federal + provincial brackets
- After-tax take-home income calculation with effective tax rate
- HST (13%) calculator for expense amounts
- Flask REST API backend serving a dynamic HTML/CSS/JS frontend
- Persistent data storage with SQLite (data saved between sessions)

## Tech Stack
- **Language:** Python 3
- **Web Framework:** Flask
- **Database:** SQLite3 (built-in)
- **Frontend:** HTML, CSS, JavaScript
- **Architecture:** REST API backend + OOP business logic
- **Tax Logic:** 2024 Canada Revenue Agency + Ontario tax brackets

## Project Structure
```
FinanceTracker/
├── app.py              # Flask server and REST API routes
├── tracker.py          # Transaction and FinanceTracker classes
├── database.py         # SQLite connection and queries
├── tax.py              # Ontario income tax and HST calculators
├── templates/
│   └── index.html      # Main web dashboard
├── static/
│   ├── style.css       # Styling and layout
│   └── script.js       # Frontend logic and API calls
├── finance.db          # Local database (auto-generated)
└── test.py             # Manual testing script
```

## How to Run
1. Clone the repository
```
git clone https://github.com/parsasalama6t/FinanceTracker.git
```

2. Navigate into the folder
```
cd FinanceTracker
```

3. Install dependencies
```
pip3 install flask
```

4. Run the app
```
python3 app.py
```

5. Open your browser and go to
```
http://127.0.0.1:5000
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serves the web dashboard |
| GET | `/api/summary` | Returns balance, income, expenses, and recent transactions |
| POST | `/api/add` | Adds a new income or expense transaction |
| POST | `/api/tax` | Calculates Ontario income tax for a given salary |
| POST | `/api/hst` | Calculates HST (13%) for a given amount |

## Tax Calculations
### Income Tax
Enter your annual gross salary and get a full breakdown:
- Federal tax (2024 brackets)
- Ontario provincial tax (2024 brackets)
- Total tax owed
- After-tax take-home income
- Effective tax rate (%)

### HST
Enter any pre-tax expense amount and instantly see:
- HST amount (13%)
- Total after-tax cost

## What I Learned
- Building a full stack web application with Python and Flask
- Designing and consuming a REST API from a JavaScript frontend
- Working with SQLite databases using Python's sqlite3 module
- Separating business logic, data persistence, and API layers
- Implementing real-world Canadian tax bracket calculations
- Structuring a multi-file Python project with clean architecture
