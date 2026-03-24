from flask import Flask, render_template, request, jsonify
from tracker import Transaction, FinanceTracker
from database import Database
from tax import calculate_ontario_income_tax, calculate_hst

app = Flask(__name__)
db = Database()
tracker = FinanceTracker()

for row in db.fetch_all():
    t = Transaction(row[1], row[2], row[3], row[4])
    t.date = row[5]
    tracker.add_transaction(t)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/summary")
def summary():
    return jsonify({
        "balance": round(tracker.get_balance(), 2),
        "income": round(sum(t.amount for t in tracker.transactions if t.t_type == "income"), 2),
        "expenses": round(sum(t.amount for t in tracker.transactions if t.t_type == "expense"), 2),
        "summary": tracker.get_summary(),
        "transactions": [
            {
                "amount": t.amount,
                "category": t.category,
                "type": t.t_type,
                "description": t.description,
                "date": t.date
            } for t in reversed(tracker.transactions[-10:])
        ]
    })

@app.route("/api/add", methods=["POST"])
def add_transaction():
    data = request.json
    t = Transaction(
        float(data["amount"]),
        data["category"],
        data["type"],
        data.get("description", "")
    )
    tracker.add_transaction(t)
    db.insert(t)
    return jsonify({"status": "ok"})

@app.route("/api/tax", methods=["POST"])
def tax():
    data = request.json
    result = calculate_ontario_income_tax(float(data["income"]))
    return jsonify(result)

@app.route("/api/hst", methods=["POST"])
def hst():
    data = request.json
    result = calculate_hst(float(data["amount"]))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
